# LayeredControlV2Sampler

## 节点类型

`LayeredControlV2Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `pipe:LayeredControlV2Pipe`（6 次）
- `layer_input_image:IMAGE`（6 次）
- `mask_image:IMAGE`（6 次）
- `prompt:STRING`（6 次）
- `width:INT`（6 次）
- `height:INT`（6 次）
- `num_inference_steps:INT`（6 次）
- `cfg_scale:FLOAT`（6 次）
- `seed:INT`（6 次）
- `mode:COMBO`（6 次）

## 输出

- `layer_0:IMAGE`（6 次）
- `layer_1:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Text 'RH'", 1024, 1024, 10, 4, 964, "randomize", "prompt_guided"]`（1 次）
- `["", 1024, 1024, 10, 1, 1275, "randomize", "mask_guided"]`（1 次）
- `["", 1024, 1024, 10, 1, 752, "randomize", "mask_guided"]`（1 次）
- `["", 1024, 1024, 10, 1, 672, "randomize", "mask_guided"]`（1 次）
- `["Text 'RH'", 1024, 1024, 10, 4, 60, "randomize", "prompt_guided"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
