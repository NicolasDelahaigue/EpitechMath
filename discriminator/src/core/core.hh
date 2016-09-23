//
// Created by kevin on 28/12/15.
//

#pragma once

#include						<iostream>

#include						"../loader/mapLoader.hh"
#include						"quadtree/QuadTree.hh"
#include						"../algo/algo.hh"

class							core {
private:
	int 						cloud;	// number of cloud in the map
	mapLoader					ml;		// map itself
	QuadTree					*qt;	// QuadTree implementation to count the number of cloud in the map
	Algo						algo;	// algorithm implementation who is used to calculate the number of cloud

	/**
	 *	calculate the center coordinate of the map
	 *
	 *	@param min_pts	=>	location of the points in the bottom-left corner of the map
	 *	@param max_pts	=>	location of the points in the top-right corner of the map
	 */
	std::pair<float, float>		getCenter(std::pair<float, float> const&min_pts, std::pair<float, float> const&max_pts);

	/**
	 *	calculate the dim of the map and divide it by 2
	 *
	 *	@param min_pts	=>	location of the points in the bottom-left corner of the map
	 *	@param max_pts	=>	location of the points in the top-right corner of the map
	 */
	float						getDim(std::pair<float, float> const&min_ptr, std::pair<float, float> const&max_ptr);

public:
	/**
	 * constructor, take the path of the file who
	 * contain the map to calculate
	 */
	core(std::string path);
	~core();

	/**
	 * the beginning =)
	 */
	void 						run();

	/**
	 * construction of the QuadTree
	 */
	bool 						build_tree();

	/**
	 * display the number of cloud in the map
	 */
	int 						getCloud() const;
};
