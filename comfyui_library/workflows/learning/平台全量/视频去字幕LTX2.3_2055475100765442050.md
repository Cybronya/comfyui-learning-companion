---
key: 平台全量/视频去字幕LTX2.3_2055475100765442050.json
name: 视频去字幕LTX2.3_2055475100765442050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频去字幕LTX2.3_2055475100765442050.json
hash: ef7e1e03c567669a
coverage: 1
learned_at: 2026-11-14 02:35:56
nodes: [PathchSageAttentionKJ, LTXAVTextEncoderLoader, CLIPTextEncode, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, LTXVAudioVAELoader, ManualSigmas, CheckpointLoaderSimple, LTXAddVideoICLoRAGuide, LTXVPreprocess, RandomNoise, Seed (rgthree), SamplerCustomAdvanced, VAEDecodeTiled, CFGGuider, EmptyLTXVLatentVideo, LayerUtility: ColorImage, ResizeImageMaskNode, ImageBatchMulti, easy setNode, LayerUtility: ColorImage, LTXVCropGuides, ResizeImageMaskNode, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VHS_VideoInfoLoaded, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, easy getNode, ImageConcanate, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, LTXICLoRALoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/视频去字幕LTX2.3_2055475100765442050.json

> 来源文件 `comfyui_library/workflows/平台全量/视频去字幕LTX2.3_2055475100765442050.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（43 个）：
- `PathchSageAttentionKJ`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVPreprocess`
- `RandomNoise`
- `Seed (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ColorImage`
- `ResizeImageMaskNode`
- `ImageBatchMulti`
- `easy setNode`
- `LayerUtility: ColorImage`
- `LTXVCropGuides`
- `ResizeImageMaskNode`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VHS_VideoInfoLoaded`
- `SimpleMath+`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `easy getNode`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `LTXICLoRALoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **100%**（43/43）

**有卡**：`PathchSageAttentionKJ`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAddVideoICLoRAGuide`、`LTXVPreprocess`、`RandomNoise`、`Seed (rgthree)`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LayerUtility: ColorImage`、`ResizeImageMaskNode`、`ImageBatchMulti`、`easy setNode`、`LTXVCropGuides`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VHS_VideoInfoLoaded`、`SimpleMath+`、`GetImageRangeFromBatch`、`easy getNode`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`、`LTXICLoRALoaderModelOnly`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
