//
// Created by kevin on 28/12/15.
//

#include		"core.hh"

core::core(std::string path) : ml(path) {
	this->cloud = 0;
	this->qt = NULL;
}

core::~core() {}

void						core::run() {
	std::pair<float, float>	center;
	std::pair<float, float>	min;
	std::pair<float, float>	max;
	float 					dim;

	this->ml.parse();

	min = this->ml.min_pts();
	max = this->ml.max_pts();

	center = this->getCenter(min, max);
	dim = this->getDim(min, max);

	this->qt = new QuadTree(center.first,		// x => center
							center.second,		// y => center
							dim,				// half-dim
							0);					// deep

	if (!this->build_tree()) {
		std::cerr << "failed on build tree" << std::endl;
		exit(84);
	}
	this->qt->aff("");
//	std::cout	<< "qts node: "
//				<< this->qt->countNode() << std::endl;
	this->algo.init(this->qt);
}

bool				 			core::build_tree() {
	for (std::pair<float, float> i : this->ml.getMap()) {
//		std::cout << "insert: "
//				<< i.first << ";" << i.second
//				<< std::endl;

		if (!this->qt->insert(i)) {
			return false;
		}
	}
	return !this->qt->cleanTree();
}

int								core::getCloud() const { return this->cloud; }

/**
 * private method
 */

std::pair<float, float>			core::getCenter(const std::pair<float, float> &min,
												const std::pair<float, float> &max)
{
	float		x = min.first + (max.first - min.first) / 2;
	float 		y = min.second + (max.second - min.second) / 2;

	return std::make_pair(x, y);
}

float							core::getDim(const std::pair<float, float> &min,
				   const std::pair<float, float> &max)
{
	float			l = max.first - min.first;
	float			h = max.second - min.second;

	return ((l > h) ? l : h) / 2;
}
