---
key: 视频生成/图生视频/图生视频-Wan2.2(极致效果)_1952225607566438401.json
name: 图生视频-Wan2.2(极致效果)_1952225607566438401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952225607566438401.json
hash: 029a0b6d0b92e165
coverage: 0.52
learned_at: 2026-10-15 22:31:00
nodes: [Int, Int, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, WanVideoApplyNAG, WanVideoTextEncodeSingle, GetNode, easy negative, WanVideoTextEncode, SetNode, SetNode, GetNode, GetNode, easy positive, LoadImage, SetNode, GetNode, GetNode, ImpactSwitch, SetNode, WanVideoLoraSelect, WanVideoSampler, GetIntFromJson, SetNode, GetIntFromJson, SetNode, GetBoolFromJson, SetNode, GetIntFromJson, SetNode, SetNode, GetFloatFromJson, GetBoolFromJson, GetFloatFromJson, SetNode, SetNode, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoLoraSelect, easy mathInt, GetNode, easy mathInt, GetNode, easy ifElse, easy ifElse, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoModelLoader, LoadJsonFromText, LoadJsonFromText, ImpactSwitch, PrimitiveInt, WanVideoSetLoRAs, WanVideoImageToVideoEncode, LoadJsonFromText, LoadJsonFromText, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频-Wan2.2(极致效果)_1952225607566438401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952225607566438401.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（75 个）：
- `Int`
- `Int`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
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
- `easy positive`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
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
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `easy mathInt`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `easy ifElse`
- `easy ifElse`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `ImpactSwitch`
- `PrimitiveInt`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `WanVideoBlockSwap`

## 知识

覆盖率 **52%**（39/75）

**有卡**：`Int`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`easy negative`、`WanVideoTextEncode`、`easy positive`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoSampler`、`GetIntFromJson`、`GetBoolFromJson`、`GetFloatFromJson`、`WanVideoSetBlockSwap`、`easy mathInt`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`LoadJsonFromText`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
