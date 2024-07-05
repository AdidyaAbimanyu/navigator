import os
from flask import Flask, render_template, send_file, jsonify, request
from prototype import *
from city_nodes import city_node_map  # Import city_node_map

app = Flask(__name__)

# Define the directory to save images
IMAGE_DIR = os.path.join(app.root_path, 'static', 'images')

# Ensure the directory exists
os.makedirs(IMAGE_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_city', methods=['POST'])
def send_city():
    data = request.get_json()
    selected_city = data['city']

    # Debug
    print(data['city'])
    
    global G
    global place_start
    global place_end
    global start_label
    global end_label
    
    # Retrieve start and end nodes from city_node_map
    place_north = city_node_map[selected_city]["north"]
    place_south = city_node_map[selected_city]["south"]
    place_east = city_node_map[selected_city]["east"]
    place_west = city_node_map[selected_city]["west"]
    place_start = city_node_map[selected_city]["start"]
    place_end = city_node_map[selected_city]["end"]
    start_label = city_node_map[selected_city]["orig_name"]
    end_label = city_node_map[selected_city]["dest_name"]

    
    G = load_graph(place_north, place_south, place_east, place_west)
    return jsonify({'message': 'City received and graph loaded successfully!'})

@app.route('/route')
def route():
    # Use the start and end nodes retrieved based on the city
    start = place_start
    end = place_end
    label_start = start_label
    label_end = end_label
    
    # Perform A* search and get path information
    a_star_path = a_star(G, start, end, label_start, label_end)
    
    # Ensure a_star_path is initialized as a dictionary
    if a_star_path is None:
        a_star_path = {}

    # Create unique filenames for images
    a_star_image_filename = f"a_star_{start}_{end}.png"
    a_star_image_path = os.path.join(IMAGE_DIR, a_star_image_filename)
    plot_graph(G, filename=a_star_image_path)

    # Get the path information and distance
    dist, speed = reconstruct_path(G, start, end)
    
    path_info = {
        'dist': dist,  # Store the distance in path_info
        'speed': speed  # Store the speed in path_info
    }
    
    path_image_filename = f"path_{start}_{end}.png"
    path_image_path = os.path.join(IMAGE_DIR, path_image_filename)
    
    # Plot graphs and save images
    plot_graph(G, filename=path_image_path)
    
    # Update path_info with image URLs
    a_star_path["a_star_image"] = f'/image/{a_star_image_filename}'
    path_info["path_image"] = f'/image/{path_image_filename}'
    
    # Combine both dictionaries to pass to the template
    context = {
        "a_star_path": a_star_path,
        "path_info": path_info
    }
    
    return render_template('route.html', **context)


@app.route('/image/<filename>')
def get_image(filename):
    return send_file(os.path.join(IMAGE_DIR, filename), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
