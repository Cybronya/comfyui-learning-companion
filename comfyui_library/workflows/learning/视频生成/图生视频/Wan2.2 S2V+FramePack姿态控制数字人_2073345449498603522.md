---
key: 视频生成/图生视频/Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json
name: Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073345449498603522.json
hash: 59b798b57415bbe7
coverage: 0.840909
learned_at: 2026-10-15 22:41:06
nodes: [WanVideoSampler, WanVideoEmptyEmbeds, WanVideoEncode, MelBandRoFormerModelLoader, NormalizeAudioLoudness, AudioEncoderLoader, Note, ACE_AudioCrop, JWInteger, Note, JWInteger, Note, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, Note, Note, AudioEncoderEncode, WanVideoTextEncodeCached, CR Prompt Text, ImageResizeKJv2, DWPreprocessor, WanVideoEncode, ImageResizeKJv2, Note, WanVideoAddS2VEmbeds, PreviewAny, WanVideoDecode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, LoadImage, VHS_LoadVideo, VHS_LoadVideo, LoadAudio, MelBandRoFormerSampler, easy anythingIndexSwitch, GetImageRangeFromBatch, ColorMatch, VHS_VideoCombine, ImageResizeKJv2, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073345449498603522.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `MelBandRoFormerModelLoader`
- `NormalizeAudioLoudness`
- `AudioEncoderLoader`
- `Note`
- `ACE_AudioCrop`
- `JWInteger`
- `Note`
- `JWInteger`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `Note`
- `Note`
- `AudioEncoderEncode`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `Note`
- `WanVideoAddS2VEmbeds`
- `PreviewAny`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `easy anythingIndexSwitch`
- `GetImageRangeFromBatch`
- `ColorMatch`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_VideoCombine`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`MelBandRoFormerModelLoader`、`NormalizeAudioLoudness`、`AudioEncoderLoader`、`ACE_AudioCrop`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioEncoderEncode`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`ImageResizeKJv2`、`DWPreprocessor`、`WanVideoAddS2VEmbeds`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`MelBandRoFormerSampler`、`easy anythingIndexSwitch`、`GetImageRangeFromBatch`、`ColorMatch`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode
