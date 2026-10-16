---
key: 视频生成/图生视频/高质量WAN2.2首尾帧极速版_2007622545448640513.json
name: 高质量WAN2.2首尾帧极速版_2007622545448640513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007622545448640513.json
hash: d092691569bffc30
coverage: 0.928571
learned_at: 2026-10-15 22:34:04
nodes: [WanVideoClipVisionEncode, ImageResize+, easy cleanGpuUsed, WanVideoDecode, INTConstant, WanVideoTextEncode, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoClipTextEncoder, JWInteger, JWInteger, CR SDXL Aspect Ratio, ImageResize+, WanVideoImageToVideoEncode, Bjornulf_ShowFloat, SimpleMath+, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, LoadImage, PrimitiveInt, PrimitiveInt, JWInteger, JWInteger, DF_Int_to_Float, CreateCFGScheduleFloatList, CR Prompt Text, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/高质量WAN2.2首尾帧极速版_2007622545448640513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007622545448640513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoClipVisionEncode`
- `ImageResize+`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `INTConstant`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoClipTextEncoder` ★核心
- `JWInteger`
- `JWInteger`
- `CR SDXL Aspect Ratio`
- `ImageResize+`
- `WanVideoImageToVideoEncode`
- `Bjornulf_ShowFloat`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `JWInteger`
- `JWInteger`
- `DF_Int_to_Float`
- `CreateCFGScheduleFloatList`
- `CR Prompt Text`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`WanVideoClipVisionEncode`、`ImageResize+`、`easy cleanGpuUsed`、`WanVideoDecode`、`INTConstant`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadWanVideoClipTextEncoder`、`JWInteger`、`CR SDXL Aspect Ratio`、`WanVideoImageToVideoEncode`、`Bjornulf_ShowFloat`、`SimpleMath+`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`LoadImage`、`DF_Int_to_Float`、`CreateCFGScheduleFloatList`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
