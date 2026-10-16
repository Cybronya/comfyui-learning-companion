---
key: 视频生成/图生视频/wan2.2 s2v + seevr2_1962480251441950721.json
name: wan2.2 s2v + seevr2_1962480251441950721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962480251441950721.json
hash: 49865c921ce3f730
coverage: 0.9
learned_at: 2026-10-15 22:31:31
nodes: [WanVideoDecode, WanVideoVAELoader, RH_GetAudioDuration, easy showAnything, ToInt, AudioSeparation, WanVideoAddS2VEmbeds, WanVideoVAELoader, WanVideoSampler, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoContextOptions, ImageResizeKJv2, WanVideoEmptyEmbeds, WanVideoEncode, VHS_VideoCombine, WanVideoLoraSelect, AudioEncoderLoader, AudioEncoderEncode, LoadImage, WanVideoTextEncode, VHS_LoadVideo, Int, SimpleMath+, AudioCrop, VHS_VideoCombine, easy showAnything, SeedVR2, SeedVR2BlockSwap, INTConstant, INTConstant, VHS_VideoInfoSource, WanVideoEncode, LoadAudio, PreviewAudio, easy showAnything, easy showAnything, DWPreprocessor, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 s2v + seevr2_1962480251441950721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962480251441950721.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoDecode`
- `WanVideoVAELoader`
- `RH_GetAudioDuration`
- `easy showAnything`
- `ToInt`
- `AudioSeparation`
- `WanVideoAddS2VEmbeds`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoContextOptions`
- `ImageResizeKJv2`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `AudioEncoderLoader`
- `AudioEncoderEncode`
- `LoadImage`
- `WanVideoTextEncode`
- `VHS_LoadVideo`
- `Int`
- `SimpleMath+`
- `AudioCrop`
- `VHS_VideoCombine`
- `easy showAnything`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `INTConstant`
- `INTConstant`
- `VHS_VideoInfoSource`
- `WanVideoEncode`
- `LoadAudio`
- `PreviewAudio`
- `easy showAnything`
- `easy showAnything`
- `DWPreprocessor`
- `ImageResizeKJv2`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`WanVideoDecode`、`WanVideoVAELoader`、`RH_GetAudioDuration`、`ToInt`、`AudioSeparation`、`WanVideoAddS2VEmbeds`、`WanVideoSampler`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoContextOptions`、`ImageResizeKJv2`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`AudioEncoderLoader`、`AudioEncoderEncode`、`LoadImage`、`WanVideoTextEncode`、`VHS_LoadVideo`、`Int`、`SimpleMath+`、`AudioCrop`、`SeedVR2`、`SeedVR2BlockSwap`、`INTConstant`、`VHS_VideoInfoSource`、`LoadAudio`、`PreviewAudio`、`DWPreprocessor`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、WanVideoSampler、AudioEncoderLoader、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
