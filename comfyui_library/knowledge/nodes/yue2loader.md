# YuE2Loader

## 节点类型

`YuE2Loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:COMBO`（2 次）
- `vae:COMBO`（2 次）
- `memory_budget_gib:FLOAT`（2 次）
- `quantization:COMBO`（2 次）
- `offload_ar:BOOLEAN`（2 次）
- `verify_hashes:BOOLEAN`（2 次）
- `keep_loaded:BOOLEAN`（2 次）

## 输出

- `pipe:YUE2_PIPE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["YuE2-3B", "YuE2-Vae", 24, "none", false, false, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
