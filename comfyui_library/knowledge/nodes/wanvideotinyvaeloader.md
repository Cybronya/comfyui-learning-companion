# WanVideoTinyVAELoader

## 节点类型

`WanVideoTinyVAELoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_name:COMBO`（2 次）
- `precision:COMBO`（2 次）
- `parallel:BOOLEAN`（2 次）

## 输出

- `vae:WANVAE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["taew2_1.safetensors", "fp16", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
