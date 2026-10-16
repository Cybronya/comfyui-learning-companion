---
key: 视频生成/图生视频/首尾帧生视频加速-WAN2.2配LoRA权重高质量版_2037500087261208578.json
name: 首尾帧生视频加速-WAN2.2配LoRA权重高质量版_2037500087261208578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037500087261208578.json
hash: 6261c3dc823989a0
coverage: 0.975
learned_at: 2026-10-15 22:35:57
nodes: [LoadImage, JWInteger, JWInteger, JWInteger, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, INTConstant, WanVideoBlockSwap, SimpleMath+, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ImageResize+, WanVideoSetLoRAs, WanVideoImageToVideoEncode, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncode, JWInteger, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, DF_Int_to_Float, PrimitiveNode, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, ImageResize+, easy cleanGpuUsed, CR Prompt Text, MuyeTextEditOutput, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧生视频加速-WAN2.2配LoRA权重高质量版_2037500087261208578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037500087261208578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（40 个）：
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `INTConstant`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageResize+`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `DF_Int_to_Float`
- `PrimitiveNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `ImageResize+`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`LoadImage`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`INTConstant`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoSetBlockSwap`、`ImageResize+`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`DF_Int_to_Float`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`CR Prompt Text`、`MuyeTextEditOutput`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
