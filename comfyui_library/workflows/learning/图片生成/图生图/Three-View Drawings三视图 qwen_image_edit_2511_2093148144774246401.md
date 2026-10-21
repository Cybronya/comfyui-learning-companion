---
key: 图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json
name: Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json
hash: 765bef972bab34b2
coverage: 1
learned_at: 2026-10-21 00:44:37
nodes: [ModelSamplingAuraFlow, UNETLoader, CLIPLoader, CFGNorm, VAEDecode, ConditioningZeroOut, ReferenceLatent, VAELoader, LoraLoaderModelOnly, VAEDecode, VAEEncode, VAEDecode, KSampler, KSampler, KSampler, FluxKontextImageScale, SaveImage, SaveImage, TextEncodeQwenImageEditPlus, EmptyLatentImage, LoraLoaderModelOnly, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 867058727936570, "steps": 4, "width": 1440}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CFGNorm`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `FluxKontextImageScale`
- `SaveImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `867058727936570`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1440`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPLoader`、`CFGNorm`、`VAEDecode`、`ConditioningZeroOut`、`ReferenceLatent`、`VAELoader`、`LoraLoaderModelOnly`、`VAEEncode`、`KSampler`、`FluxKontextImageScale`、`SaveImage`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
