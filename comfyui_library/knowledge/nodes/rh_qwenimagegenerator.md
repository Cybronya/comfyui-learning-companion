# RH_QwenImageGenerator

## 节点类型

`RH_QwenImageGenerator`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:QWEN_PIPELINE`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `num_inference_steps:INT`（1 次）
- `true_cfg_scale:FLOAT`（1 次）
- `seed:INT`（1 次）
- `language:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `negative_prompt:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["夜晚的麦田在星空中延展，天空中布满旋转的黄色、蓝色星云，像梵高的《星月夜》一样充满流动感，麦田里有几棵扭曲的树木，远处有一座小小的农舍，整体色彩浓烈，笔触奔放，保留油画的肌理感，画面充满生命力。", 1664, 928, 20, 4, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
