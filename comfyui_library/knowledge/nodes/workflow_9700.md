# workflow>一键分离

## 节点类型

`workflow>一键分离`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩层:MASK`（1 次）
- `LayerUtility: ImageBlend layer_mask:MASK`（1 次）
- `LayerUtility: ImageBlend 2 layer_mask:MASK`（1 次）
- `图像4:IMAGE`（1 次）
- `图像5:IMAGE`（1 次）
- `图像6:IMAGE`（1 次）
- `panel_width:INT`（1 次）
- `panel_height:INT`（1 次）
- `fill_color:COMBO`（1 次）

## 输出

- `显示帮助:STRING`（1 次）
- `剩余遮罩:MASK`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[480, 1024, "white", "#000000", "sam_vit_h (2.56GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.3, 16, 0.15, 0.99, true, "hum`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
