import os
from flask import Flask, render_template, send_file
from prototype import *
import random
import tempfile

app = Flask(__name__)

# Load graph
place_name = "Solo, Indonesia"
G = load_graph(place_name)

# Define the directory to save images
IMAGE_DIR = os.path.join(app.root_path, 'static', 'images')

# Ensure the directory exists
os.makedirs(IMAGE_DIR, exist_ok=True)

@app.route('/')
def index():
    return 'Welcome to the prototype server!'

@app.route('/run_algorithm')
def run_algorithm():
    start = random.choice(list(G.nodes))
    end = random.choice(list(G.nodes))
    a_star(G, start, end, plot=True)
    reconstruct_path(G, start, end, plot=True)
    return 'Algorithm executed successfully!'

@app.route('/plot_image')
def plot_image():
    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    plot_graph(G, filename=temp_file.name)
    return send_file(temp_file.name, mimetype='image/png')

@app.route('/route')
def route():
    start = random.choice(list(G.nodes))
    end = random.choice(list(G.nodes))
    
    # Perform A* search and get path information
    a_star(G, start, end)
    path_info = reconstruct_path(G, start, end)
    
    # Create unique filenames for images
    a_star_image_filename = f"a_star_{start}_{end}.png"
    a_star_image_path = os.path.join(IMAGE_DIR, a_star_image_filename)
    
    path_image_filename = f"path_{start}_{end}.png"
    path_image_path = os.path.join(IMAGE_DIR, path_image_filename)
    
    # Plot graphs and save images
    plot_graph(G, filename=a_star_image_path)
    plot_graph(G, filename=path_image_path)
    
    # Update path_info with image URLs
    path_info["a_star_image"] = f'/image/{a_star_image_filename}'
    path_info["path_image"] = f'/image/{path_image_filename}'
    
    return render_template('route.html', path_info=path_info)

@app.route('/image/<filename>')
def get_image(filename):
    return send_file(os.path.join(IMAGE_DIR, filename), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
