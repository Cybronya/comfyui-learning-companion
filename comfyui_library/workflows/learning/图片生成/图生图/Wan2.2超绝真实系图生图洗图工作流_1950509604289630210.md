---
key: 图片生成/图生图/Wan2.2超绝真实系图生图洗图工作流_1950509604289630210.json
name: Wan2.2超绝真实系图生图洗图工作流_1950509604289630210
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2超绝真实系图生图洗图工作流_1950509604289630210.json
hash: e9c9b483b853d83f
coverage: 0.966667
learned_at: 2026-10-23 11:28:25
nodes: [Note, PathchSageAttentionKJ, CLIPLoader, CLIPTextEncode, ModelSamplingSD3, VAEEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, Bjornulf_TextToStringAndSeed, VAELoader, VAEDecode, PDIMAGE_LongerSize, VAEDecode, SaveImage, SaveImage, KSampler, KSampler, SaveImage, LoadImage, PMRF, SaveImage, PDIMAGE_LongerSize, ImageConcanate]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 497163970725457, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2超绝真实系图生图洗图工作流_1950509604289630210.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2超绝真实系图生图洗图工作流_1950509604289630210.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Note`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Bjornulf_TextToStringAndSeed`
- `VAELoader`
- `VAEDecode` ★核心
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `PMRF`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `ImageConcanate`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`Bjornulf_TextToStringAndSeed`、`VAELoader`、`VAEDecode`、`PDIMAGE_LongerSize`、`SaveImage`、`KSampler`、`LoadImage`、`PMRF`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
