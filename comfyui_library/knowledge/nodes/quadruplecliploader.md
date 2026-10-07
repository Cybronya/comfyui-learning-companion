# QuadrupleCLIPLoader

## 节点类型

`QuadrupleCLIPLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `CLIP:CLIP`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["clip_l_hidream.safetensors", "clip_g_hidream.safetensors", "t5xxl_fp8_e4m3fn_scaled.safetensors", "llama_3.1_8b_instru`（1 次）
- `["clip_l_hidream.safetensors", "clip_g_hidream.safetensors", "t5xxl_fp8_e4m3fn.safetensors", "llama_3.1_8b_instruct_fp8_`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
