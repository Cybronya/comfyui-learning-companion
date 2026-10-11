# RH_MagiHumanModelLoader

## 节点类型

`RH_MagiHumanModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model_type:COMBO`（3 次）
- `use_turbo_vae:BOOLEAN`（3 次）
- `vram_mode:COMBO`（3 次）
- `sr_model:COMBO`（3 次）
- `torch_compile:BOOLEAN`（2 次）

## 输出

- `pipeline:MAGIHUMAN_PIPELINE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["distill", true, "mid_vram", "540p_sr", false]`（2 次）
- `["distill", true, "low_vram", "540p_sr"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
