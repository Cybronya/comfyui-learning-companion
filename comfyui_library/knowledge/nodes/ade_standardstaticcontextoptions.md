# ADE_StandardStaticContextOptions

## 节点类型

`ADE_StandardStaticContextOptions`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prev_context:CONTEXT_OPTIONS`（2 次）
- `view_opts:VIEW_OPTS`（2 次）
- `context_length:INT`（2 次）
- `context_overlap:INT`（2 次）
- `fuse_method:COMBO`（2 次）
- `use_on_equal_length:BOOLEAN`（2 次）
- `start_percent:FLOAT`（2 次）
- `guarantee_steps:INT`（2 次）

## 输出

- `CONTEXT_OPTS:CONTEXT_OPTIONS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, 4, "pyramid", false, 0, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
