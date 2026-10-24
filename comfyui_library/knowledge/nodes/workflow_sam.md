# workflow/sam

## 节点类型

`workflow/sam`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `detailer_hook:DETAILER_HOOK`（1 次）
- `SAMDetectorCombined image:IMAGE`（1 次）
- `图像:IMAGE`（1 次）

## 输出

- `SEGM_DETECTOR:SEGM_DETECTOR`（1 次）
- `MASK:MASK`（1 次）
- `图像:IMAGE`（1 次）
- `ImageResize+ 图像:IMAGE`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- ` 图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `MaskBlur+ 遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bbox/face_yolov8n_v2.pt", "sam_vit_b_01ec64.pth", "Prefer GPU", 0.5, 10, 25.200000000000003, 10, "all", "center-1", 0,`（1 次）
- `["GroundingDINO_SwinT_OGC (694MB)", "RealESRGAN_x2.pth", "sam_vit_b_01ec64.pth", "Prefer GPU", 1280, 1280, "nearest", "k`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
