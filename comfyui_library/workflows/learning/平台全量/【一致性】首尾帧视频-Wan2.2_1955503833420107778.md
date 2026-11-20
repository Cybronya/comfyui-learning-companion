---
key: 平台全量/【一致性】首尾帧视频-Wan2.2_1955503833420107778.json
name: 【一致性】首尾帧视频-Wan2.2_1955503833420107778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【一致性】首尾帧视频-Wan2.2_1955503833420107778.json
hash: 0e171b7abe3e2eb3
coverage: 0.532468
learned_at: 2026-11-14 01:22:33
nodes: [Int, Int, SetNode, GetNode, SetNode, WanVideoApplyNAG, WanVideoTextEncodeSingle, GetNode, easy negative, WanVideoTextEncode, SetNode, SetNode, GetNode, GetNode, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, GetIntFromJson, SetNode, GetIntFromJson, SetNode, GetBoolFromJson, SetNode, GetIntFromJson, SetNode, SetNode, GetFloatFromJson, GetBoolFromJson, GetFloatFromJson, SetNode, SetNode, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, easy mathInt, GetNode, easy mathInt, GetNode, WanVideoTorchCompileSettings, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, WanVideoLoraSelect, GetNode, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, easy ifElse, easy ifElse, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetLoRAs, ImpactSwitch, PrimitiveInt, easy positive, WanVideoImageToVideoEncode, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/【一致性】首尾帧视频-Wan2.2_1955503833420107778.json

> 来源文件 `comfyui_library/workflows/平台全量/【一致性】首尾帧视频-Wan2.2_1955503833420107778.json`

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

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoTextEncodeSingle、WanVideoVAELoader
