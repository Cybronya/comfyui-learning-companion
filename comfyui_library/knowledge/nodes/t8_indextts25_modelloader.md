# T8_IndexTTS25_ModelLoader

## 节点类型

`T8_IndexTTS25_ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `acceleration_mode:COMBO`（1 次）
- `use_cuda_kernel:BOOLEAN`（1 次）
- `release_after_run:BOOLEAN`（1 次）
- `recycle_after_runs:INT`（1 次）
- `verify_hashes:BOOLEAN`（1 次）
- `reference_device:COMBO`（1 次）
- `reuse_spk_cond_for_emo:BOOLEAN`（1 次）

## 输出

- `IndexTTS 2.5 模型:T8_INDEXTTS25_MODEL`（1 次）
- `模型信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["IndexTTS-2.5", "cuda:0", "float32", "bigvgan_cuda", false, false, 0, false, "same", false, true, false, false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
