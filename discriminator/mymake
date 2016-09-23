NAME		= discriminator

CXX		=	g++

RM		=	rm -f

ALGO	=	src/algo

CORE	=	src/core

LOADER	=	src/loader

QUADTREE	=	src/core/quadtree

SRCS		=	src/main.cpp				\
				$(ALGO)/algo.cpp			\
				$(CORE)/core.cpp			\
				$(QUADTREE)/QuadTree.cpp	\
				$(LOADER)/mapLoader.cpp

OBJS		=	$(SRCS:%.cpp=%.o)

INCLUDE		=	-I $(ALGO) -I $(CORE) -I $(LOADER) -I $(QUADTREE)

CXXFLAGS		=	$(INCLUDE) -std=c++11

all		:	$(NAME)

$(NAME)		:	$(OBJS)
			$(CXX) $(OBJS) $(CXXFLAGS) -o $(NAME)

clean		:
			$(RM) $(OBJS)

fclean		:	clean
			$(RM) $(NAME)

re		:	fclean all

dbg		:	CXXFLAGS += -g
dbg		:	fclean re
