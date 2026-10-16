---
key: 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1955836777492725762.json
name: 首尾帧视频-Wan2.2(极致效果)_1955836777492725762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955836777492725762.json
hash: 6a7322ae3bcdce3e
coverage: 0.532468
learned_at: 2026-10-15 22:31:10
nodes: [Int, Int, SetNode, GetNode, SetNode, WanVideoApplyNAG, WanVideoTextEncodeSingle, GetNode, easy negative, WanVideoTextEncode, SetNode, SetNode, GetNode, GetNode, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, GetIntFromJson, SetNode, GetIntFromJson, SetNode, GetBoolFromJson, SetNode, GetIntFromJson, SetNode, SetNode, GetFloatFromJson, GetBoolFromJson, GetFloatFromJson, SetNode, SetNode, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, easy mathInt, GetNode, easy mathInt, GetNode, WanVideoTorchCompileSettings, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, WanVideoLoraSelect, GetNode, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, easy ifElse, easy ifElse, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetLoRAs, ImpactSwitch, PrimitiveInt, easy positive, WanVideoImageToVideoEncode, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1955836777492725762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955836777492725762.json`

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
- `LayerUtility: ImageMaskScaleAsV2`
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
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **53%**（41/77）

**有卡**：`Int`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`easy negative`、`WanVideoTextEncode`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetIntFromJson`、`GetBoolFromJson`、`GetFloatFromJson`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`easy mathInt`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`easy positive`、`WanVideoImageToVideoEncode`、`LoadJsonFromText`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
