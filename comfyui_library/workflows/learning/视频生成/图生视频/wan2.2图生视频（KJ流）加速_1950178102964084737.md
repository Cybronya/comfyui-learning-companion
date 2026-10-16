---
key: 视频生成/图生视频/wan2.2图生视频（KJ流）加速_1950178102964084737.json
name: wan2.2图生视频（KJ流）加速_1950178102964084737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950178102964084737.json
hash: 06eca537206524fe
coverage: 0.892857
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, Note, GetImageSizeAndCount, WanVideoSampler, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, WanVideoTextEncode, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoModelLoader, WanVideoDecode, RH_Translator, ShowText|pysssss, WanVideoImageToVideoEncode, ImageResizeKJv2, Note, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频（KJ流）加速_1950178102964084737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950178102964084737.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `Note`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoTextEncode`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `RH_Translator`
- `ShowText|pysssss`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `Note`
- `VHS_VideoCombine`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoTextEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`WanVideoDecode`、`RH_Translator`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
