---
key: 视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json
name: Wan2.2 Multitalk-超好用图生视频_1953496222059384834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json
hash: 56140d0454c3ae3d
coverage: 0.9375
learned_at: 2026-10-10 23:06:51
nodes: [WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSampler, ImageResizeKJv2, DownloadAndLoadWav2VecModel, RH_GetAudioDuration, Int, MultiTalkWav2VecEmbeds, SimpleMath+, Float to Int, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, GetImageSizeAndCount, CreateCFGScheduleFloatList, INTConstant, INTConstant, LoadImage, LoadAudio, WanVideoSampler, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, VHS_VideoCombine]
patterns: []
missing: [Float to Int, SimpleMath+]
discoveries: [次要节点 `Float to Int` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `DownloadAndLoadWav2VecModel`
- `RH_GetAudioDuration`
- `Int`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `Float to Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoSampler`、`ImageResizeKJv2`、`DownloadAndLoadWav2VecModel`、`RH_GetAudioDuration`、`Int`、`MultiTalkWav2VecEmbeds`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`CreateCFGScheduleFloatList`、`INTConstant`、`LoadImage`、`LoadAudio`、`WanVideoTextEncode`、`VHS_VideoCombine`

**缺卡**（2）：`Float to Int`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
