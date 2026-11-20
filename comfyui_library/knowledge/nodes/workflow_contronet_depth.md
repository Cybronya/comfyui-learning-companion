# workflow>ControNet Depth

## 节点类型

`workflow>ControNet Depth`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `vae:VAE`（1 次）

## 输出

- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lllyasviel_sd_control_collection/sai_xl_depth_256lora.safetensors", "DepthAnythingV2Preprocessor", 1024, 0.1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
