---
key: 图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json
name: Qwen + Wan2.2 真实质感文生图_1988095557270937601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json
hash: 25ae115137092395
coverage: 0.883721
learned_at: 2026-10-10 20:58:50
nodes: [CLIPLoader, VAELoader, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, VAEEncode, VAELoader, KSampler, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, PrimitiveStringMultiline, VAEEncode, VAELoader, VAEDecode, CLIPTextEncode, CLIPTextEncode, VAEDecode, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, LoraLoaderModelOnly, UNETLoader, UpscaleModelLoader, ImageUpscaleWithModel, CR SDXL Aspect Ratio, KSampler, ImageScaleBy, SaveImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, LoraLoaderModelOnly, TextInputBasic, LoraLoaderModelOnly, KSampler, SaveImage, VAEDecode, PreviewImage]
patterns: []
missing: [CR SDXL Aspect Ratio]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 230262900321590, "steps": 10}
discoveries: [次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen + Wan2.2 真实质感文生图_1988095557270937601.json`

## 结构

**节点**（43 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `DualCLIPLoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode`
- `VAELoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `VAEEncode`
- `VAELoader`
- `VAEDecode`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ImageScaleBy`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly`
- `TextInputBasic`
- `LoraLoaderModelOnly`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `PreviewImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.3500000000000001`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `230262900321590`
- `steps` = `10`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`KSampler`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`PrimitiveStringMultiline`、`VAEDecode`、`ModelSamplingAuraFlow`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`CR SDXL Aspect Ratio`、`ImageScaleBy`、`SaveImage`、`Fast Groups Bypasser (rgthree)`、`TextInputBasic`

**缺卡**（1）：`CR SDXL Aspect Ratio`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
