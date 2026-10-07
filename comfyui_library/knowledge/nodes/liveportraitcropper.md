# LivePortraitCropper

## 节点类型

`LivePortraitCropper`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:LIVEPORTRAITPIPE`（1 次）
- `cropper:LPCROPPER`（1 次）
- `source_image:IMAGE`（1 次）
- `dsize:INT`（1 次）
- `scale:FLOAT`（1 次）
- `vx_ratio:FLOAT`（1 次）
- `vy_ratio:FLOAT`（1 次）
- `face_index:INT`（1 次）
- `face_index_order:COMBO`（1 次）
- `rotate:BOOLEAN`（1 次）

## 输出

- `cropped_image:IMAGE`（1 次）
- `crop_info:CROPINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 2.3, 0, -0.125, 0, "large-small", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
