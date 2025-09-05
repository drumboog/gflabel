from __future__ import annotations

import argparse
import logging
import sys

from build123d import Axis, BuildPart, BuildSketch, Rectangle, Vector, extrude, fillet, chamfer

from ..util import unit_registry
from . import LabelBase

logger = logging.getLogger(__name__)


class RuggedBoxBase(LabelBase):
    """
    Generate a GridfinityRuggedBox-label body.

    Origin is positioned at the center of the label, with the label
    surface at z=0.

    Args:
        width_mm: The width of the label.
        recessed:
            Whether the label surface is resecced into the label (used
            for embossing) or just flat, for cutting away.

    """

    DEFAULT_WIDTH = None
    DEFAULT_WIDTH_UNIT = unit_registry.mm

    @classmethod
    def validate_arguments(cls, args):
        if args.width < 10:
            logger.warning(
                f"Warning: Small width ({args.width}) for rugged box base. Did you specify in mm?"
            )
        if not args.height:
            args.height = unit_registry.Quantity(15, unit_registry.mm)
        return super().validate_arguments(args)

    def __init__(self, args: argparse.Namespace):
        if args.width.units == unit_registry.u:
            sys.exit("Error: Cannot specify width in units for rugged box base")
        width_mm = args.width.to("mm").magnitude
        height_mm = args.height.to("mm").magnitude
        depth_mm = 1.5
        with BuildPart() as part:
            with BuildSketch() as _sketch:
                Rectangle(width_mm, height=height_mm)
            # Extrude the base up
            extrude(amount=-depth_mm)

            chamfer(objects = part.edges().filter_by(Axis.X), length=0.5)

            # 1 mm fillet all corners
            fillet(part.edges().filter_by(Axis.Z), radius=1)

        self.part = part.part
        self.area = Vector(width_mm - 5, height_mm - 5)
