# EditDetailerPipe

## 节点类型

`EditDetailerPipe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `detailer_pipe:DETAILER_PIPE`（4 次）
- `model:MODEL`（4 次）
- `clip:CLIP`（4 次）
- `vae:VAE`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `bbox_detector:BBOX_DETECTOR`（4 次）
- `sam_model:SAM_MODEL`（4 次）
- `segm_detector:SEGM_DETECTOR`（4 次）
- `detailer_hook:DETAILER_HOOK`（4 次）

## 输出

- `detailer_pipe:DETAILER_PIPE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[CONCAT] {eyes|eyes,detailed eyes}", "Select the LoRA to add to the text", "Select Wildcard 🟢 Full Cache"]`（1 次）
- `["[CONCAT] {face|face,detailed face}", "Select the LoRA to add to the text", "Select Wildcard 🟢 Full Cache"]`（1 次）
- `["[LAB]\n[ALL] nsfw\n[NIPPLES] nsfw, nipples\n[PUSSY] nsfw, pussy\n[ANUS] nsfw, (anus)\n[PENIS] nsfw, penis\n[TESTICLES]`（1 次）
- `["[CONCAT] hand, perfect hands", "Select the LoRA to add to the text", "Select Wildcard 🟢 Full Cache"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
