# RunningHubHeliosI2V

## 节点类型

`RunningHubHeliosI2V`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `helios_pipe:HELIOS_PIPE`（3 次）
- `image:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `num_frames:INT`（3 次）
- `num_inference_steps:INT`（3 次）
- `guidance_scale:FLOAT`（3 次）
- `seed:INT`（3 次）
- `is_enable_stage2:BOOLEAN`（3 次）

## 输出

- `video:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 384, 640, 251, 6, 1, 42, "fixed", true, "2,2,2", true, true, ""]`（2 次）
- `["女人在路上走路", 384, 640, 251, 50, 1, 3537581451, "randomize", true, "2,2,2", true, "ugly,"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
