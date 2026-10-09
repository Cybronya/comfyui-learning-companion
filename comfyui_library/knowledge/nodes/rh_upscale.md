# RH_Upscale

## 节点类型

`RH_Upscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `视频:VIDEO`（4 次）
- `模型:COMBO`（4 次）
- `分辨率:COMBO`（4 次）

## 输出

- `视频:VIDEO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["High", "4K"]`（3 次）
- `["Max", "4K"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
