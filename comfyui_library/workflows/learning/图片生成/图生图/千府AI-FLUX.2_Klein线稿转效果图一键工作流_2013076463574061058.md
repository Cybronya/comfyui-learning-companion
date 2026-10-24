---
key: 图片生成/图生图/千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058.json
name: 千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058.json
hash: 10d6bf89f42056b1
coverage: 0.9375
learned_at: 2026-10-23 12:28:32
nodes: [Image Comparer (rgthree), ConditioningZeroOut, ReferenceLatent, VAEEncode, VAELoader, ModelPatchTorchSettings, SaveImage, VAEDecode, UNETLoader, PathchSageAttentionKJ, KSampler, CLIPTextEncode, CLIPLoader, LoraLoaderModelOnly, LoadImage, JsonPromptNode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 771157998328483, "steps": 25}
---

# 图片生成/图生图/千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `ModelPatchTorchSettings`
- `SaveImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `JsonPromptNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `771157998328483`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`ModelPatchTorchSettings`、`SaveImage`、`VAEDecode`、`UNETLoader`、`PathchSageAttentionKJ`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`、`JsonPromptNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
