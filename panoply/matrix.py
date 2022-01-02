import config

from rgbmatrix import RGBMatrix, RGBMatrixOptions

def init():
    global device
    # Configure Matrix
    options = RGBMatrixOptions()
    options.rows = config.DISPLAY_HEIGHT # Put your display height here
    options.cols = config.DISPLAY_WIDTH # Put your display width here
    options.pixel_mapper_config = 'Rotate:{}'.format(config.DISPLAY_ROTATION) # Put any rotation you need here
    options.hardware_mapping = config.DISPLAY_HARDWARE_MAPPING  # Put your display type here
    options.chain_length = 1
    options.parallel = 1

    # Initialise Matrix
    device = RGBMatrix(options = options)
