# RunningHub HunyuanTo3D Text

## 节点类型

`RunningHub HunyuanTo3D Text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `prompt:STRING`（3 次）
- `EnablePBR:BOOLEAN`（3 次）
- `seed:INT`（3 次）

## 输出

- `Preview:IMAGE`（3 次）
- `Download Url:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一件黄色衬衣，上面有猪猪的卡通图案", false, 1027019329610452, "randomize"]`（1 次）
- `["一件黄色衬衣，上面有猪猪的卡通图案", false, 145013355445668, "randomize"]`（1 次）
- `["一只穿着黄色衬衣的卡通猪猪", true, 235002471536166, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
