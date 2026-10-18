---
key: 视频生成/图生视频/声音+图片+视频动作，S2V+控制+Framepack+ContextWindow长视频工作流_1964517302806921217.json
name: 声音+图片+视频动作，S2V+控制+Framepack+ContextWindow长视频工作流_1964517302806921217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/声音+图片+视频动作，S2V+控制+Framepack+ContextWindow长视频工作流_1964517302806921217.json
hash: 1eb86f7be2619e90
coverage: 0.928571
learned_at: 2026-10-15 22:31:35
nodes: [DownloadAndLoadGIMMVFIModel, SoundFlow_GetLength, INTConstant, GIMMVFI_interpolate, LoadAudio, ImageResizeKJv2, WanVideoEncode, VHS_VideoCombine, ImageResizeKJv2, DWPreprocessor, WanVideoDecode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ToInt, SimpleMath+, Display Int (rgthree), AudioEncoderLoader, AudioEncoderEncode, easy int, WanVideoEncode, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, WanVideoSampler, WanVideoContextOptions, PreviewAny, VHS_VideoCombine, AudioCrop, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVAELoader, ImageConcanate, VHS_LoadVideo, PreviewImage, LoadImage, WanVideoTextEncodeCached, Note, INTConstant, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/声音+图片+视频动作，S2V+控制+Framepack+ContextWindow长视频工作流_1964517302806921217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964517302806921217.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `DownloadAndLoadGIMMVFIModel`
- `SoundFlow_GetLength`
- `INTConstant`
- `GIMMVFI_interpolate`
- `LoadAudio`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `WanVideoDecode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `ToInt`
- `SimpleMath+`
- `Display Int (rgthree)`
- `AudioEncoderLoader`
- `AudioEncoderEncode`
- `easy int`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `PreviewAny`
- `VHS_VideoCombine`
- `AudioCrop`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `ImageConcanate`
- `VHS_LoadVideo`
- `PreviewImage`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `Note`
- `INTConstant`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`SoundFlow_GetLength`、`INTConstant`、`GIMMVFI_interpolate`、`LoadAudio`、`ImageResizeKJv2`、`WanVideoEncode`、`VHS_VideoCombine`、`DWPreprocessor`、`WanVideoDecode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`ToInt`、`SimpleMath+`、`Display Int (rgthree)`、`AudioEncoderLoader`、`AudioEncoderEncode`、`easy int`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`WanVideoSampler`、`WanVideoContextOptions`、`AudioCrop`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageConcanate`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached
