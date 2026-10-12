# RunningHub KiwiEdit Sampler

## 节点类型

`RunningHub KiwiEdit Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:RH_KiwiEdit_Pipeline`（1 次）
- `source_video:VIDEO`（1 次）
- `ref_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `max_num_frames:INT`（1 次）
- `num_inference_steps:INT`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Apply the dynamic aesthetic of abstract art to this video.", 81, 20, 715457606007997, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
