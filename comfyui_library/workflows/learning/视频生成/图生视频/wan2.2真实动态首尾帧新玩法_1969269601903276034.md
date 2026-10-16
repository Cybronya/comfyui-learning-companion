---
key: 视频生成/图生视频/wan2.2真实动态首尾帧新玩法_1969269601903276034.json
name: wan2.2真实动态首尾帧新玩法_1969269601903276034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969269601903276034.json
hash: 2a3f94a95c42addb
coverage: 0.5125
learned_at: 2026-10-15 22:31:48
nodes: [GetNode, GetBoolFromJson, SetNode, SetNode, SetNode, GetFloatFromJson, GetBoolFromJson, GetFloatFromJson, GetNode, GetNode, easy ifElse, WanVideoSetLoRAs, GetNode, LayerUtility: ImageMaskScaleAsV2, GetNode, SetNode, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoModelLoader, easy ifElse, WanVideoSetBlockSwap, WanVideoSetBlockSwap, SetNode, SetNode, WanVideoBlockSwap, WanVideoApplyNAG, GetNode, GetNode, GetNode, GetNode, GetNode, easy mathInt, GetNode, GetNode, GetNode, GetNode, easy mathInt, GetNode, GetNode, SetNode, SetNode, LoadImage, LoadImage, WanVideoDecode, SetNode, SetNode, WanVideoTextEncodeSingle, SetNode, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, SetNode, Int, Int, GetIntFromJson, SetNode, SetNode, SetNode, GetIntFromJson, SetNode, GetIntFromJson, WanVideoImageToVideoEncode, ImpactSwitch, WanVideoTextEncode, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, VHS_VideoCombine, ImpactSwitch, WanVideoSampler, WanVideoSampler, Note, PrimitiveInt, easy positive, easy negative]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2真实动态首尾帧新玩法_1969269601903276034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969269601903276034.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
- `GetNode`
- `GetBoolFromJson`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetFloatFromJson`
- `GetBoolFromJson`
- `GetFloatFromJson`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `WanVideoSetLoRAs`
- `GetNode`
- `LayerUtility: ImageMaskScaleAsV2`
- `GetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `easy ifElse`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoApplyNAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeSingle`
- `SetNode`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `Int`
- `Int`
- `GetIntFromJson`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetIntFromJson`
- `SetNode`
- `GetIntFromJson`
- `WanVideoImageToVideoEncode`
- `ImpactSwitch`
- `WanVideoTextEncode`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Note`
- `PrimitiveInt`
- `easy positive`
- `easy negative`

## 知识

覆盖率 **51%**（41/80）

**有卡**：`GetBoolFromJson`、`GetFloatFromJson`、`WanVideoSetLoRAs`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`easy mathInt`、`LoadImage`、`WanVideoDecode`、`WanVideoTextEncodeSingle`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`GetIntFromJson`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadJsonFromText`、`VHS_VideoCombine`、`WanVideoSampler`、`easy positive`、`easy negative`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
