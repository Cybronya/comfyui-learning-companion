# IndexTTS2_ModelManager

## 节点类型

`IndexTTS2_ModelManager`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:STRING`（1 次）
- `config_path:STRING`（1 次）
- `model_dir:STRING`（1 次）
- `use_fp16:BOOLEAN`（1 次）
- `use_cuda_kernel:BOOLEAN`（1 次）
- `device:COMBO`（1 次）
- `cache_model:BOOLEAN`（1 次）
- `force_reload:BOOLEAN`（1 次）
- `memory_optimization:BOOLEAN`（1 次）
- `verbose:BOOLEAN`（1 次）

## 输出

- `model:INDEXTTS2_MODEL`（1 次）
- `model_info:STRING`（1 次）
- `model_stats:DICT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["IndexTTS2-Default", "auto", "auto", false, false, "auto", true, false, true, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
