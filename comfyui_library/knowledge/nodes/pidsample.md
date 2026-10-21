# PiDSample

## 节点类型

`PiDSample`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `prepared:PID_PREP`（15 次）
- `pid_steps:INT`（15 次）
- `cfg_scale:FLOAT`（15 次）
- `seed:INT`（15 次）
- `aggressive_cleanup:BOOLEAN`（15 次）
- `sequential_offload:COMBO`（15 次）

## 输出

- `sampled:PID_SAMPLES`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 1, 1208772597, "fixed", true, "sequential_blocks_aggressive"]`（6 次）
- `[4, 1, 423924292, "randomize", true, "sequential_blocks_aggressive"]`（1 次）
- `[4, 1, 1285939353, "randomize", true, "sequential_blocks_aggressive"]`（1 次）
- `[4, 1, 1532528392, "randomize", true, "sequential_blocks_aggressive"]`（1 次）
- `[4, 1, 795374709, "randomize", true, "sequential_blocks_aggressive"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
