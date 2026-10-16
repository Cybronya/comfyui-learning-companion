---
key: 视频生成/文生视频/【KJ加速版】万相Wan2.2图生视频FusionX超级加速确保跑通_1958062823505088514.json
name: 【KJ加速版】万相Wan2.2图生视频FusionX超级加速确保跑通_1958062823505088514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1958062823505088514.json
hash: d0e3dc9bb8b930e0
coverage: 1
learned_at: 2026-10-15 22:43:41
nodes: [CreateCFGScheduleFloatList, WanVideoDecode, WanVideoSampler, WanVideoSampler, INTConstant, INTConstant, WanVideoImageToVideoEncode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, easy seed, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetImageSizeAndCount, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/【KJ加速版】万相Wan2.2图生视频FusionX超级加速确保跑通_1958062823505088514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958062823505088514.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `easy seed`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `LoadImage`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoSampler`、`INTConstant`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`easy seed`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
