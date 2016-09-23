//
// Created by kevin on 05/01/16.
//

#ifndef				DISCRIMINATOR_QUADTREE_HH
# define			DISCRIMINATOR_QUADTREE_HH

# include			<unistd.h>
# include			<vector>
# include			<utility>
# include			<iostream>

/**
 * this class is an implementation of a QuadTree based on the wikipedia article
 *
 * the class have position information directly inside it,
 * I use two coordinates, x and y,
 * the node is a square, so for the dim I divide it by 2,
 * with this I have just to add or sub the dim to x or y
 * to know the corner coordinate
 *
 * @param x		=> pos x for the center of the node
 * @param y		=> pos y for the center of the node
 * @param dim	=> half-size of the node
 * @param deep	=> deeps of the node
 */
class				QuadTree {
private:
	/**
	 * this enum contain the general information for the QuadTree
	 * MAX_QTS => number max of points per node
	 */
	enum INFO {
		MAX_QTS = 2
	};

	/**
	 * 3 first variables are use to specifies the boundary of the node
	 * x and y are the center of the area and dim is the half-size
	 *
	 * the 4' variable is the deep of the QuadTree
	 *
	 * the last one is the list of points who are in this area
	 */
	float 									_x;
	float 									_y;
	float 									_dim;
	int 									_deep;
	std::vector<std::pair<float, float> >	pts;

	/**
	 * this 4 following variables are the 4' next sections,
	 * which are limited by this area
	 */
	QuadTree		*ne;
	QuadTree		*nw;
	QuadTree		*se;
	QuadTree		*sw;

	/**
	 * this method is here to don't duplicate the code,
	 * it's a little generalisation of the way to check the node's validity
	 *
	 * @param node: node to visit
	 */
	bool 			visit(QuadTree *node);

	/**
	 * this variable is used to check if the node has already been subdivided
	 */
	bool 			firstSub;

	/**
	 * id to know in wich cloud is the point or collection of points
	 *
	 * -1 if not in any cloud
	 */
	int 			_id;

public:
	// x, y, dim, deep
	/**
	 * @param x		=>	center in x of the node
	 * @param y		=>	center in y of the node
	 * @param dim	=>	half-size o the node
	 * @param deep	=>	deeps oh the node
	 */
	QuadTree(float const &, float const &, float const&, int const &);
	~QuadTree();

	/**
	 * method to subdivide in 4 sections the current one
	 */
	void 			subdivide();

	/**
	 * method to know if the current section contain the point
	 *
	 * @param 1		=> position x
	 * @param 2		=> position y
	 */
	bool 			contain(float const&, float const &);
	bool 			contain(std::pair<float, float> const&);

	/**
	 * insert a point in this section or under
	 *
	 * @param 1		=> position x
	 * @param 2		=> position y
	 */
	bool 			insert(float const&, float const&);
	bool 			insert(std::pair<float, float> const&);

	/**
	 * main method to clean the tree,
	 * this method use "visit" to check information of the node
	 */
	bool			cleanTree();

	/**
	 * method use to count the number of node in the tree
	 */
	int 			countNode();

	void 			setId(int id);
	int 			getId();

	void 			aff(std::string str);
};

#endif				//DISCRIMINATOR_QUADTREE_HH
