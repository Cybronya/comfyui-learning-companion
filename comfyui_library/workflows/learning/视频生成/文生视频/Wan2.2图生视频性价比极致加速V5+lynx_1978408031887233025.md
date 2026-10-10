---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_1978408031887233025.json
name: Wan2.2图生视频性价比极致加速V5+lynx_1978408031887233025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_1978408031887233025.json
hash: 4e91b1293bc635cb
coverage: 0.732143
learned_at: 2026-10-10 23:07:25
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, WanVideoModelLoader, easy seed, WanVideoTorchCompileSettings, easy globalSeed, GetNode, LoadWanVideoT5TextEncoder, Note, easy showAnything, PreviewImage, easy showAnything, WanVideoModelLoader, Int, PrimitiveNode, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, Int, Int, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoTextEncodeCached, LynxEncodeFaceIP, RH_Captioner, LoadLynxResampler, LynxInsightFaceCrop, WanVideoImageToVideoEncode, ImageResizeKJv2, WanVideoAddLynxEmbeds, WanVideoVAELoader, LoadImage, String Literal, WanVideoExtraModelSelect]
patterns: []
missing: [String Literal, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_1978408031887233025.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_1978408031887233025.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSetRadialAttention`
- `PrimitiveNode`
- `WanVideoDecode`
- `WanVideoSetRadialAttention`
- `WanVideoScheduler`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `easy seed`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `easy showAnything`
- `PreviewImage`
- `easy showAnything`
- `WanVideoModelLoader`
- `Int`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoTextEncodeCached`
- `LynxEncodeFaceIP`
- `RH_Captioner`
- `LoadLynxResampler` ★核心
- `LynxInsightFaceCrop`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `WanVideoAddLynxEmbeds`
- `WanVideoVAELoader`
- `LoadImage`
- `String Literal`
- `WanVideoExtraModelSelect`

## 知识

覆盖率 **73%**（41/56）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`Int`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`RH_Captioner`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoAddLynxEmbeds`、`WanVideoVAELoader`、`LoadImage`

**缺卡**（3）：`String Literal`、`easy globalSeed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
