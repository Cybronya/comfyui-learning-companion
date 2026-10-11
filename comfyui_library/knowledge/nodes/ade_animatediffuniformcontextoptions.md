# ADE_AnimateDiffUniformContextOptions

## 节点类型

`ADE_AnimateDiffUniformContextOptions`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `prev_context:CONTEXT_OPTIONS`（3 次）
- `view_opts:VIEW_OPTS`（3 次）
- `deprecation_warning:ADEWARN`（1 次）

## 输出

- `CONTEXT_OPTIONS:CONTEXT_OPTIONS`（2 次）
- `CONTEXT_OPTS:CONTEXT_OPTIONS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, 1, 4, "uniform", false, "flat", false, 0, 1]`（2 次）
- `[16, 1, 4, "uniform", false, "flat", false, 0, 1, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
