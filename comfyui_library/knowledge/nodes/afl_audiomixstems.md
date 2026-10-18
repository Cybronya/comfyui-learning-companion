# AFL:AudioMixStems

## 节点类型

`AFL:AudioMixStems`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `stem_a:AUDIO`（3 次）
- `stem_b:AUDIO`（3 次）
- `stem_c:AUDIO`（3 次）
- `stem_d:AUDIO`（3 次）
- `gain_a:FLOAT`（3 次）
- `gain_b:FLOAT`（3 次）
- `gain_c:FLOAT`（3 次）
- `gain_d:FLOAT`（3 次）

## 输出

- `audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.0000000000000002, 1.0000000000000002, 1.0000000000000002, 1.0000000000000002]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
