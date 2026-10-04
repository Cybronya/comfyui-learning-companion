# Node Analysis Rules


# 1. Node Discovery


扫描来源：


## Built-in Nodes



nodes.py



## Custom Nodes



custom_nodes/



---


# 2. Node Information


每个节点记录：



- node_name
- class_type
- category
- inputs
- outputs
- package
- version



---


# 3. Node Category Rules



## Loader


包含：


- Load
- Loader
- Checkpoint
- Model


分类：


model_loading




---


## Sampling


包含：


- Sampler
- KSampler
- Scheduler


分类：


sampling




---


## Conditioning


包含：


- CLIP
- Prompt
- Conditioning


分类：


conditioning




---


## VAE


包含：


- VAE
- Encode
- Decode


分类：


vae




---


## Control


包含：


- ControlNet
- Adapter
- Pose
- Depth


分类：


control




---


## Video


包含：


- Video
- Animate
- Motion
- Wan
- LTX
- Hunyuan


分类：


video




---


# 4. Relationship Extraction


建立：


Node A

requires

Node B



例如：


KSampler

requires:

- CheckpointLoader
- CLIPTextEncode
- VAE




---


# 5. Human Knowledge


允许人工补充：


- description
- usage
- tips
- limitations
