# MiniCPM_VQA

## 节点类型

`MiniCPM_VQA`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_video_path:PATH`（2 次）
- `source_image_path_1st:IMAGE`（2 次）
- `source_image_path_2nd:IMAGE`（2 次）
- `source_image_path_3rd:IMAGE`（2 次）
- `text:STRING`（1 次）

## 输出

- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Describe the image in detail", "MiniCPM-V-2_6-int4", false, 0.8, 100, 0.7, 1.05, 2048, 64, 2, 22, "randomize", true]`（1 次）
- `["", "MiniCPM-V-2_6-int4", true, 0.8, 100, 0.7, 1.05, 2048, 64, 2, 824, "randomize", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
