# IF_MemoCheckpointLoader

## 节点类型

`IF_MemoCheckpointLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输出

- `reference_net:MODEL`（1 次）
- `diffusion_net:MODEL`（1 次）
- `vae:VAE`（1 次）
- `image_proj:IMAGE_PROJ`（1 次）
- `audio_proj:AUDIO_PROJ`（1 次）
- `emotion_classifier:EMOTION_CLASSIFIER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["memoavatar/memo"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
