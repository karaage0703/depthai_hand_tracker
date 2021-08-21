#!/usr/bin/env python3
import sys
sys.path.append("../..")
from HandTrackerRobotControlRenderer import HandTrackerRenderer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--edge', action="store_true",
                    help="Use Edge mode (postprocessing runs on the device)")
parser_tracker = parser.add_argument_group("Tracker arguments")
parser_tracker.add_argument('-i', '--input', type=str,
                            help="Path to video or image file to use as input (if not specified, use OAK color camera)")
parser_tracker.add_argument('-f', '--internal_fps', type=int,
                            help="Fps of internal color camera. Too high value lower NN fps (default= depends on the model)")
parser_tracker.add_argument("-r", "--resolution", choices=['full', 'ultra'], default='full',
                            help="Sensor resolution: 'full' (1920x1080) or 'ultra' (3840x2160) (default=%(default)s)")
parser_tracker.add_argument('--internal_frame_height', type=int,
                            help="Internal color camera frame height in pixels")
parser_tracker.add_argument('-t', '--trace', action="store_true",
                            help="Print some debug messages")
parser_renderer = parser.add_argument_group("Renderer arguments")
parser_renderer.add_argument('-o', '--output',
                             help="Path to output video file")
args = parser.parse_args()

if args.edge:
    from HandTrackerEdge import HandTracker
else:
    from HandTracker import HandTracker

dargs = vars(args)

tracker = HandTracker(
        input_src=args.input,
        use_lm=True,
        use_gesture=True,
        xyz=True,
        solo=True,
        crop=False,
        resolution=args.resolution,
        stats=True,
        trace=args.trace,
        )

renderer = HandTrackerRenderer(
        tracker=tracker,
        output=args.output)

while True:
    # Run hand tracker on next frame
    frame, hands = tracker.next_frame()
    if frame is None: break
    # Draw hands
    frame = renderer.draw(frame, hands)
    key = renderer.waitKey(delay=1)
    if key == 27 or key == ord('q'):
        break
    elif key == ord('c'):
        renderer.robot_calibration(hands)
renderer.exit()
tracker.exit()
