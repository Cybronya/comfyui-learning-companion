# Audio Add Silence

## 节点类型

`Audio Add Silence`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `audio:AUDIO`（8 次）
- `prepend_silence:FLOAT`（8 次）
- `append_silence:FLOAT`（8 次）

## 输出

- `audio:AUDIO`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 5000]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
