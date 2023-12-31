import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class Redandant(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.Redandant()
        >>> print(robot)
    """

    def __init__(self, symbolic=False):

        self.N_Dof = 7


        if symbolic:
            import spatialmath.base.symbolic as sym
            zero = sym.zero()
            pi = sym.pi()
        else:
            from math import pi
            zero = 0.0

        deg = pi / 180



        L=[
            RevoluteMDH(
                d=0,
                a=0,
                alpha=0,
                qlim=[-160 * deg, 160 * deg],
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=-pi/2,
                qlim=[-110 * deg, 110 * deg],
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=pi / 2,
                qlim=[-135 * deg, 135 * deg],
            ),
            PrismaticMDH(
                theta=-pi/2,
                a=0,
                alpha=0,
                qlim=[-266 * deg, 266 * deg],
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=0,
                qlim=[-100 * deg, 100 * deg],
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=-pi/2,
                qlim=[-266 * deg, 266 * deg],
            ),
            RevoluteMDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=[-20 * deg, 20 * deg],
            ),
        ]



        super().__init__(
            L,
            name="Redandant",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    Redandant = Redandant(symbolic=False)

