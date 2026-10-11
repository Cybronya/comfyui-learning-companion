# ComfyBerniniDirector

## 节点类型

`ComfyBerniniDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_high:MODEL`（1 次）
- `model_low:MODEL`（1 次）
- `vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `task_type:COMBO`（1 次）
- `global_prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `bd_grp_high:BDGROUP`（1 次）
- `high_noise_cfg:FLOAT`（1 次）
- `high_noise_seed:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `fps:FLOAT`（1 次）
- `frame_count:INT`（1 次）
- `source_images:IMAGE`（1 次）
- `report:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["rv2v — 参考素材改视频", "", "bad video", "高噪采样设置", 1, 0, "randomize", "低噪采样设置", 1, 0, "randomize", 24, 832, 480, 848, 81, "{\`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
