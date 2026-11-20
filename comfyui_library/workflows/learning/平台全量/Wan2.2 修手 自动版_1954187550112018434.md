---
key: 平台全量/Wan2.2 修手 自动版_1954187550112018434.json
name: Wan2.2 修手 自动版_1954187550112018434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 修手 自动版_1954187550112018434.json
hash: a7a0cfcbbb5fbff9
coverage: 0.769231
learned_at: 2026-11-14 01:05:41
nodes: [MaskPreview+, GrowMaskWithBlur, SetLatentNoiseMask, PreviewImage, VAEEncode, Anything Everywhere3, Image Comparer (rgthree), ConditioningZeroOut, VAEDecode, SaveImage, JjkText, LoadImage, CLIPTextEncode, ConstrainImage|pysssss, LayerMask: SegmentAnythingUltra V2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 647269727232695, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2 修手 自动版_1954187550112018434.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 修手 自动版_1954187550112018434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `MaskPreview+`
- `GrowMaskWithBlur`
- `SetLatentNoiseMask`
- `PreviewImage`
- `VAEEncode` ★核心
- `Anything Everywhere3`
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `JjkText`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ConstrainImage|pysssss`
- `LayerMask: SegmentAnythingUltra V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `647269727232695`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`MaskPreview+`、`GrowMaskWithBlur`、`SetLatentNoiseMask`、`VAEEncode`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`LoadImage`、`CLIPTextEncode`、`ConstrainImage|pysssss`、`LayerMask: SegmentAnythingUltra V2`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
