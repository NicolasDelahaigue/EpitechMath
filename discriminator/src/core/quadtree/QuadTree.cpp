//
// Created by kevin on 05/01/16.
//

#include 			<string>
#include			"QuadTree.hh"

QuadTree::QuadTree(float const &x,
				   float const &y,
				   float const &dim,
				   int const& deep = 0)
{
	this->_x = x;
	this->_y = y;
	this->_dim = dim;
	this->_deep = deep;

//	std::cout	<< "QuadTree construction:"	<< std::endl
//				<< "\tx	=> "	<< x		<< std::endl
//				<< "\ty	=> "	<< y		<< std::endl
//				<< "\tdim	=> "	<< dim		<< std::endl
//				<< "\tdeep	=> "	<< deep		<< std::endl
//				<< std::endl;

	this->ne = NULL;
	this->nw = NULL;
	this->se = NULL;
	this->sw = NULL;

	this->firstSub = false;

	this->_id = -1;
}

QuadTree::~QuadTree() {
	delete this->ne;
	delete this->nw;
	delete this->se;
	delete this->sw;
}

void				QuadTree::subdivide() {
//	std::cout << "subdivide: " << this->_deep + 1 << std::endl;

	this->ne = new QuadTree(this->_x + this->_dim / 2,
							this->_y + this->_dim / 2,
							this->_dim / 2,
							this->_deep + 1);

	this->nw = new QuadTree(this->_x - this->_dim / 2,
							this->_y + this->_dim / 2,
							this->_dim / 2,
							this->_deep + 1);

	this->se = new QuadTree(this->_x + this->_dim / 2,
							this->_y - this->_dim / 2,
							this->_dim / 2,
							this->_deep + 1);

	this->sw = new QuadTree(this->_x - this->_dim / 2,
							this->_y - this->_dim / 2,
							this->_dim / 2,
							this->_deep + 1);
}

bool				QuadTree::contain(const float &x, const float &y) {

//	std::cout	<< this->_deep << "\t"
//				<< x << ";" << y
//				<< " in ("
//				<< this->_x - this->_dim << ";" << this->_x + this->_dim
//				<< ", "
//				<< this->_y - this->_dim << ";" << this->_y + this->_dim << ")"
//				<< std::endl;

	return ((x >= this->_x - this->_dim && x <= this->_x + this->_dim)
			&& (y >= this->_y - this->_dim && y <= this->_y + this->_dim));
}

bool				QuadTree::insert(const float &x, const float &y) {
	if (!this->contain(x, y)) {
		return false;
	}

	this->pts.push_back(std::make_pair(x, y));

	if (this->pts.size() > MAX_QTS) {
		if (!this->firstSub) {							// check if it's the first subdivide
			this->subdivide();
			for (auto i : this->pts) {					// insert father's points in it childs
				if (this->ne->insert(i) || this->nw->insert(i) || this->se->insert(i) || this->sw->insert(i));
			}
			this->firstSub = true;
		} else {
			ne->insert(x, y);
			nw->insert(x, y);
			se->insert(x, y);
			sw->insert(x, y);
		}
	}
	return true;
}

bool				QuadTree::contain(const std::pair<float, float> &pt)	{ return this->contain(pt.first, pt.second); }
bool				QuadTree::insert(const std::pair<float, float> &pt)		{ return this->insert(pt.first, pt.second); }
void				QuadTree::setId(int id)									{ this->_id = id; }
int					QuadTree::getId()										{ return this->_id; }


bool				QuadTree::cleanTree() {
	if (!this->visit(this->ne))
		this->ne = NULL;
	if (!this->visit(this->nw))
		this->nw = NULL;
	if (!this->visit(this->se))
		this->se = NULL;
	if (!this->visit(this->sw))
		this->sw = NULL;

	return this->pts.empty();
}

/**
 * private method
 */

bool 				QuadTree::visit(QuadTree *node) {
	if (node != NULL) {
		if (node->cleanTree()) {
			delete node;
			return false;
		}
	}
	return true;
}

int					QuadTree::countNode() {
	int 			i = 0;

	if (this->ne != NULL)
		i += this->ne->countNode() + 1;
	if (this->nw != NULL)
		i += this->nw->countNode() + 1;
	if (this->se != NULL)
		i += this->se->countNode() + 1;
	if (this->sw != NULL)
		i += this->sw->countNode() + 1;
	return i;
}

void 				QuadTree::aff(std::string str) {
	if (this->ne != NULL)
		this->ne->aff(str + "ne>");
	if (this->nw != NULL)
		this->nw->aff(str + "nw>");
	if (this->se != NULL)
		this->se->aff(str + "se>");
	if (this->sw != NULL)
		this->sw->aff(str + "sw>"); 
	std::cout << str;
	if (this->ne == NULL && this->nw == NULL && this->se == NULL && this->sw == NULL)
	{
		std::cout << "\033[34m";
	}
	std::cout << this->pts.size() << "\033[0m" << std::endl;
}
