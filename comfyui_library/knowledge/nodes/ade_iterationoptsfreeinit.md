# ADE_IterationOptsFreeInit

## 节点类型

`ADE_IterationOptsFreeInit`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `iterations:INT`（1 次）
- `filter:COMBO`（1 次）
- `d_s:FLOAT`（1 次）
- `d_t:FLOAT`（1 次）
- `n_butterworth:INT`（1 次）
- `sigma_step:INT`（1 次）
- `apply_to_1st_iter:BOOLEAN`（1 次）
- `init_type:COMBO`（1 次）
- `iter_batch_offset:INT`（1 次）
- `iter_seed_offset:INT`（1 次）

## 输出

- `ITERATION_OPTS:ITERATION_OPTS`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "gaussian", 0.25, 0.25, 4, 999, false, "FreeInit [sampler sigma]", 0, 1]`（7 次）
- `[1, "gaussian", 0.25, 0.25, 4, 999, false, "FreeInit [sampler sigma]", 0, 1, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
