# Qwen2_5_VL_Run_Advanced

## 节点类型

`Qwen2_5_VL_Run_Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `Qwen2_5_VL_model:QWEN2_5_VL_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `video:VIDEO`（1 次）
- `BatchImage:BatchImage`（1 次）
- `system_text:STRING`（1 次）
- `text:STRING`（1 次）
- `video_decode_method:COMBO`（1 次）
- `max_new_tokens:INT`（1 次）
- `min_pixels:INT`（1 次）
- `max_pixels:INT`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你是一个优秀的人工智能助手，给我反推这张图片的中文提示词，要包含“主要元素”，“构图/视角”，“风格定位”，“色彩/光影”，“景深”，“文字”，以及文字所在的位置等详细内容", "", "torchvision", 1000, 256,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
