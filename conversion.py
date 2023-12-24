import tensorflow as tf
import onnx

# Load the TensorFlow model
tf_model_path = "mobilenet_tf.pb"
tf_graph = tf.Graph()
with tf_graph.as_default():
    tf_sess = tf.compat.v1.Session()
    with tf.io.gfile.GFile(tf_model_path, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

# Convert the TensorFlow model to ONNX
onnx_model_path = "mobilenet_v2_float.onnx"
onnx_graph = tf_graph.as_graph_def().SerializeToString()
onnx_model = onnx.load_from_string(onnx_graph)
onnx.save_model(onnx_model, onnx_model_path)


"""
import torch
import torch.onnx
dummy_input = torch.randn(1, 3, 224, 224)  #input shape

onnx_file_path = "my_model.onnx"
torch.onnx.export(my_model, dummy_input, onnx_file_path, verbose=True)

"""