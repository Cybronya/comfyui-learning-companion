---
key: 平台全量/修手-wan2.2低噪-手动版_2009196228432633858.json
name: 修手-wan2.2低噪-手动版_2009196228432633858
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/修手-wan2.2低噪-手动版_2009196228432633858.json
hash: ea66e478ce1c48a1
coverage: 0.894737
learned_at: 2026-11-14 01:39:13
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, VAELoader, CLIPLoader, Image Comparer (rgthree), ConditioningZeroOut, SaveImage, VAEDecode, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, GrowMaskWithBlur, VAEEncode, MaskPreview+, SetLatentNoiseMask, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 33330563312477, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/修手-wan2.2低噪-手动版_2009196228432633858.json

> 来源文件 `comfyui_library/workflows/平台全量/修手-wan2.2低噪-手动版_2009196228432633858.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GrowMaskWithBlur`
- `VAEEncode` ★核心
- `MaskPreview+`
- `SetLatentNoiseMask`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `33330563312477`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPTextEncode`、`GrowMaskWithBlur`、`VAEEncode`、`MaskPreview+`、`SetLatentNoiseMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
