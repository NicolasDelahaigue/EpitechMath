//
// Created by kevin on 28/12/15.
//

#pragma once

#include 	<algorithm>
#include	<string>
#include	<sstream>
#include 	<fstream>
#include	<iostream>
#include	<utility>
#include	<vector>

/**
 * this class contain the map to parse
 * and extract each points and puts then in a vector of float pair
 */
class		mapLoader{
private:
	std::ifstream								file;
	/**
	 *	the container for points
	 */
	std::vector<std::pair<float, float>>		points;

public:
	mapLoader(std::string path);
	~mapLoader();

	/**
	 *	method use to parse and extract the data of the file
	 */
	void 										parse();

	/**
	 *	return the point's vector
	 */
	std::vector<std::pair<float, float>>		getMap();

	/**
	 *	find ans return the coordinates of the bottom-left corner
	 */
	std::pair<float, float>						min_pts();

	/**
	 *	find ans return the coordinates of the top-right corner
	 */
	std::pair<float, float>						max_pts();
};
