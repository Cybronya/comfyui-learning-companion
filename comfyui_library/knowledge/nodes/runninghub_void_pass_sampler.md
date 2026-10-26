# RunningHub Void Pass Sampler

## 节点类型

`RunningHub Void Pass Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipeline:RH_Void_PIPELINE`（2 次）
- `source:VIDEO`（2 次）
- `quadmask:VIDEO`（2 次）
- `prompt:STRING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `steps:INT`（2 次）
- `num_frames:INT`（2 次）
- `fps:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 784, 384, 30, 197, 12, 461920030042104, "randomize"]`（1 次）
- `["", 784, 384, 30, 85, 12, 600525610172329, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
