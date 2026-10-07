# RunningHub_UNO_Sampler

## 节点类型

`RunningHub_UNO_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `uno_model:UNO_MODEL`（2 次）
- `uno_clip:UNO_CLIP`（2 次）
- `uno_vae:UNO_VAE`（2 次）
- `ref_images:IMAGE`（2 次）

## 输出

- `image_out:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A little boy singing on stage.      ", 1024, 1024, 4, 25, 373, "randomize", "d"]`（1 次）
- `["The panda is in the crystal ball", 1024, 1024, 4, 25, 1994, "randomize", "d"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
