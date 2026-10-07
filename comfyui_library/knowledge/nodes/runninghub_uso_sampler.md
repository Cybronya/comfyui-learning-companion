# RunningHub USO Sampler

## 节点类型

`RunningHub USO Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `uso:RHUSOMudules`（1 次）
- `content_image:IMAGE`（1 次）
- `style_image:IMAGE`（1 次）
- `style2_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `num_inference_steps:INT`（1 次）
- `guidance:FLOAT`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a cute anime girl ", 1024, 1024, 25, 4, 681165972496256, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
