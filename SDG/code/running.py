import mnist_loader
import network
#import network2


training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

#net2 = network2.Network([784, 30,30,30, 10])

#net2.SGD(training_data, 10, 10, 0.1, lmbda=5.0,evaluation_data=validation_data, monitor_evaluation_accuracy=True)
