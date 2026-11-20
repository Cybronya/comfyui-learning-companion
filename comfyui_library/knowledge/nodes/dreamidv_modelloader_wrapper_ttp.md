# DreamIDV_ModelLoader_Wrapper_TTP

## 节点类型

`DreamIDV_ModelLoader_Wrapper_TTP`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `dreamidv_model:COMBO`（1 次）
- `t5_checkpoint:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `attention_mode:COMBO`（1 次）

## 输出

- `dreamidv_wrapper:DREAMIDV_WRAPPER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dreamidv.pth", "umt5-xxl-enc-fp8_e4m3fn.safetensors", "bf16", "fp8_e4m3fn", "sageattn"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
