from rgbmatrix import RGBMatrix, RGBMatrixOptions

def init():
    global device
    # Configure Matrix
    options = RGBMatrixOptions()
    options.rows = 64 # Put your display height here
    options.cols = 64 # Put your display width here
    options.pixel_mapper_config = 'Rotate:180' # Put any rotation you need here
    options.hardware_mapping = 'adafruit-hat'  # Put your display type here
    options.chain_length = 1
    options.parallel = 1

    # Initialise Matrix
    device = RGBMatrix(options = options)