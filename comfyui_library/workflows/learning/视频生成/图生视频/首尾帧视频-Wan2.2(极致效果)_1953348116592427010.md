---
key: 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1953348116592427010.json
name: 首尾帧视频-Wan2.2(极致效果)_1953348116592427010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953348116592427010.json
hash: 9ba90a1e8bb41bac
coverage: 0.532468
learned_at: 2026-10-15 22:31:04
nodes: [Int, Int, SetNode, GetNode, SetNode, WanVideoApplyNAG, WanVideoTextEncodeSingle, GetNode, easy negative, WanVideoTextEncode, SetNode, SetNode, GetNode, GetNode, LoadImage, LayerUtility: ImageMaskScaleAsV2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, GetIntFromJson, SetNode, GetIntFromJson, SetNode, GetBoolFromJson, SetNode, GetIntFromJson, SetNode, SetNode, GetFloatFromJson, GetBoolFromJson, GetFloatFromJson, SetNode, SetNode, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, easy mathInt, GetNode, easy mathInt, GetNode, WanVideoTorchCompileSettings, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, WanVideoLoraSelect, GetNode, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, easy ifElse, easy ifElse, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetLoRAs, ImpactSwitch, PrimitiveInt, easy positive, WanVideoImageToVideoEncode, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1953348116592427010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953348116592427010.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
- `Int`
- `Int`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `easy negative`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactSwitch`
- `GetIntFromJson`
- `SetNode`
- `GetIntFromJson`
- `SetNode`
- `GetBoolFromJson`
- `SetNode`
- `GetIntFromJson`
- `SetNode`
- `SetNode`
- `GetFloatFromJson`
- `GetBoolFromJson`
- `GetFloatFromJson`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `easy ifElse`
- `easy ifElse`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `ImpactSwitch`
- `PrimitiveInt`
- `easy positive`
- `WanVideoImageToVideoEncode`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `LoadJsonFromText`

## 知识

覆盖率 **53%**（41/77）

**有卡**：`Int`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`easy negative`、`WanVideoTextEncode`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetIntFromJson`、`GetBoolFromJson`、`GetFloatFromJson`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`easy mathInt`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`easy positive`、`WanVideoImageToVideoEncode`、`LoadJsonFromText`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
