# ClipInterrogator

## 节点类型

`ClipInterrogator`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）

## 输出

- `prompt:STRING`（2 次）
- `random_samples:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["fast", "off", "a bird perched on a branch in the middle of a lake, irish mountains background, nature and clouds in ba`（1 次）
- `["fast", "off", "a beach with a pink sky and white clouds, beach aesthetic, pastelwave, vaporwave surreal ocean, vaporwa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
