# CheckpointLoaderSimpleShared //Inspire

## 节点类型

`CheckpointLoaderSimpleShared //Inspire`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `ckpt_name:COMBO`（2 次）
- `key_opt:STRING`（2 次）
- `mode:COMBO`（2 次）

## 输出

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `cache key:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["majicMIX realistic 麦橘写实_v7_250803.safetensors", "", "Auto"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
