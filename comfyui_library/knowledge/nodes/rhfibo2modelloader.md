# RHFibo2ModelLoader

## 节点类型

`RHFibo2ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `fibo2_name:COMBO`（9 次）
- `dtype:COMBO`（9 次）

## 输出

- `模型:MODEL`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["fibo2_edit_turbo_bf16.safetensors", "default"]`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
