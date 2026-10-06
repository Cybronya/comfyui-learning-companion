# RTXVideoSuperResolution

## 节点类型

`RTXVideoSuperResolution`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `resize_type:COMFY_DYNAMICCOMBO_V3`（3 次）
- `resize_type.scale:FLOAT`（3 次）
- `quality:COMBO`（3 次）

## 输出

- `upscaled_images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["scale by multiplier", 1.5000000000000002, "ULTRA"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
