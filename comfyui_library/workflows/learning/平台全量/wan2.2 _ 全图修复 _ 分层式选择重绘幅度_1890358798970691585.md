---
key: 平台全量/wan2.2 _ 全图修复 _ 分层式选择重绘幅度_1890358798970691585.json
name: wan2.2 _ 全图修复 _ 分层式选择重绘幅度_1890358798970691585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 _ 全图修复 _ 分层式选择重绘幅度_1890358798970691585.json
hash: 9d9a1997b19c0fb6
coverage: 0.956522
learned_at: 2026-11-14 01:19:18
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, LayerMask: LoadBiRefNetModelV2, Joy_caption_two, VAELoader, GrowMaskWithBlur, CLIPTextEncode, VAEEncode, SetLatentNoiseMask, SetLatentNoiseMask, VAEEncode, ImageScale, Get Image Size, GrowMaskWithBlur, ImageScale, VAEDecode, VAEEncode, SetLatentNoiseMask, Get Image Size, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LayerMask: BiRefNetUltraV2, ConstrainImage|pysssss, LayerUtility: RestoreCropBox, LayerUtility: CropByMask V2, KSampler, KSampler, KSampler, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, PreviewImage, Image Comparer (rgthree), SaveImage, CLIPTextEncode, GrowMaskWithBlur, CLIPLoader, VAEDecode, VAEDecode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Joy_caption_two_load, LayerMask: SegmentAnythingUltra V2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.15, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1104947676497949, "steps": 20}
---

# 平台全量/wan2.2 _ 全图修复 _ 分层式选择重绘幅度_1890358798970691585.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 _ 全图修复 _ 分层式选择重绘幅度_1890358798970691585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerMask: LoadBiRefNetModelV2`
- `Joy_caption_two`
- `VAELoader`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `ImageScale`
- `Get Image Size`
- `GrowMaskWithBlur`
- `ImageScale`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `Get Image Size`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LayerMask: BiRefNetUltraV2`
- `ConstrainImage|pysssss`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: CropByMask V2`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `GrowMaskWithBlur`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Joy_caption_two_load`
- `LayerMask: SegmentAnythingUltra V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1104947676497949`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.15`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerMask: LoadBiRefNetModelV2`、`Joy_caption_two`、`VAELoader`、`GrowMaskWithBlur`、`CLIPTextEncode`、`VAEEncode`、`SetLatentNoiseMask`、`ImageScale`、`Get Image Size`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: BiRefNetUltraV2`、`ConstrainImage|pysssss`、`LayerUtility: RestoreCropBox`、`LayerUtility: CropByMask V2`、`KSampler`、`LoadImage`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Joy_caption_two_load`、`LayerMask: SegmentAnythingUltra V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
