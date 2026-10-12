# RealRestorerLoadPipeline

## 节点类型

`RealRestorerLoadPipeline`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `torch_dtype:COMBO`（1 次）
- `force_reload:BOOLEAN`（1 次）
- `model_subfolder:STRING`（1 次）

## 输出

- `pipeline:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["fp8_e4m3fn (transformer only)", false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
