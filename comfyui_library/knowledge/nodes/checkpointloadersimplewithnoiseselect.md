# CheckpointLoaderSimpleWithNoiseSelect

## 节点类型

`CheckpointLoaderSimpleWithNoiseSelect`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输出

- `MODEL:MODEL`（4 次）
- `CLIP:CLIP`（4 次）
- `VAE:VAE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["majicMIX realistic 麦橘写实_v7.safetensors", "avg(sqrt_linear,linear)", false, 0.18216000000000002]`（1 次）
- `["majicmixRealistic_v7.safetensors", "avg(sqrt_linear,linear)", false, 0.18216000000000002]`（1 次）
- `["majicMIX realistic 麦橘写实_v7.safetensors", "sqrt_linear (AnimateDiff)", false, 0.18000000000000005]`（1 次）
- `["极氪摄影PRO-V8纯净质感_极氪摄影PRO-V8纯净质感.safetensors", "avg(sqrt_linear,linear)", false, 0.18216000000000002]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
