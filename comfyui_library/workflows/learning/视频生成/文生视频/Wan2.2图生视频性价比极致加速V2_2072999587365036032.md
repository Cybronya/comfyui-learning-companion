---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_2072999587365036032.json
name: Wan2.2图生视频性价比极致加速V2_2072999587365036032
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_2072999587365036032.json
hash: 5cc044ccd49414a0
coverage: 0.810811
learned_at: 2026-10-15 22:47:14
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoTorchCompileSettings, easy globalSeed, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, easy seed, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoContextOptions, WanVideoSetRadialAttention, ImageResizeKJv2, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, String Literal, WanVideoLoraSelect, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, PrimitiveNode, WanVideoBlockSwap, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_2072999587365036032.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_2072999587365036032.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `easy seed`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoSetRadialAttention`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `String Literal`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `WanVideoDecode`
- `WanVideoSetRadialAttention`
- `WanVideoScheduler`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTextEncode`、`easy seed`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoContextOptions`、`WanVideoSetRadialAttention`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`LoadImage`、`String Literal`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
