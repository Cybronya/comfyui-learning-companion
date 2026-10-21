# OllamaOptionsV2

## 节点类型

`OllamaOptionsV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `enable_mirostat:BOOLEAN`（1 次）
- `mirostat:INT`（1 次）
- `enable_mirostat_eta:BOOLEAN`（1 次）
- `mirostat_eta:FLOAT`（1 次）
- `enable_mirostat_tau:BOOLEAN`（1 次）
- `mirostat_tau:FLOAT`（1 次）
- `enable_num_ctx:BOOLEAN`（1 次）
- `num_ctx:INT`（1 次）
- `enable_repeat_last_n:BOOLEAN`（1 次）
- `repeat_last_n:INT`（1 次）

## 输出

- `options:OLLAMA_OPTIONS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 0, false, 0.1, false, 5, false, 2048, false, 64, false, 1.1, false, 0.8, false, 485887208, "randomize", false, "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
