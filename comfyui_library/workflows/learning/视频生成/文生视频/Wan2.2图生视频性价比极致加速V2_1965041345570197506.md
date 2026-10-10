---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json
name: Wan2.2图生视频性价比极致加速V2_1965041345570197506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json
hash: bdfc835f863a6e21
coverage: 0.72973
learned_at: 2026-10-10 23:07:22
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoTorchCompileSettings, easy globalSeed, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, easy seed, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoContextOptions, WanVideoSetRadialAttention, ImageResizeKJv2, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, String Literal, WanVideoLoraSelect, PrimitiveNode, WanVideoSigmaToStep, WanVideoScheduler, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, PrimitiveNode, WanVideoBlockSwap, VHS_VideoCombine]
patterns: []
missing: [String Literal, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_1965041345570197506.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `easy seed`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoSetRadialAttention`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `String Literal`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `WanVideoDecode`
- `WanVideoSetRadialAttention`
- `WanVideoScheduler`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoContextOptions`、`WanVideoSetRadialAttention`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`

**缺卡**（3）：`String Literal`、`easy globalSeed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
