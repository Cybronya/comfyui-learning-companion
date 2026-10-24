# InsertAnythingLoader

## 节点类型

`InsertAnythingLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `lora_path:STRING`（1 次）
- `dtype:COMBO`（1 次）

## 输出

- `FLUX_FILL_MODEL:FLUX_FILL_MODEL`（14 次）
- `FLUX_REDUX_MODEL:FLUX_REDUX_MODEL`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bfloat16"]`（14 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
