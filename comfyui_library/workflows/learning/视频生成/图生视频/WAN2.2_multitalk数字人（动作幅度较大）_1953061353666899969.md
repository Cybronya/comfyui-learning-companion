---
key: 视频生成/图生视频/WAN2.2_multitalk数字人（动作幅度较大）_1953061353666899969.json
name: WAN2.2_multitalk数字人（动作幅度较大）_1953061353666899969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953061353666899969.json
hash: d2886291c65848a7
coverage: 0.975
learned_at: 2026-10-15 22:31:04
nodes: [WanVideoClipVisionEncode, WanVideoUni3C_ControlnetLoader, WanVideoEncode, Reroute, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, INTConstant, CreateCFGScheduleFloatList, INTConstant, WanVideoImageToVideoEncode, WanVideoUni3C_embeds, WanVideoContextOptions, ImageResizeKJv2, ImageResizeKJ, WanVideoSetLoRAs, WanVideoSetLoRAs, CLIPVisionLoader, AudioSeparation, AudioCrop, VHS_VideoCombine, WanVideoVAELoader, MultiTalkModelLoader, WanVideoModelLoader, WanVideoDecode, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, Int, VHS_DuplicateImages, MathExpression|pysssss, LoadAudio, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2_multitalk数字人（动作幅度较大）_1953061353666899969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953061353666899969.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoClipVisionEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `WanVideoUni3C_embeds`
- `WanVideoContextOptions`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `AudioSeparation`
- `AudioCrop`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkWav2VecEmbeds`
- `Int`
- `VHS_DuplicateImages`
- `MathExpression|pysssss`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LoadImage`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoContextOptions`、`ImageResizeKJv2`、`ImageResizeKJ`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`AudioSeparation`、`AudioCrop`、`VHS_VideoCombine`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`MultiTalkWav2VecEmbeds`、`Int`、`VHS_DuplicateImages`、`MathExpression|pysssss`、`LoadAudio`、`WanVideoSampler`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
