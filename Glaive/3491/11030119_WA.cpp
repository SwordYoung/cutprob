#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

double pai = 3.1415927;

typedef struct {
	double x;
	double y;
} Point;

double eq(double d0, double d1, bool sqr = false) {
	// return sqr ? (abs(d0 - d1) < (d0 / 10000)) : abs(d0 - d1) < 0.01;
	return sqr ? eq(sqrt(d0), sqrt(d1)) : abs(d0 - d1) < (abs(d0 - d1) / 100);
}

double get_angle(double x, double y) {
	double res = 0;
	if (x > 0) res = atan(y / x);
	if (x < 0 && y >= 0) res = atan(y / x) + pai;
	if (x < 0 && y < 0) res = atan(y / x) - pai;
	if (x == 0 && y > 0) res = pai / 2;
	if (x == 0 && y < 0) res = -pai / 2;
	if (x == 0 && y == 0) res = 0;
	// cout << "angle: " << x << " " << y << " " << res << endl;
	assert(res < 3.14160 && res > -3.14160);
	return res;
}

bool fit(Point& p0, Point& p1, double scale_sqr, double angle) {
	double l0 = p0.x * p0.x + p0.y * p0.y;
	double l1 = p1.x * p1.x + p1.y * p1.y;
	// cout << "l0 = " << l0 << "; l1 = " << l1 << endl;
	if (!eq(l0, l1 * scale_sqr, true)) {
		return false;
	}
	if (l0 == 0) return true;
	assert(l1 != 0);
	double angle0 = get_angle(p0.x, p0.y);
	double angle1 = get_angle(p1.x, p1.y);
	double angle_delta = angle0 - angle1;
	if (angle_delta > pai ) angle_delta = angle_delta - 2 * pai;
	if (angle_delta < -pai) angle_delta = angle_delta + 2 * pai;
	// cout << "s angle0 = " << angle0 << endl;
	// cout << "s angle1 = " << angle1 << endl;
	// cout << "angle_delta = " << angle_delta << endl;
	// cout << "s delta_angle = " << (angle_delta / 3.1415926) * 180 << endl;
	return eq(angle, angle_delta);
}

bool has_result(Point* p0, Point* p1, int n, int i, double& res) {
	int s0 = 0; int s1 = i;

	double l0 = 0; double l1 = 0;
	while (l0 == 0 && l1 == 0 && s0 < n) {
		l0 = p0[s0].x * p0[s0].x + p0[s0].y * p0[s0].y;
		l1 = p1[s1].x * p1[s1].x + p1[s1].y * p1[s1].y;
		assert(l0 == 0 && l1 == 0 || l0 != 0 && l1 != 0);
		if (l0 == 0 && l1 == 0) {
	                s0++; s1++; if (s1 == n) s1 = 0;
		} else {
			break;
		}
	}
	if (s0 == n) {
		res = 0;
		return true;
	}

	// cout << "i = " << i << endl;
	double scale_sqr = l0 / l1;
	double angle0 = get_angle(p0[s0].x, p0[s0].y);
	double angle1 = get_angle(p1[s1].x, p1[s1].y);
	double angle = angle0 - angle1;
	// cout << "scale: " << scale_sqr << endl;
	// cout << "angle0 = " << angle0 << endl;
	// cout << "angle1 = " << angle1 << endl;
	// cout << "delta_angle = " << (angle / 3.1415926) * 180 << endl;

	int j1 = s1+1;
	for (int j0 = s0+1; j0 < n; ++j0, ++j1) {
		if (j1 == n) j1 = 0;
		// cout << "j0 = " << j0 << "; j1 = " << j1 << endl;
		if (!fit(p0[j0], p1[j1], scale_sqr, angle)) {
			// cout << "not fit" << endl;
			return false;
		}
	}
	res = angle;
	// cout << "fit" << endl;
	return true;
}

double result(Point* p0, Point* p1, int n) {
	double res = 0;
	for (int i = 0; i < n; ++i) {
		bool has_res = has_result(p0, p1, n, i, res);
		if (has_res) return res;
	}
	assert(0);
	return 0;
}

int main() {
	int n;
	cout.precision(2);
	cout.setf(ios::fixed);
	while (cin >> n) {
		Point* p0 = new Point[n];
		Point* p1 = new Point[n];
		for (int i = 0; i < n; ++i) {
			cin >> p0[i].x;
			cin >> p0[i].y;
		}
		for (int i = 0; i < n; ++i) {
			cin >> p1[i].x;
			cin >> p1[i].y;
		}

		double res = result(p0, p1, n);
		res = (res / pai) * 180;
		if (res < 0) res += 360;
		res = 360 - res;
		cout << res << endl;
		delete [] p0;
		delete [] p1;
	}
	return 0;
}