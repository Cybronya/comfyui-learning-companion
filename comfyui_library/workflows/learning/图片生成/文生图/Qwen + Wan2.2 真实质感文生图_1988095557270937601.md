---
key: 图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json
name: Qwen + Wan2.2 真实质感文生图_1988095557270937601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json
hash: 25ae115137092395
coverage: 0.906977
learned_at: 2026-10-15 22:26:56
nodes: [CLIPLoader, VAELoader, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, VAEEncode, VAELoader, KSampler, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, PrimitiveStringMultiline, VAEEncode, VAELoader, VAEDecode, CLIPTextEncode, CLIPTextEncode, VAEDecode, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, LoraLoaderModelOnly, UNETLoader, UpscaleModelLoader, ImageUpscaleWithModel, CR SDXL Aspect Ratio, KSampler, ImageScaleBy, SaveImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, LoraLoaderModelOnly, TextInputBasic, LoraLoaderModelOnly, KSampler, SaveImage, VAEDecode, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 230262900321590, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `VAEEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `CR SDXL Aspect Ratio`
- `KSampler` ★核心
- `ImageScaleBy`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `TextInputBasic`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`

## 关键参数

- `seed` = `230262900321590`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`KSampler`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`ModelSamplingAuraFlow`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`CR SDXL Aspect Ratio`、`ImageScaleBy`、`SaveImage`、`TextInputBasic`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
