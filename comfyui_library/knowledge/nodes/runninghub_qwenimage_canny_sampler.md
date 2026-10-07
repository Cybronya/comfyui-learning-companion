# RunningHub QwenImage Canny Sampler

## 节点类型

`RunningHub QwenImage Canny Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `canny_image:IMAGE`（2 次）
- `pipeline:RHQwenCannyPipeline`（2 次）
- `prompt:STRING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `num_inference_steps:INT`（2 次）
- `seed:INT`（2 次）
- `ref_image:IMAGE`（1 次）
- `control_type:COMBO`（1 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["女人，下面写着六六大顺", 512, 768, 20, 19993863880209, "randomize"]`（1 次）
- `["一只小猫，毛发光洁柔顺，眼神灵动，背景是樱花纷飞的春日庭院，唯美温馨。", 1024, 1024, 20, 863113286623394, "randomize", "canny"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
