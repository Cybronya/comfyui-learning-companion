# LLavaSamplerSimple

## 节点类型

`LLavaSamplerSimple`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `prompt:STRING`（4 次）
- `model:CUSTOM`（4 次）
- `temperature:FLOAT`（4 次）

## 输出

- `STRING:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.1]`（2 次）
- `[0.10000000000000002]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
