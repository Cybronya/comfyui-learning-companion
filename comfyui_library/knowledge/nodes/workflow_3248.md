# workflow>获取图像尺寸

## 节点类型

`workflow>获取图像尺寸`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `b:*`（1 次）
- `c:*`（1 次）
- `图像:IMAGE`（1 次）
- `SimpleMath+ c:*`（1 次）
- `SimpleMath+ b:*`（1 次）
- `SimpleMath+ 2 c:*`（1 次）
- `value:INT`（1 次）
- `SimpleMathInt+ value:INT`（1 次）
- `SimpleMath+ value:STRING`（1 次）
- `SimpleMath+ 2 value:STRING`（1 次）

## 输出

- `浮点:FLOAT`（1 次）
- `width:INT`（1 次）
- `SimpleMath+ 浮点:FLOAT`（1 次）
- `SimpleMath+ 5 浮点:FLOAT`（1 次）
- `结果:*`（1 次）
- `字符串:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1, "a+(a/2)", "a-b", "a/1024", ">", "raw value"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
