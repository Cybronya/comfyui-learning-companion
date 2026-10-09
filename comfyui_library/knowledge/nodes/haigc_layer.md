# HAIGC_Layer

## 节点类型

`HAIGC_Layer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `每批合成方式:COMBO`（1 次）
- `不透明度:INT`（1 次）
- `混合模式:COMBO`（1 次）
- `排版方式:COMBO`（1 次）
- `间距:INT`（1 次）
- `间距颜色:STRING`（1 次）
- `匹配上一层大小:BOOLEAN`（1 次）

## 输出

- `图层数据:PSD_LAYERS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["所有单元合成", 100, "正常", "叠加", 0, "#FFFFFF", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
