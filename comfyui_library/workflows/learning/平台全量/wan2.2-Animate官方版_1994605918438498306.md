---
key: 平台全量/wan2.2-Animate官方版_1994605918438498306.json
name: wan2.2-Animate官方版_1994605918438498306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-Animate官方版_1994605918438498306.json
hash: 3d28bf553f06c734
coverage: 0.892857
learned_at: 2026-11-14 01:19:28
nodes: [KSampler, KSampler, VAEDecode, TrimVideoLatent, TrimVideoLatent, VAEDecode, ImageFromBatch, WanAnimateToVideo, ImageFromBatch, MarkdownNote, MarkdownNote, ImageBatch, Mute / Bypass Repeater (rgthree), CreateVideo, ImageBatch, CreateVideo, SaveVideo, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPLoader, KSampler, MaskPreview, DownloadAndLoadSAM2Model, Sam2Segmentation, CLIPTextEncode, ImageBatch, PreviewImage, ModelSamplingSD3, Int, Mute / Bypass Repeater (rgthree), WanAnimateToVideo, WanAnimateToVideo, KSampler, easy float, VAEDecode, VAELoader, PreviewAnimation, PreviewAnimation, SaveVideo, TrimVideoLatent, ImageFromBatch, CreateVideo, Mute / Bypass Repeater (rgthree), SaveVideo, SaveVideo, Int, Fast Bypasser (rgthree), easy showAnything, MathExpression|pysssss, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, CLIPVisionEncode, ImageFromBatch, GrowMask, PixelPerfectResolution, ImageFromBatch, CreateVideo, VAEDecode, TrimVideoLatent, BlockifyMask, DrawMaskOnImage, CLIPTextEncode, PreviewImage, Fast Bypasser (rgthree), LayerMask: SegmentAnythingUltra V2, WanAnimateToVideo, Fast Bypasser (rgthree), Note, DWPreprocessor, DWPreprocessor, PreviewImage, CM_FloatToInt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Int, PointsEditor, VHS_VideoCombine, LoadImage, Reroute, Reroute, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 581460770651088, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.2-Animate官方版_1994605918438498306.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-Animate官方版_1994605918438498306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanAnimateToVideo`
- `ImageFromBatch`
- `MarkdownNote`
- `MarkdownNote`
- `ImageBatch`
- `Mute / Bypass Repeater (rgthree)`
- `CreateVideo`
- `ImageBatch`
- `CreateVideo`
- `SaveVideo`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `KSampler` ★核心
- `MaskPreview`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `CLIPTextEncode` ★核心
- `ImageBatch`
- `PreviewImage`
- `ModelSamplingSD3`
- `Int`
- `Mute / Bypass Repeater (rgthree)`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `easy float`
- `VAEDecode` ★核心
- `VAELoader`
- `PreviewAnimation`
- `PreviewAnimation`
- `SaveVideo`
- `TrimVideoLatent`
- `ImageFromBatch`
- `CreateVideo`
- `Mute / Bypass Repeater (rgthree)`
- `SaveVideo`
- `SaveVideo`
- `Int`
- `Fast Bypasser (rgthree)`
- `easy showAnything`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageFromBatch`
- `GrowMask`
- `PixelPerfectResolution`
- `ImageFromBatch`
- `CreateVideo`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Fast Bypasser (rgthree)`
- `LayerMask: SegmentAnythingUltra V2`
- `WanAnimateToVideo`
- `Fast Bypasser (rgthree)`
- `Note`
- `DWPreprocessor`
- `DWPreprocessor`
- `PreviewImage`
- `CM_FloatToInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `PointsEditor`
- `VHS_VideoCombine`
- `LoadImage`
- `Reroute`
- `Reroute`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `581460770651088`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（75/84）

**有卡**：`KSampler`、`VAEDecode`、`TrimVideoLatent`、`ImageFromBatch`、`WanAnimateToVideo`、`ImageBatch`、`Mute / Bypass Repeater (rgthree)`、`CreateVideo`、`SaveVideo`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`MaskPreview`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`CLIPTextEncode`、`ModelSamplingSD3`、`Int`、`easy float`、`VAELoader`、`PreviewAnimation`、`MathExpression|pysssss`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`CLIPVisionEncode`、`GrowMask`、`PixelPerfectResolution`、`BlockifyMask`、`DrawMaskOnImage`、`LayerMask: SegmentAnythingUltra V2`、`DWPreprocessor`、`CM_FloatToInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`PointsEditor`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
