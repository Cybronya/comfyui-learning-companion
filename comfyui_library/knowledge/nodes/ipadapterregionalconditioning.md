# IPAdapterRegionalConditioning

## 节点类型

`IPAdapterRegionalConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）

## 输出

- `IPADAPTER_PARAMS:IPADAPTER_PARAMS`（3 次）
- `POSITIVE:CONDITIONING`（3 次）
- `NEGATIVE:CONDITIONING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.7000000000000001, 1, "linear", 0, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
