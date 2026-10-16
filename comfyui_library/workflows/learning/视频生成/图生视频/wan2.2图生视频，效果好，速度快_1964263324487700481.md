---
key: 视频生成/图生视频/wan2.2图生视频，效果好，速度快_1964263324487700481.json
name: wan2.2图生视频，效果好，速度快_1964263324487700481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964263324487700481.json
hash: 596079d261324b70
coverage: 0.909091
learned_at: 2026-10-15 22:31:34
nodes: [ImageStitch, easy showAnything, easy ifElse, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoClipVisionEncode, WanVideoSLG, CogVideoEnhanceAVideo, SimpleMath+, LayerUtility: ImageMaskScaleAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, LoadWanVideoClipTextEncoder, CLIPVisionLoader, Textbox, PrimitiveBoolean, easy int, easy cleanGpuUsed, WanVideoImageToVideoEncode, easy ifElse, CLIPTextEncode, easy cleanGpuUsed, CR Text Replace, RH_Captioner, VAELoader, Note, LayerUtility: ImageScaleByAspectRatio V2, TextBox, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, TextBox, easy showAnything, SimpleMath+, easy int, ModelSamplingSD3, WanImageToVideo, ModelSamplingSD3, RH_Translator, easy showAnything, DF_Integer, VHS_VideoCombine, LoadImage, LoadImage, CLIPVisionEncode, CLIPVisionLoader, CLIPTextEncode, easy showAnything, DF_Integer, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, TextBox, PrimitiveBoolean, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频，效果好，速度快_1964263324487700481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964263324487700481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（88 个）：
- `ImageStitch`
- `easy showAnything`
- `easy ifElse`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `SimpleMath+`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `LoadWanVideoClipTextEncoder` ★核心
- `CLIPVisionLoader`
- `Textbox`
- `PrimitiveBoolean`
- `easy int`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CR Text Replace`
- `RH_Captioner`
- `VAELoader`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextBox`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `TextBox`
- `easy showAnything`
- `SimpleMath+`
- `easy int`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `RH_Translator`
- `easy showAnything`
- `DF_Integer`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `DF_Integer`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `TextBox`
- `PrimitiveBoolean`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（80/88）

**有卡**：`ImageStitch`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`SimpleMath+`、`LayerUtility: ImageMaskScaleAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`LoadWanVideoClipTextEncoder`、`CLIPVisionLoader`、`Textbox`、`PrimitiveBoolean`、`easy int`、`WanVideoImageToVideoEncode`、`CLIPTextEncode`、`CR Text Replace`、`VAELoader`、`TextBox`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`RH_Translator`、`DF_Integer`、`VHS_VideoCombine`、`LoadImage`、`CLIPVisionEncode`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
