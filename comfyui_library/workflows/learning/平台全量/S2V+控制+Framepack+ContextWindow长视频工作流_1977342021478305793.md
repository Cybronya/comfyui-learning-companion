---
key: 平台全量/S2V+控制+Framepack+ContextWindow长视频工作流_1977342021478305793.json
name: S2V+控制+Framepack+ContextWindow长视频工作流_1977342021478305793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/S2V+控制+Framepack+ContextWindow长视频工作流_1977342021478305793.json
hash: 50000bde0eab625b
coverage: 0.909091
learned_at: 2026-11-14 00:54:59
nodes: [LoadImage, ImageConcanate, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, WanVideoSampler, PreviewAny, VHS_VideoCombine, MelBandRoFormerSampler, AudioEncoderEncode, WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoDecode, DownloadAndLoadGIMMVFIModel, WanVideoEncode, WanVideoTextEncodeCached, ImageFlip+, PreviewImage, ToInt, Display Int (rgthree), SoundFlow_GetLength, easy int, SimpleMath+, WanVideoEncode, VHS_VideoCombine, PreviewImage, WanVideoBlockSwap, WanVideoContextOptions, WanVideoAddS2VEmbeds, Note, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, INTConstant, INTConstant, MelBandRoFormerModelLoader, AudioEncoderLoader, GIMMVFI_interpolate, VHS_VideoCombine, WanVideoEmptyEmbeds, DWPreprocessor, VHS_LoadVideo, LoadAudio, AudioCrop]
patterns: []
missing: []
---

# 平台全量/S2V+控制+Framepack+ContextWindow长视频工作流_1977342021478305793.json

> 来源文件 `comfyui_library/workflows/平台全量/S2V+控制+Framepack+ContextWindow长视频工作流_1977342021478305793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `LoadImage`
- `ImageConcanate`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `PreviewAny`
- `VHS_VideoCombine`
- `MelBandRoFormerSampler` ★核心
- `AudioEncoderEncode`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `ImageFlip+`
- `PreviewImage`
- `ToInt`
- `Display Int (rgthree)`
- `SoundFlow_GetLength`
- `easy int`
- `SimpleMath+`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoAddS2VEmbeds`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `MelBandRoFormerModelLoader`
- `AudioEncoderLoader`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `LoadAudio`
- `AudioCrop`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`LoadImage`、`ImageConcanate`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoSampler`、`VHS_VideoCombine`、`MelBandRoFormerSampler`、`AudioEncoderEncode`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`DownloadAndLoadGIMMVFIModel`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageFlip+`、`ToInt`、`Display Int (rgthree)`、`SoundFlow_GetLength`、`easy int`、`SimpleMath+`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`WanVideoAddS2VEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`INTConstant`、`MelBandRoFormerModelLoader`、`AudioEncoderLoader`、`GIMMVFI_interpolate`、`WanVideoEmptyEmbeds`、`DWPreprocessor`、`VHS_LoadVideo`、`LoadAudio`、`AudioCrop`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSampler、AudioEncoderEncode、AudioEncoderLoader、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
