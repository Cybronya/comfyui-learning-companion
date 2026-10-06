# RH_DLSS5Enhance

## 节点类型

`RH_DLSS5Enhance`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `video:VIDEO`（3 次）
- `upscaling_mode:COMBO`（3 次）
- `style:COMBO`（3 次）
- `preset:INT`（3 次）
- `intensity:FLOAT`（3 次）
- `tone:FLOAT`（3 次）
- `structure:FLOAT`（3 次）
- `skin:FLOAT`（3 次）
- `auto_mask:COMBO`（3 次）

## 输出

- `images:IMAGE`（3 次）
- `video:VIDEO`（3 次）
- `status:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1x (DLAA / native)", "natural", 0, 1, 1, 1.5, -1, "on", "auto", 0.24, "still images", 0, "on", "auto", "auto", "off", `（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
