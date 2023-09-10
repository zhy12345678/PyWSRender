#!/usr/bin/env python
"""
@author: Peter Corke
@author: Jesse Haviland
"""

# 2/8/95  changed D3 to 150.05mm which is closer to data from Lee, AKB86 and
# Tarn fixed errors in COG for links 2 and 3
# 29/1/91 to agree with data from Armstrong etal.  Due to their use
#  of modified D&H params, some of the offsets Ai, Di are
#  offset, and for links 3-5 swap Y and Z axes.
# 14/2/91 to use Paul's value of link twist (alpha) to be consistant
#  with ARCL.  This is the -ve of Lee's values, which means the
#  zero angle position is a righty for Paul, and lefty for Lee.

# all parameters are in SI units: m, radians, kg, kg.m2, N.m, N.m.s etc.

# from math import pi
import numpy as np
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH
from spatialmath import SE3
from spatialmath import base


class Puma560(DHRobot):
    """
    Class that models a Puma 560 manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool

    ``Puma560()`` is an object which models a Unimation Puma560 robot and
    describes its kinematic and dynamic characteristics using standard DH
    conventions.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.DH.Puma560()
        >>> print(robot)

    Defined joint configurations are:

    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration
    - qs, arm is stretched out in the x-direction
    - qn, arm is at a nominal non-singular configuration

    .. note::
        - SI units are used.
        - The model includes armature inertia and gear ratios.
        - The value of m1 is given as 0 here.  Armstrong found no value for it
          and it does not appear in the equation for tau1 after the
          substituion is made to inertia about link frame rather than COG
          frame.
        - Gravity load torque is the motor torque necessary to keep the joint
          static, and is thus -ve of the gravity caused torque.

    .. warning:: Compared to the MATLAB version of the Toolbox this model
        includes the pedestal, making the z-coordinates 26 inches larger.

    :references:
        - "A search for consensus among model parameters reported for the PUMA
          560 robot", P. Corke and B. Armstrong-Helouvry,
          Proc. IEEE Int. Conf. Robotics and Automation, (San Diego),
          pp. 1608-1613, May 1994. (for kinematic and dynamic parameters)
        - "A combined optimization method for solving the inverse kinematics
          problem", Wang & Chen, IEEE Trans. RA 7(4) 1991 pp 489-.
          (for joint angle limits)
        - https://github.com/4rtur1t0/ARTE/blob/master/robots/UNIMATE/puma560/parameters.m

    .. codeauthor:: Peter Corke
    """  # noqa

    def __init__(self, symbolic=False):
        self.N_Dof = 6

        if symbolic:
            import spatialmath.base.symbolic as sym

            zero = sym.zero()
            pi = sym.pi()
        else:
            from math import pi

            zero = 0.0

        deg = pi / 180
        inch = 0.0254

        base = 26.45 * inch  # from mounting surface to shoulder axis

        L = [
            RevoluteMDH(
                d=0,  # link length (Dennavit-Hartenberg notation)
                a=0,  # link offset (Dennavit-Hartenberg notation)
                alpha=0,  # link twist (Dennavit-Hartenberg notation)
                qlim=np.deg2rad([-45 , 45]),  # minimum and maximum joint angle
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([-45 , 135]),  # qlim=[-45*deg, 225*deg]
            ),
            PrismaticMDH(

                a=0,
                alpha=-pi / 2,
                qlim=np.deg2rad([ 0.24/deg , 0.40/deg]), # qlim=[-225*deg, 45*deg]
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=0,
                qlim=[-180 ,180],  # qlim=[-110*deg, 170*deg]
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=pi / 2,
                qlim=[20,160],
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=[-70,  70],
            ),
        ]

        super().__init__(
            L,
            name="Puma560",
            symbolic=symbolic,

        )





if __name__ == "__main__":  # pragma nocover

    puma = Puma560(symbolic=False)
    print(puma)
    print(puma.dynamics())

