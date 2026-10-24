# HMImagePipelineLoader

## 节点类型

`HMImagePipelineLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输出

- `hm_image_pipeline:HMIMAGEPIPELINE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["菜里有毒_绘本故事：小公主的自我修养SD1.5_v2.0.safetensors", "[preset]BabyFaceV1", "same as checkpoint", "v5", "x1", "huggingface", 1, "`（2 次）
- `["toonyou_beta6.safetensors", "drawix10.safetensors", "same as checkpoint", "v5b", "x1", "huggingface", 1, "fp32"]`（1 次）
- `["cineroSD15Photomatic_cineroV14Handsome.safetensors", "None", "same as checkpoint", "v5", "x1", "huggingface", 1, "fp32`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
