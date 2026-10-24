# RunningHub DreamOmni2 Editor

## 节点类型

`RunningHub DreamOmni2 Editor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipeline:RHDreamOmni2EditPipeline`（12 次）
- `src_image:IMAGE`（12 次）
- `ref_image:IMAGE`（12 次）
- `prompt:STRING`（12 次）
- `num_inference_steps:INT`（12 次）
- `guidance_scale:FLOAT`（12 次）
- `seed:INT`（12 次）

## 输出

- `image:IMAGE`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Make the person from the first image has the same pose as person from the second image.", 30, 3.5, 1108048937604224, "`（1 次）
- `["Make the woman from the second image stand on the road in the first image.", 30, 3.5, 421192453286698, "randomize"]`（1 次）
- `["make the firest image has the same light condition as the second image", 30, 3.5, 863029795854972, "randomize"]`（1 次）
- `["make the first image have the same image style as the second image", 30, 3.5, 654281769865547, "randomize"]`（1 次）
- `["make the first image have the same image style as the second image", 30, 3.5, 747296120153533, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
