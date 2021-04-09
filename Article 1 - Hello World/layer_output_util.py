
inputs = [] # the list of inputs from the previous layer
weights = [[], [], []] # nested list of weights for each node in the layer
biases = [] # biad for each node

layer_outputs = []

for neuron_weights, neuron_bias in zip(weights, biases):

	neuron_output = 0

	for neuron_input, weight in zip(inputs, neuron_weights):

		neuron_output += neuron_input*weight # output = w1*x1 + w2*x2 + w3*x3 ....

	neuron_output += neuron_bias # output = output + bias 

	layer_outputs.append(neuron_output)

print(layer_outputs)

