# IDM-VTON

## 节点类型

`IDM-VTON`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipeline:PIPELINE`（2 次）
- `human_img:IMAGE`（2 次）
- `pose_img:IMAGE`（2 次）
- `mask_img:IMAGE`（2 次）
- `garment_img:IMAGE`（2 次）
- `garment_description:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `num_inference_steps:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 768, 1024, 30, 2, 1, 355233080502087, "fixed"]`（1 次）
- `["Best quality, masterpiece, high-definition, 8k", "monochrome, lowres, bad anatomy, worst quality, low quality", 768, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
