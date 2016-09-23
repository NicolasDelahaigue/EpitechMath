//
// Created by kevin on 28/12/15.
//

#include									"mapLoader.hh"

mapLoader::mapLoader(std::string path) {
	try {
		this->file.open(path);
	} catch (std::ifstream::failure e) {
		std::cerr << e.what() << std::endl;
		exit(84);
	}
}

mapLoader::~mapLoader() {
	try {
		this->file.close();
	} catch (std::ifstream::failure e) {
		std::cerr << e.what() << std::endl;
		exit(84);
	}
}

void										mapLoader::parse() {
	std::string								item;
	std::string								line;
	char									delim = ';';

	try {
		while (getline(this->file, line)) {
			std::stringstream									ss(line);
			std::pair<float, float>								elem;
			std::vector<std::pair<float, float>>::iterator		it = this->points.begin();

			if (std::count(line.begin(), line.end(), delim) != 1) {
				std::cerr << "bad file" << std::endl;
				exit(-1);
			}
			std::getline(ss, item, delim);
			elem.first = std::stof(item.c_str());
			std::getline(ss, item, delim);
			elem.second = std::stof(item.c_str());

			this->points.insert(it, elem);
		}
	} catch (std::ifstream::failure e) {
		std::cerr << e.what() << std::endl;
		exit(84);
	} catch (std::invalid_argument e) {
		std::cerr << e.what() << std::endl;
		exit(84);
	} catch (std::out_of_range e) {
		std::cerr << e.what() << std::endl;
		exit(84);
	}
}

std::vector<std::pair<float, float>>		mapLoader::getMap() {
	return this->points;
}

std::pair<float, float>						mapLoader::min_pts() {
	std::vector<std::pair<float, float>>::iterator		it = this->points.begin();
	float												min_x = it->first;
	float												min_y = it->second;

	for (it; it < this->points.end(); it++) {
		min_x = ((min_x > it->first) ? it->first : min_x);
		min_y = ((min_y > it->second) ? it->second : min_y);
	}
	return std::make_pair(min_x, min_y);
}

std::pair<float, float> 					mapLoader::max_pts() {
	std::vector<std::pair<float, float>>::iterator		it = this->points.begin();
	float												max_x = it->first;
	float												max_y = it->second;

	for (it; it < this->points.end(); it++) {
		max_x = ((max_x < it->first) ? it->first : max_x);
		max_y = ((max_y < it->second) ? it->second : max_y);
	}
	return std::make_pair(max_x, max_y);
}
