//
// Created by kevin on 28/12/15.
//

#ifndef			DISCRIMINATOR_ALGO_HH
#define			DISCRIMINATOR_ALGO_HH

#include		"../core/quadtree/QuadTree.hh"

/**
 * class ALgo will calculate clouds in the map
 */
class			Algo {
private:
	/**
	 * the pointer of the QuadTree
	 */
	QuadTree	*_qt;

public:
	Algo();
	~Algo();

	/**
	 * the initialyser of the class
	 *
	 * @param qt	=> 	the pointer of the quadtree
	 */
	void		init(QuadTree *qt);

	/**
	 * execute the algo
	 */
	void 		run();
};

#endif			//DISCRIMINATOR_ALGO_HH
