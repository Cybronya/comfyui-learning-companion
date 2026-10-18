---
key: 视频生成/图生视频/Dasiwa V9 Vs Anisoxa v3 Vs Anime-U V3动漫视频对比_2011420423543590914.json
name: Dasiwa V9 Vs Anisoxa v3 Vs Anime-U V3动漫视频对比_2011420423543590914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Dasiwa V9 Vs Anisoxa v3 Vs Anime-U V3动漫视频对比_2011420423543590914.json
hash: cde5f8e42e20b64c
coverage: 0.842105
learned_at: 2026-10-15 22:34:22
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ImageScaleBy, Pick From Batch (mtb), easy cleanGpuUsed, CLIPVisionEncode, Note, Note, WanImageToVideo, Note, Note, Note, ModelSamplingSD3, LayerUtility: PurgeVRAM, ModelSamplingSD3, PreviewImage, ColorMatch, PathchSageAttentionKJ, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM, easy showAnything, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, VAELoader, CLIPVisionLoader, VHS_VideoCombine, Seed (rgthree), UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CR Prompt Text, Note, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, INTConstant, CreateCFGScheduleFloatList, WanVideoSigmaToStep, Float, WanVideoScheduler, WanVideoScheduler, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, PrimitiveNode, WanVideoLoraSelect, Wan22ImageToVideoLatent, CLIPTextEncode, KSampler, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, JWInteger, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, VHS_VideoCombine, UNETLoader, easy showAnything, CLIPLoader, Note, AILab_QwenVL, RH_LLMAPI_NODE, Reroute, GetImageSizeAndCount, AddLabel, LayerUtility: PurgeVRAM, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, AddLabel, AddLabel, ImageConcatMulti, RunningHub Deepcleaner, WanVideoModelLoader, VAEDecodeTiled, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 668589935468070, "steps": 20}
---

# 视频生成/图生视频/Dasiwa V9 Vs Anisoxa v3 Vs Anime-U V3动漫视频对比_2011420423543590914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011420423543590914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ImageScaleBy`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `Note`
- `WanImageToVideo`
- `Note`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `PreviewImage`
- `ColorMatch`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CR Prompt Text`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoLoraSelect`
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `easy showAnything`
- `CLIPLoader`
- `Note`
- `AILab_QwenVL`
- `RH_LLMAPI_NODE`
- `Reroute`
- `GetImageSizeAndCount`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `RunningHub Deepcleaner`
- `WanVideoModelLoader`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `668589935468070`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（80/95）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`Pick From Batch (mtb)`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`ColorMatch`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`KSamplerAdvanced`、`UNETLoader`、`VAELoader`、`CLIPVisionLoader`、`VHS_VideoCombine`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`LoadImage`、`CR Prompt Text`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`Float`、`WanVideoScheduler`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`Wan22ImageToVideoLatent`、`KSampler`、`CLIPLoader`、`JWInteger`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`AILab_QwenVL`、`RH_LLMAPI_NODE`、`GetImageSizeAndCount`、`AddLabel`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`RunningHub Deepcleaner`、`VAEDecodeTiled`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
