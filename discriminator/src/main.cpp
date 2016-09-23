//
// Created by kevin on 28/12/15.
//

#include	"core/core.hh"

int			main(int ac, char **av) {
	if (ac != 2)
		exit(84);
	core	c(av[1]);

	c.run();
	std::cout << c.getCloud() << std::endl;
	return (0);
}
