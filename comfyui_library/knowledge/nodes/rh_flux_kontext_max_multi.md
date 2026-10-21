# RH_Flux_Kontext_Max_Multi

## 节点类型

`RH_Flux_Kontext_Max_Multi`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `guidance_scale:FLOAT`（2 次）
- `aspect_ratio:COMBO`（2 次）

## 输出

- `image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 3.5, "1:1"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
