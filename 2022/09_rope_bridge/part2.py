from collections import defaultdict

with open("input.txt", "r") as file:

    d = defaultdict(int)

    H0x = 0
    H0y = 0
    H1x = 0
    H1y = 0
    H2x = 0
    H2y = 0
    H3x = 0
    H3y = 0
    H4x = 0
    H4y = 0
    H5x = 0
    H5y = 0
    H6x = 0
    H6y = 0
    H7x = 0
    H7y = 0
    H8x = 0
    H8y = 0
    H9x = 0
    H9y = 0

    for line in file:
        line = line.strip()
        direction, distance = line.split()
        for i in range(int(distance)):
            if direction == "R":
                H0x += 1
            elif direction == "L":
                H0x -= 1
            elif direction == "U":
                H0y += 1
            elif direction == "D":
                H0y -= 1

            # H0-H1
            H01x_diff = H0x-H1x
            H01y_diff = H0y-H1y
            if H01y_diff == 0 and H01x_diff > 1:
                H1x += 1
            elif H01y_diff == 0 and H01x_diff < -1:
                H1x -= 1
            elif H01x_diff == 0 and H01y_diff > 1:
                H1y += 1
            elif H01x_diff == 0 and H01y_diff < -1:
                H1y -= 1
            elif abs(H01y_diff) > 1 or abs(H01x_diff) > 1:
                if H01y_diff > 0:
                    H1y += 1
                else:
                    H1y -= 1
                if H01x_diff > 0:
                    H1x += 1
                else:
                    H1x -= 1

            # H1-H2
            H12x_diff = H1x-H2x
            H12y_diff = H1y-H2y
            if H12y_diff == 0 and H12x_diff > 1:
                H2x += 1
            elif H12y_diff == 0 and H12x_diff < -1:
                H2x -= 1
            elif H12x_diff == 0 and H12y_diff > 1:
                H2y += 1
            elif H12x_diff == 0 and H12y_diff < -1:
                H2y -= 1
            elif abs(H12y_diff) > 1 or abs(H12x_diff) > 1:
                if H12y_diff > 0:
                    H2y += 1
                else:
                    H2y -= 1
                if H12x_diff > 0:
                    H2x += 1
                else:
                    H2x -= 1
            
            # H2-H3
            H23x_diff = H2x-H3x
            H23y_diff = H2y-H3y
            if H23y_diff == 0 and H23x_diff > 1:
                H3x += 1
            elif H23y_diff == 0 and H23x_diff < -1:
                H3x -= 1
            elif H23x_diff == 0 and H23y_diff > 1:
                H3y += 1
            elif H23x_diff == 0 and H23y_diff < -1:
                H3y -= 1
            elif abs(H23y_diff) > 1 or abs(H23x_diff) > 1:
                if H23y_diff > 0:
                    H3y += 1
                else:
                    H3y -= 1
                if H23x_diff > 0:
                    H3x += 1
                else:
                    H3x -= 1

            # H3-H4
            H34x_diff = H3x-H4x
            H34y_diff = H3y-H4y
            if H34y_diff == 0 and H34x_diff > 1:
                H4x += 1
            elif H34y_diff == 0 and H34x_diff < -1:
                H4x -= 1
            elif H34x_diff == 0 and H34y_diff > 1:
                H4y += 1
            elif H34x_diff == 0 and H34y_diff < -1:
                H4y -= 1
            elif abs(H34y_diff) > 1 or abs(H34x_diff) > 1:
                if H34y_diff > 0:
                    H4y += 1
                else:
                    H4y -= 1
                if H34x_diff > 0:
                    H4x += 1
                else:
                    H4x -= 1
            
            # H4-H5
            H45x_diff = H4x-H5x
            H45y_diff = H4y-H5y
            if H45y_diff == 0 and H45x_diff > 1:
                H5x += 1
            elif H45y_diff == 0 and H45x_diff < -1:
                H5x -= 1
            elif H45x_diff == 0 and H45y_diff > 1:
                H5y += 1
            elif H45x_diff == 0 and H45y_diff < -1:
                H5y -= 1
            elif abs(H45y_diff) > 1 or abs(H45x_diff) > 1:
                if H45y_diff > 0:
                    H5y += 1
                else:
                    H5y -= 1
                if H45x_diff > 0:
                    H5x += 1
                else:
                    H5x -= 1

            # H5-H6
            H56x_diff = H5x-H6x
            H56y_diff = H5y-H6y
            if H56y_diff == 0 and H56x_diff > 1:
                H6x += 1
            elif H56y_diff == 0 and H56x_diff < -1:
                H6x -= 1
            elif H56x_diff == 0 and H56y_diff > 1:
                H6y += 1
            elif H56x_diff == 0 and H56y_diff < -1:
                H6y -= 1
            elif abs(H56y_diff) > 1 or abs(H56x_diff) > 1:
                if H56y_diff > 0:
                    H6y += 1
                else:
                    H6y -= 1
                if H56x_diff > 0:
                    H6x += 1
                else:
                    H6x -= 1
                
            # H6-H7
            H67x_diff = H6x-H7x
            H67y_diff = H6y-H7y
            if H67y_diff == 0 and H67x_diff > 1:
                H7x += 1
            elif H67y_diff == 0 and H67x_diff < -1:
                H7x -= 1
            elif H67x_diff == 0 and H67y_diff > 1:
                H7y += 1
            elif H67x_diff == 0 and H67y_diff < -1:
                H7y -= 1
            elif abs(H67y_diff) > 1 or abs(H67x_diff) > 1:
                if H67y_diff > 0:
                    H7y += 1
                else:
                    H7y -= 1
                if H67x_diff > 0:
                    H7x += 1
                else:
                    H7x -= 1

            # H7-H8
            H78x_diff = H7x-H8x
            H78y_diff = H7y-H8y
            if H78y_diff == 0 and H78x_diff > 1:
                H8x += 1
            elif H78y_diff == 0 and H78x_diff < -1:
                H8x -= 1
            elif H78x_diff == 0 and H78y_diff > 1:
                H8y += 1
            elif H78x_diff == 0 and H78y_diff < -1:
                H8y -= 1
            elif abs(H78y_diff) > 1 or abs(H78x_diff) > 1:
                if H78y_diff > 0:
                    H8y += 1
                else:
                    H8y -= 1
                if H78x_diff > 0:
                    H8x += 1
                else:
                    H8x -= 1
            
            # H8-H9
            H89x_diff = H8x-H9x
            H89y_diff = H8y-H9y
            if H89y_diff == 0 and H89x_diff > 1:
                H9x += 1
            elif H89y_diff == 0 and H89x_diff < -1:
                H9x -= 1
            elif H89x_diff == 0 and H89y_diff > 1:
                H9y += 1
            elif H89x_diff == 0 and H89y_diff < -1:
                H9y -= 1
            elif abs(H89y_diff) > 1 or abs(H89x_diff) > 1:
                if H89y_diff > 0:
                    H9y += 1
                else:
                    H9y -= 1
                if H89x_diff > 0:
                    H9x += 1
                else:
                    H9x -= 1
            d[(H9x, H9y)] += 1
    print(len(d))