# PixaromaInpaintCrop

## 节点类型

`PixaromaInpaintCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `image:IMAGE`（12 次）
- `mask:MASK`（12 次）
- `size_mode:COMBO`（12 次）
- `target:INT`（12 次）
- `multiple:COMBO`（12 次）
- `context_px:INT`（12 次）
- `mask_grow:INT`（12 次）
- `mask_blur:INT`（12 次）
- `softness:INT`（12 次）
- `blend_mode:COMBO`（12 次）

## 输出

- `image:IMAGE`（12 次）
- `mask:MASK`（12 次）
- `crop_info:PIXAROMA_CROP_INFO`（12 次）
- `width:INT`（12 次）
- `height:INT`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["keep shape (long side)", 1024, 8, 24, 4, 96, 16, "mask", false, null, {"state_json": "{}"}]`（12 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
