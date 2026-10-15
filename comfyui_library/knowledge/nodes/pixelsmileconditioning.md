# PixelSmileConditioning

## 节点类型

`PixelSmileConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `conditioning_target:CONDITIONING`（6 次）
- `conditioning_neutral:CONDITIONING`（6 次）
- `score:FLOAT`（6 次）
- `method:COMBO`（6 次）

## 输出

- `CONDITIONING:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5000000000000001, "score_one (last 7 tokens)"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
