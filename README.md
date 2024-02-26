# FlipPharma
FlipPharma - a solution to evaluate placement of your products quick and fast

Our proposed solution involves a 2 point approach. Based on the placement of the product on the shelf, we allocate a rating to it. Secondly, we suggest some small improvements to enhance the rating of the placed product. The score is based on 3 features currently, The lighting of the area, the visibility of the area, how many competitive products are placed in the vicinity of the product. The model takes in all 3 of the features and then determines how good the placement of a certain product is. 

For the visibility feature, we calculate hot and cold zones based on whether the product is placed at eye-level, how less accessible is the product, etc. The products in the centre of the shelf and those to the left are given a higher rating as general viewing is from left to right.
