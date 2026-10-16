---
key: 视频生成/图生视频/6wan2.1万相图生视_1936315199089463298.json
name: 6wan2.1万相图生视_1936315199089463298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1936315199089463298.json
hash: 0c69ef21f8875d5b
coverage: 0.849057
learned_at: 2026-10-15 22:30:26
nodes: [BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, ConditioningZeroOut, UpscaleModelLoader, LyingSigmaSampler, VAELoader, KSamplerSelect, UltimateSDUpscaleCustomSample, BasicScheduler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy imageSize, VHS_VideoCombine, PreviewImage, Image Comparer (rgthree), ModelSamplingFlux, LoraLoader, UNETLoader, VHS_LoadVideo, PreviewImage, WanVideoSampler, WanVideoExperimentalArgs, WanVideoTeaCache, ImageSmartSharpen+, ImageScaleToMegapixels, UpscaleModelLoader, GIMMVFI_interpolate, easy cleanGpuUsed, WanVideoModelLoader, WanVideoDecode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoBlockSwap, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, Note, WanVideoTextEncode, WanVideoLoraSelect, LoadImage, WanVideoImageClipEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, VHS_LoadVideo]
patterns: [lora]
missing: []
parameters: {"lora_name": "增加细节SYK_Mild detail adjuster_V1.0_4（MINI）", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/6wan2.1万相图生视_1936315199089463298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936315199089463298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（53 个）：
- `BasicScheduler`
- `CLIPTextEncodeFlux` ★核心
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `UpscaleModelLoader`
- `LyingSigmaSampler` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `UltimateSDUpscaleCustomSample`
- `BasicScheduler`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `VHS_VideoCombine`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ModelSamplingFlux`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageSmartSharpen+`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `Note`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoImageClipEncode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `增加细节SYK_Mild detail adjuster_V1.0_4（MINI）`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **85%**（45/53）

**有卡**：`BasicScheduler`、`CLIPTextEncodeFlux`、`DualCLIPLoader`、`ConditioningZeroOut`、`UpscaleModelLoader`、`LyingSigmaSampler`、`VAELoader`、`KSamplerSelect`、`UltimateSDUpscaleCustomSample`、`easy imageSize`、`VHS_VideoCombine`、`ModelSamplingFlux`、`LoraLoader`、`UNETLoader`、`VHS_LoadVideo`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageSmartSharpen+`、`ImageScaleToMegapixels`、`GIMMVFI_interpolate`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTorchCompileSettings`、`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoImageClipEncode`

**用到的条目**：VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、KSamplerSelect、WanVideoSampler、LyingSigmaSampler、CLIPTextEncodeFlux
