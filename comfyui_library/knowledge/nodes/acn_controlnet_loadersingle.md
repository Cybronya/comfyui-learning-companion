# ACN_ControlNet++LoaderSingle

## 节点类型

`ACN_ControlNet++LoaderSingle`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输出

- `CONTROL_NET:CONTROL_NET`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["controlnet-union-sdxl-1.0_promax.safetensors", "openpose"]`（1 次）
- `["controlnet-union-sdxl-1.0_promax.safetensors", "tile"]`（1 次）
- `["controlnet-union-sdxl-1.0_promax.safetensors", "depth"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
