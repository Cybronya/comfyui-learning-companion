# chx_Ksampler_Kontext_inpaint

## 节点类型

`chx_Ksampler_Kontext_inpaint`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `context:RUN_CONTEXT`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `pos:STRING`（1 次）

## 输出

- `context:RUN_CONTEXT`（1 次）
- `result_img:IMAGE`（1 次）
- `sample_img:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "fixed", 1, -1, 0, 0, 0.5, true, 512, 10, 0, "Bring black sunglasses"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
