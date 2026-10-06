# DetailDaemonSamplerNode

## 节点类型

`DetailDaemonSamplerNode`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `sampler:SAMPLER`（8 次）
- `detail_amount:FLOAT`（8 次）
- `start:FLOAT`（8 次）
- `end:FLOAT`（8 次）
- `bias:FLOAT`（8 次）
- `exponent:FLOAT`（8 次）
- `start_offset:FLOAT`（8 次）
- `end_offset:FLOAT`（8 次）
- `fade:FLOAT`（8 次）
- `smooth:BOOLEAN`（8 次）

## 输出

- `SAMPLER:SAMPLER`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.1, 0.2, 0.8, 0.5, 1, 0, 0, 0, true, 0]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
