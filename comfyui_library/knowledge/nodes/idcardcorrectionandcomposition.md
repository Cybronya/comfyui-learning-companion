# IDCardCorrectionAndComposition

## 节点类型

`IDCardCorrectionAndComposition`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `front_image:IMAGE`（2 次）
- `front_mask:MASK`（2 次）
- `back_image:IMAGE`（2 次）
- `back_mask:MASK`（2 次）
- `画布宽_cm:FLOAT`（2 次）
- `画布高_cm:FLOAT`（2 次）
- `图像间距_cm:FLOAT`（2 次）
- `阴影大小:INT`（2 次）
- `阴影模糊:INT`（2 次）
- `阴影不透明度:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[21, 29.7, 2, 2, 2, 100, 110, 50, false, false, "仅供办理驾驶证业务使用", "苹方粗体.ttf", 100, "#808080", 38, 150, 30, "#ffffff"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
