---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V4_1978022050193362945.json
name: Wan2.2图生视频性价比极致加速V4_1978022050193362945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V4_1978022050193362945.json
hash: bf51e7300de469ca
coverage: 0.736842
learned_at: 2026-10-10 23:07:24
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, easy seed, WanVideoTorchCompileSettings, easy globalSeed, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Note, easy showAnything, PreviewImage, easy showAnything, WanVideoLoraSelect, Int, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, WanVideoSigmaToStep, WanVideoExtraModelSelect, LoadLynxResampler, WanVideoExtraModelSelect, WanVideoTextEncodeCached, WanVideoVAELoader, LynxEncodeFaceIP, WanVideoAddLynxEmbeds, Int, Int, ImageResizeKJv2, WanVideoImageToVideoEncode, LynxInsightFaceCrop, RH_Captioner, PrimitiveNode, String Literal, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadImage]
patterns: []
missing: [String Literal, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V4_1978022050193362945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V4_1978022050193362945.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（57 个）：
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
- `easy seed`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `easy showAnything`
- `PreviewImage`
- `easy showAnything`
- `WanVideoLoraSelect`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoExtraModelSelect`
- `LoadLynxResampler` ★核心
- `WanVideoExtraModelSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `LynxEncodeFaceIP`
- `WanVideoAddLynxEmbeds`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `LynxInsightFaceCrop`
- `RH_Captioner`
- `PrimitiveNode`
- `String Literal`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`

## 知识

覆盖率 **74%**（42/57）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`Int`、`WanVideoSigmaToStep`、`WanVideoExtraModelSelect`、`LoadLynxResampler`、`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`WanVideoAddLynxEmbeds`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`LynxInsightFaceCrop`、`RH_Captioner`、`WanVideoModelLoader`、`LoadImage`

**缺卡**（3）：`String Literal`、`easy globalSeed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
