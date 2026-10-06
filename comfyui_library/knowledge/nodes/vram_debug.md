# VRAM_Debug

## 节点类型

`VRAM_Debug`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `any_input:*`（3 次）
- `image_pass:IMAGE`（3 次）
- `model_pass:MODEL`（3 次）
- `empty_cache:BOOLEAN`（3 次）
- `gc_collect:BOOLEAN`（3 次）
- `unload_all_models:BOOLEAN`（3 次）

## 输出

- `any_output:*`（3 次）
- `image_pass:IMAGE`（3 次）
- `model_pass:MODEL`（3 次）
- `freemem_before:INT`（3 次）
- `freemem_after:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
