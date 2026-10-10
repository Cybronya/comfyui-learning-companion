---
key: 首尾帧视频-WAN2.2高质量版_1980937502708158465.json
name: 首尾帧视频-WAN2.2高质量版_1980937502708158465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json
hash: 06451172ab7434c2
coverage: 0.777778
learned_at: 2026-10-10 21:00:00
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, easy cleanGpuUsed, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, WanVideoSampler, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoImageToVideoEncode, SimpleMath+, JWInteger, JWInteger, JWInteger, LoadImage, LoadImage, CreateCFGScheduleFloatList, VHS_VideoCombine, CR Prompt Text, WanVideoTextEncode]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+, easy cleanGpuUsed, CR Prompt Text, ImageResize+, ImageResize+]
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 首尾帧视频-WAN2.2高质量版_1980937502708158465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（36 个）：
- `ImageResize+`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `easy cleanGpuUsed`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `WanVideoTextEncode`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`LoadImage`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoTextEncode`

**缺卡**（7）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`easy cleanGpuUsed`、`CR Prompt Text`、`ImageResize+`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
