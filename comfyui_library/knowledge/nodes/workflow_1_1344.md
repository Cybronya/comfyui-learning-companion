# workflow>节点1

## 节点类型

`workflow>节点1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `ImageRemoveBackground+ image:IMAGE`（1 次）
- `video_frames:IMAGE`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- ` 图像:IMAGE`（1 次）
- `GroundingDinoSAMSegment (segment anything) 遮罩:MASK`（1 次）
- `MaskToImage 图像:IMAGE`（1 次）
- `foreground_frames:IMAGE`（1 次）
- `alpha_frames:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["GroundingDINO_SwinT_OGC (694MB)", "base-nightly", true, "sam_vit_h (2.56GB)", "0", "character", 0.3, 10, 10, 10, 255, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
