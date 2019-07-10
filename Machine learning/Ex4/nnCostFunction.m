function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m

%% Add row of ones for x0s to matrix X
X=[ones(size(X,1),1) X];

%% Convert y into matrix of K columns, m rows that signals output as 1, not output as 0
y_matrix=zeros(m, size(Theta2,1));
for i=1:m
y_matrix(i,y(i,:))=1;
end


%% Calculate h(x)=a3 with forward propagation
a2=sigmoid(X*Theta1');
a2=[ones(size(a2,1),1) a2];
a3=sigmoid(a2*Theta2'); %R= 5000 x 10 

%% Calculate Cost function with y_matrix and h(x)
K=size(y_matrix,2);
for i=1:K
J(i)=(1/m)*( - y_matrix(:,i)'*log(a3(:,i)) - (1-y_matrix(:,i))'*log(1-a3(:,i)));
end
% calculate regularization term
reg= (lambda/(2*m))*(sum(sum( Theta1(:,2:(size(Theta1,2) )) .* Theta1(:,2:(size(Theta1,2) )) )) + sum(sum( Theta2(:,2:(size(Theta2,2))) .* Theta2(:,2:(size(Theta2,2))) )));
J=sum(J)+reg;
%J=((-y'*log( sigmoid(z) ) - (1-y)'*log( 1- sigmoid(z)))/m)

%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%

%%initialize delta2, delta1
delta3 = zeros(m,K);
delta2 = zeros(m,size(Theta2,2));
delta1 = zeros(m,size(Theta1,2));

%% calculate errors from output side towards input side
for i=1:m
delta3(i,:)= a3(i,:) - y_matrix(i,:);
delta2(i,:)= (delta3(i,:) * Theta2).*a2(i,:).*(1-a2(i,:));
delta1(i,:)= (delta2(i,2:size(delta2,2)) * Theta1) .* X(i,:) .* (1-X(i,:)); 
end

%% calculate grads for each example of m separately and add them up. delta2 was dimension 1 x 26 but should be 1 x 25
for t=1:m
Theta1_grad = Theta1_grad + (1/m)* ( X(t,:) .* (delta2(t,2:size(delta2,2)))' );
Theta2_grad = Theta2_grad + (1/m)* (a2(t,:) .* delta3(t,:)' );
end




% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%


reg_grad1=(lambda/m) * Theta1(:,2:size(Theta1,2));
reg_grad2=(lambda/m) * Theta2(:,2:size(Theta2,2));

Theta1_grad = [Theta1_grad(:,1) Theta1_grad(:,2:size(Theta1_grad,2))+reg_grad1];
Theta2_grad = [Theta2_grad(:,1) Theta2_grad(:,2:size(Theta2_grad,2))+reg_grad2];

grad = [Theta1_grad(:) ; Theta2_grad(:)];











% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
