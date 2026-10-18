---
key: 视频生成/图生视频/Wan2.2首尾帧视频+补帧_KJ版_2018932205057216513.json
name: Wan2.2首尾帧视频+补帧_KJ版_2018932205057216513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧视频+补帧_KJ版_2018932205057216513.json
hash: f0000805893999a3
coverage: 0.97619
learned_at: 2026-10-15 22:34:59
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, easy cleanGpuUsed, WanVideoSampler, WanVideoSLG, WanVideoSLG, WanVideoDecode, SimpleMath+, WanVideoSampler, ColorMatch, VHS_VideoCombine, VHS_VideoCombine, JWInteger, JWInteger, Float, CR Prompt Text, RIFE VFI, JWInteger, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧视频+补帧_KJ版_2018932205057216513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018932205057216513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `ImageResize+`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWInteger`
- `INTConstant`
- `PrimitiveNode`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoSLG`
- `WanVideoDecode`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `ColorMatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `Float`
- `CR Prompt Text`
- `RIFE VFI`
- `JWInteger`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoDecode`、`SimpleMath+`、`ColorMatch`、`VHS_VideoCombine`、`Float`、`CR Prompt Text`、`RIFE VFI`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
