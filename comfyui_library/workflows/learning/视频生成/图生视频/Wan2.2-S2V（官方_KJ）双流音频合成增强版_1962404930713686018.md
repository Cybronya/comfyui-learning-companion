---
key: 视频生成/图生视频/Wan2.2-S2V（官方_KJ）双流音频合成增强版_1962404930713686018.json
name: Wan2.2-S2V（官方_KJ）双流音频合成增强版_1962404930713686018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-S2V（官方_KJ）双流音频合成增强版_1962404930713686018.json
hash: d65425de4c04a64f
coverage: 0.673913
learned_at: 2026-10-15 22:31:30
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoModelLoader, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoEncode, GetNode, ImageResizeKJv2, WanVideoEmptyEmbeds, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfoLoaded, GetNode, MelBandRoFormerModelLoader, GetNode, WanVideoAddS2VEmbeds, GetNode, WanVideoDecode, easy cleanGpuUsed, easy clearCacheAll, GetNode, GetNode, VHS_VideoCombine, easy clearCacheAll, SetNode, WanVideoSampler, SeargeIntegerConstant, SeargeIntegerConstant, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, WanVideoTextEncodeCached, Primitive string multiline [Crystools], SetNode, AudioEncoderEncode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, easy cleanGpuUsed, easy clearCacheAll, CLIPTextEncode, GetNode, CLIPTextEncode, VAEDecode, GetNode, GetNode, WanSoundImageToVideo, ImageResizeKJv2, GetNode, VHS_VideoCombine, SeedVR2, VHS_VideoInfo, SeedVR2BlockSwap, VHS_VideoCombine, UnloadAllModels, easy cleanGpuUsed, VHS_VideoCombine, GetNode, AudioEncoderLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, easy clearCacheAll, Video_Upscale_With_Model, Free_Video_Memory, easy cleanGpuUsed, VHS_VideoCombine, GetNode, easy clearCacheAll, WanVideoContextOptions, KSampler, VHS_LoadVideo, ContextWindowsManual, LoadImage, WanVideoLoraSelect, AudioEncoderLoader, MelBandRoFormerSampler, AudioEncoderEncode, Fast Groups Bypasser (rgthree), VHS_LoadVideoPath, VHS_LoadVideoPath]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 968810699390732, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-S2V（官方_KJ）双流音频合成增强版_1962404930713686018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962404930713686018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（92 个）：
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
- `GetNode`
- `WanVideoAddS2VEmbeds`
- `GetNode`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `SetNode`
- `WanVideoSampler` ★核心
- `SeargeIntegerConstant`
- `SeargeIntegerConstant`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `WanVideoTextEncodeCached`
- `Primitive string multiline [Crystools]`
- `SetNode`
- `AudioEncoderEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `WanSoundImageToVideo`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
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
- `easy clearCacheAll`
- `Video_Upscale_With_Model`
- `Free_Video_Memory`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `GetNode`
- `easy clearCacheAll`
- `WanVideoContextOptions`
- `KSampler` ★核心
- `VHS_LoadVideo`
- `ContextWindowsManual`
- `LoadImage`
- `WanVideoLoraSelect`
- `AudioEncoderLoader`
- `MelBandRoFormerSampler` ★核心
- `AudioEncoderEncode`
- `Fast Groups Bypasser (rgthree)`
- `VHS_LoadVideoPath`
- `VHS_LoadVideoPath`

## 关键参数

- `seed` = `968810699390732`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（62/92）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoEmptyEmbeds`、`VHS_VideoInfoLoaded`、`MelBandRoFormerModelLoader`、`WanVideoAddS2VEmbeds`、`WanVideoDecode`、`easy clearCacheAll`、`VHS_VideoCombine`、`WanVideoSampler`、`SeargeIntegerConstant`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`WanVideoTextEncodeCached`、`Primitive string multiline [Crystools]`、`AudioEncoderEncode`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`WanSoundImageToVideo`、`SeedVR2`、`VHS_VideoInfo`、`SeedVR2BlockSwap`、`UnloadAllModels`、`AudioEncoderLoader`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`Video_Upscale_With_Model`、`Free_Video_Memory`、`WanVideoContextOptions`、`KSampler`、`VHS_LoadVideo`、`ContextWindowsManual`、`LoadImage`、`WanVideoLoraSelect`、`MelBandRoFormerSampler`、`VHS_LoadVideoPath`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
