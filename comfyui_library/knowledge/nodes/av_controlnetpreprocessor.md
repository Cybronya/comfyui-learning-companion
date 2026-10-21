# AV_ControlNetPreprocessor

## 节点类型

`AV_ControlNetPreprocessor`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `preprocessor:COMBO`（1 次）
- `sd_version:COMBO`（1 次）
- `resolution:INT`（1 次）
- `preprocessor_override:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `CNET_NAME:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["scribble", "sdxl", 768, "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
