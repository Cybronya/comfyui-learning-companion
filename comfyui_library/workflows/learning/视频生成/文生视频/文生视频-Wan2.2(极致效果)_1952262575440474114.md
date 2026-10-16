---
key: 视频生成/文生视频/文生视频-Wan2.2(极致效果)_1952262575440474114.json
name: 文生视频-Wan2.2(极致效果)_1952262575440474114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1952262575440474114.json
hash: 51bb6f6b82bcd853
coverage: 0.481013
learned_at: 2026-10-15 22:43:38
nodes: [WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoDecode, GetNode, easy negative, SetNode, WanVideoVAELoader, SetNode, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, PrimitiveString, JWStringSplit, easy convertAnything, easy convertAnything, SetNode, SetNode, GetNode, LoadWanVideoT5TextEncoder, WanVideoApplyNAG, WanVideoTextEncodeSingle, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoTextEncode, WanVideoEmptyEmbeds, GetNode, WanVideoLoraSelect, ImpactSwitch, easy positive, WanVideoSampler, GetIntFromJson, SetNode, GetIntFromJson, SetNode, GetBoolFromJson, SetNode, GetIntFromJson, SetNode, SetNode, GetFloatFromJson, GetBoolFromJson, GetFloatFromJson, SetNode, SetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, easy mathInt, GetNode, GetNode, easy mathInt, LoadJsonFromText, WanVideoModelLoader, WanVideoSetLoRAs, GetNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, GetNode, easy ifElse, easy ifElse, ImpactSwitch, PrimitiveInt, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText]
patterns: []
missing: []
---

# 视频生成/文生视频/文生视频-Wan2.2(极致效果)_1952262575440474114.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952262575440474114.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（79 个）：
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `easy negative`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `JWStringSplit`
- `easy convertAnything`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoLoraSelect`
- `ImpactSwitch`
- `easy positive`
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
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `LoadJsonFromText`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `GetNode`
- `easy ifElse`
- `easy ifElse`
- `ImpactSwitch`
- `PrimitiveInt`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `LoadJsonFromText`

## 知识

覆盖率 **48%**（38/79）

**有卡**：`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoDecode`、`easy negative`、`WanVideoVAELoader`、`JWStringSplit`、`easy convertAnything`、`LoadWanVideoT5TextEncoder`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelect`、`easy positive`、`WanVideoSampler`、`GetIntFromJson`、`GetBoolFromJson`、`GetFloatFromJson`、`easy mathInt`、`LoadJsonFromText`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect、WanVideoSetLoRAs
