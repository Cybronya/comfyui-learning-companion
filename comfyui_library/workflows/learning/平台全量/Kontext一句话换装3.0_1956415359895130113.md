---
key: 平台全量/Kontext一句话换装3.0_1956415359895130113.json
name: Kontext一句话换装3.0_1956415359895130113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext一句话换装3.0_1956415359895130113.json
hash: 32b2cdbaa800f654
coverage: 0.928571
learned_at: 2026-11-14 00:35:09
nodes: [FluxGuidance, ReferenceLatent, ConditioningZeroOut, DualCLIPLoader, VAELoader, UNETLoader, KSampler, CR SDXL Aspect Ratio, CLIPTextEncode, Image Comparer (rgthree), VAEDecode, SaveImage, easy imageSize, LoraLoaderModelOnly, LoadImage, LayerMask: SegmentAnythingUltra V2, CR Latent Input Switch, ImageConcatMulti, PreviewImage, LayerMask: SegmentAnythingUltra V2, LayerUtility: CropByMask V2, FluxKontextImageScale, VAEEncode, RH_Translator, LayerUtility: CropByMask V2, ImageConcatMulti, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 640952212513837, "steps": 20}
---

# 平台全量/Kontext一句话换装3.0_1956415359895130113.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext一句话换装3.0_1956415359895130113.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CR SDXL Aspect Ratio`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `easy imageSize`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `CR Latent Input Switch`
- `ImageConcatMulti`
- `PreviewImage`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: CropByMask V2`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `RH_Translator`
- `LayerUtility: CropByMask V2`
- `ImageConcatMulti`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `640952212513837`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`CR SDXL Aspect Ratio`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`easy imageSize`、`LoraLoaderModelOnly`、`LoadImage`、`LayerMask: SegmentAnythingUltra V2`、`CR Latent Input Switch`、`ImageConcatMulti`、`LayerUtility: CropByMask V2`、`FluxKontextImageScale`、`VAEEncode`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
