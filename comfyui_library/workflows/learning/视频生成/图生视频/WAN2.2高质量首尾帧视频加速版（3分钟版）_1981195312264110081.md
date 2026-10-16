---
key: 视频生成/图生视频/WAN2.2高质量首尾帧视频加速版（3分钟版）_1981195312264110081.json
name: WAN2.2高质量首尾帧视频加速版（3分钟版）_1981195312264110081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981195312264110081.json
hash: 228d66aea33ec051
coverage: 0.972973
learned_at: 2026-10-15 22:32:36
nodes: [ImageResize+, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResize+, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy cleanGpuUsed, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoDecode, DF_Int_to_Float, PrimitiveNode, JWInteger, INTConstant, SimpleMath+, LoadImage, LoadImage, JWInteger, JWInteger, JWInteger, JWInteger, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2高质量首尾帧视频加速版（3分钟版）_1981195312264110081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981195312264110081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（37 个）：
- `ImageResize+`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `ImageResize+`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `DF_Int_to_Float`
- `PrimitiveNode`
- `JWInteger`
- `INTConstant`
- `SimpleMath+`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`ImageResize+`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`DF_Int_to_Float`、`JWInteger`、`INTConstant`、`SimpleMath+`、`LoadImage`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
