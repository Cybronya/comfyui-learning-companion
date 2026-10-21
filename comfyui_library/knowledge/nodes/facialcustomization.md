# FacialCustomization

## 节点类型

`FacialCustomization`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `mode:COMBO`（4 次）
- `gender:COMBO`（4 次）
- `ftype:COMBO`（4 次）
- `age_group:COMBO`（4 次）
- `age_input:STRING`（4 次）
- `profession:COMBO`（4 次）
- `face:COMBO`（4 次）
- `makeup:COMBO`（4 次）
- `bone:COMBO`（4 次）
- `eye:COMBO`（4 次）

## 输出

- `prompt:STRING`（4 次）
- `negative:STRING`（4 次）
- `meta:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["整脸库", "女性", "非古风", "男子/女子 · 19–35 岁", "（随脸型自动生成）", "（随脸型自动生成）", "F025 · 27 岁 · 长椭圆脸 · 知性书卷", "（随脸型自动生成）", "（随脸型自动生成）",`（3 次）
- `["整脸库", "女性", "非古风", "不限", "（随脸型自动生成）", "（随脸型自动生成）", "F017 · 21 岁 · 长菱形脸 · 清瘦病娇", "（随脸型自动生成）", "（随脸型自动生成）", "（随脸型自动生成）",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
