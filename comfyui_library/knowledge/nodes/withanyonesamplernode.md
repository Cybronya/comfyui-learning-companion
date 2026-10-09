# WithAnyoneSamplerNode

## 节点类型

`WithAnyoneSamplerNode`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（3 次）
- `withAnyone_pipeline:WITHANYONE_PIPELINE`（3 次）
- `person1:PERSON_CONDITIONING`（3 次）
- `person2:PERSON_CONDITIONING`（3 次）
- `person3:PERSON_CONDITIONING`（3 次）
- `person4:PERSON_CONDITIONING`（3 次）
- `seed:INT`（3 次）
- `num_steps:INT`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）

## 输出

- `image:LATENT`（3 次）
- `debug_bbox_image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[48, "randomize", 25, 1024, 1024, 0.6000000000000001]`（1 次）
- `[414, "randomize", 25, 1024, 1024, 0.6500000000000001]`（1 次）
- `[1469, "randomize", 25, 1024, 1024, 0.6500000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
