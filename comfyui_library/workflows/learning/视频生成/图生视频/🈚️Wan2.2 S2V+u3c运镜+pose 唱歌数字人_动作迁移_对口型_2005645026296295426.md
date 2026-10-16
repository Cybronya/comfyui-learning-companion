---
key: 视频生成/图生视频/🈚️Wan2.2 S2V+u3c运镜+pose 唱歌数字人_动作迁移_对口型_2005645026296295426.json
name: 🈚️Wan2.2 S2V+u3c运镜+pose 唱歌数字人_动作迁移_对口型_2005645026296295426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2005645026296295426.json
hash: b80cfe0fd17c33bc
coverage: 0.416667
learned_at: 2026-10-15 22:33:58
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, SetNode, AudioEncoderEncode, WanVideoVAELoader, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, SetNode, SetNode, SetNode, GetImageRangeFromBatch, SetNode, SetNode, SetNode, GetNode, SetNode, WanVideoModelLoader, MelBandRoFormerSampler, SetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerModelLoader, SetNode, VHS_VideoCombine, AudioEncoderLoader, GetNode, WanVideoDecode, Fast Groups Bypasser (rgthree), ImageResizeKJv2, PreviewAny, NormalizeAudioLoudness, GetNode, GetNode, WanVideoTextEncodeCached, GetNode, Note, Fast Groups Bypasser (rgthree), SetNode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, SaveAudio, AudioSeparation, GetNode, GetNode, Reroute, WanVideoEncode, WanVideoEncode, WanVideoEncode, WanVideoBlockSwap, Note, GetNode, GetNode, SetNode, SetNode, GetNode, SaveAudio, GetNode, VHS_LoadAudioUpload, WanVideoUni3C_embeds, easy seed, WanVideoUni3C_ControlnetLoader, GetNode, WanVideoLoraSelect, WanVideoContextOptions, WanVideoSampler, GetNode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, WanVideoAddS2VEmbeds, WanVideoEmptyEmbeds, WanVideoLoraSelect, SetNode, VHS_VideoInfoLoaded, SetNode, LoadImage, Reroute, VHS_LoadVideo, Reroute, VHS_LoadVideo, Text, VHS_LoadVideo, VHS_VideoCombine, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, PoseDetectionOneToAllAnimation, WanVideoLoraSelect, WanVideoLoraSelect, Note, VHS_VideoCombine, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️Wan2.2 S2V+u3c运镜+pose 唱歌数字人_动作迁移_对口型_2005645026296295426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005645026296295426.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（120 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `AudioEncoderEncode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoModelLoader`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `VHS_VideoCombine`
- `AudioEncoderLoader`
- `GetNode`
- `WanVideoDecode`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `PreviewAny`
- `NormalizeAudioLoudness`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `SaveAudio`
- `AudioSeparation`
- `GetNode`
- `GetNode`
- `Reroute`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SaveAudio`
- `GetNode`
- `VHS_LoadAudioUpload`
- `WanVideoUni3C_embeds`
- `easy seed`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddS2VEmbeds`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `LoadImage`
- `Reroute`
- `VHS_LoadVideo`
- `Reroute`
- `VHS_LoadVideo`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `VHS_VideoCombine`
- `Int`
- `Int`

## 知识

覆盖率 **42%**（50/120）

**有卡**：`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`AudioEncoderEncode`、`WanVideoVAELoader`、`ImageResizeKJv2`、`GetImageRangeFromBatch`、`WanVideoModelLoader`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`VHS_VideoCombine`、`AudioEncoderLoader`、`WanVideoDecode`、`NormalizeAudioLoudness`、`WanVideoTextEncodeCached`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`SaveAudio`、`AudioSeparation`、`WanVideoEncode`、`WanVideoBlockSwap`、`VHS_LoadAudioUpload`、`WanVideoUni3C_embeds`、`easy seed`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelect`、`WanVideoContextOptions`、`WanVideoSampler`、`OnnxDetectionModelLoader`、`WanVideoAddS2VEmbeds`、`WanVideoEmptyEmbeds`、`VHS_VideoInfoLoaded`、`LoadImage`、`VHS_LoadVideo`、`Text`、`PoseDetectionOneToAllAnimation`、`Int`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、MelBandRoFormerSampler、easy seed、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader
