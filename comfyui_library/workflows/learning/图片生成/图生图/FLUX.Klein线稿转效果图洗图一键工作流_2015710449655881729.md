---
key: 图片生成/图生图/FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729.json
name: FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729.json
hash: acf5e92667c202cb
coverage: 0.888889
learned_at: 2026-10-23 10:54:16
nodes: [UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoader, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, ReferenceLatent, VAEDecode, SaveImage, KSampler, VAEEncode, LoadImage, KontextArchPresetMain, PreviewAny, Image Comparer (rgthree), Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 57207269969513, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `KontextArchPresetMain`
- `PreviewAny`
- `Image Comparer (rgthree)`
- `Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `57207269969513`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`CR Text Concatenate`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEDecode`、`SaveImage`、`KSampler`、`VAEEncode`、`LoadImage`、`KontextArchPresetMain`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
