# RunningHub Mammothmoda T2I Sampler

## 节点类型

`RunningHub Mammothmoda T2I Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:RHMammothmoda`（2 次）
- `prompt:STRING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `num_inference_steps:INT`（2 次）
- `cfg_scale:FLOAT`（2 次）
- `text_guidance_scale:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1 girl", 1280, 720, 50, 7, 9, 973062618661005, "randomize"]`（1 次）
- `["1 girl", 1280, 720, 50, 7, 9, 126051501953268, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
