---
key: 视频生成/图生视频/Wan2.2-S2V参考视频（官方_KJ）双流音频合成增强版_1962460220972732417.json
name: Wan2.2-S2V参考视频（官方_KJ）双流音频合成增强版_1962460220972732417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-S2V参考视频（官方_KJ）双流音频合成增强版_1962460220972732417.json
hash: 166ee7e0cddbfd73
coverage: 0.651376
learned_at: 2026-10-15 22:31:31
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoModelLoader, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoEncode, GetNode, ImageResizeKJv2, WanVideoEmptyEmbeds, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfoLoaded, GetNode, MelBandRoFormerModelLoader, AudioEncoderLoader, GetNode, GetNode, WanVideoDecode, easy cleanGpuUsed, GetNode, GetNode, AudioEncoderEncode, easy clearCacheAll, SetNode, WanVideoSampler, MelBandRoFormerSampler, UNETLoader, CLIPLoader, WanVideoTextEncodeCached, Primitive string multiline [Crystools], SetNode, AudioEncoderEncode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, GetNode, WanSoundImageToVideo, ImageResizeKJv2, SeedVR2, VHS_VideoInfo, SeedVR2BlockSwap, VHS_VideoCombine, UnloadAllModels, easy cleanGpuUsed, VHS_VideoCombine, GetNode, AudioEncoderLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, Video_Upscale_With_Model, Free_Video_Memory, easy cleanGpuUsed, VHS_VideoCombine, GetNode, easy clearCacheAll, WanVideoLoraSelect, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, LoadImage, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, WanVideoEncode, VHS_VideoCombine, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageResizeKJv2, DWPreprocessor, ImageResizeKJv2, KSampler, ContextWindowsManual, DWPreprocessor, VHS_LoadVideo, SeargeIntegerConstant, SeargeIntegerConstant, WanVideoAddS2VEmbeds, VHS_LoadVideoPath, VHS_LoadVideoPath, Fast Groups Bypasser (rgthree), WanVideoContextOptions, easy clearCacheAll, easy clearCacheAll, Reroute]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 129072981727977, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-S2V参考视频（官方_KJ）双流音频合成增强版_1962460220972732417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962460220972732417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（109 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoEmptyEmbeds`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `AudioEncoderLoader`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `easy clearCacheAll`
- `SetNode`
- `WanVideoSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `WanVideoTextEncodeCached`
- `Primitive string multiline [Crystools]`
- `SetNode`
- `AudioEncoderEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `WanSoundImageToVideo`
- `ImageResizeKJv2`
- `SeedVR2`
- `VHS_VideoInfo`
- `SeedVR2BlockSwap`
- `VHS_VideoCombine`
- `UnloadAllModels`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `GetNode`
- `AudioEncoderLoader`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `Video_Upscale_With_Model`
- `Free_Video_Memory`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `GetNode`
- `easy clearCacheAll`
- `WanVideoLoraSelect`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `KSampler` ★核心
- `ContextWindowsManual`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `SeargeIntegerConstant`
- `SeargeIntegerConstant`
- `WanVideoAddS2VEmbeds`
- `VHS_LoadVideoPath`
- `VHS_LoadVideoPath`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoContextOptions`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `Reroute`

## 关键参数

- `seed` = `129072981727977`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（71/109）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoEmptyEmbeds`、`VHS_VideoInfoLoaded`、`MelBandRoFormerModelLoader`、`AudioEncoderLoader`、`WanVideoDecode`、`AudioEncoderEncode`、`easy clearCacheAll`、`WanVideoSampler`、`MelBandRoFormerSampler`、`UNETLoader`、`CLIPLoader`、`WanVideoTextEncodeCached`、`Primitive string multiline [Crystools]`、`CLIPTextEncode`、`WanSoundImageToVideo`、`SeedVR2`、`VHS_VideoInfo`、`SeedVR2BlockSwap`、`VHS_VideoCombine`、`UnloadAllModels`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`Video_Upscale_With_Model`、`Free_Video_Memory`、`WanVideoLoraSelect`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`LoadImage`、`VAEDecode`、`DWPreprocessor`、`KSampler`、`ContextWindowsManual`、`VHS_LoadVideo`、`SeargeIntegerConstant`、`WanVideoAddS2VEmbeds`、`VHS_LoadVideoPath`、`WanVideoContextOptions`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
