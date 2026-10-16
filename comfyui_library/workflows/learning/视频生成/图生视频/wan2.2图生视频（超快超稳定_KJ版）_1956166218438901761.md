---
key: 视频生成/图生视频/wan2.2图生视频（超快超稳定_KJ版）_1956166218438901761.json
name: wan2.2图生视频（超快超稳定_KJ版）_1956166218438901761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956166218438901761.json
hash: d1b01d205a8794b5
coverage: 0.561404
learned_at: 2026-10-15 22:31:11
nodes: [WanVideoBlockSwap, SetNode, SetNode, SetNode, WanVideoTorchCompileSettings, SetNode, WanVideoImageToVideoEncode, GetNode, INTConstant, CreateCFGScheduleFloatList, INTConstant, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, RH_Captioner, VHS_VideoCombine, easy showAnything, SetNode, WanVideoTextEncode, GetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoVAELoader, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, GetNode, GetNode, WanVideoLoraSelect, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, SetNode, SetNode, WanVideoModelLoader, WanVideoModelLoader, easy showAnything, RH_Prompter, RHHiddenNodes, TextCombinerTwo, TextCombinerTwo, GetNode, JjkText, Int, Int, Int, ImageResizeKJv2, WanVideoSampler, WanVideoSampler, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频（超快超稳定_KJ版）_1956166218438901761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956166218438901761.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（57 个）：
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `RH_Captioner`
- `VHS_VideoCombine`
- `easy showAnything`
- `SetNode`
- `WanVideoTextEncode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy showAnything`
- `RH_Prompter`
- `RHHiddenNodes`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `GetNode`
- `JjkText`
- `Int`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **56%**（32/57）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`RH_Captioner`、`VHS_VideoCombine`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`RH_Prompter`、`RHHiddenNodes`、`TextCombinerTwo`、`Int`、`ImageResizeKJv2`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
