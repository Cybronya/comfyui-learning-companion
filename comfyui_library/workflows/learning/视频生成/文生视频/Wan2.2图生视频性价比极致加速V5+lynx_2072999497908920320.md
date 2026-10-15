---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_2072999497908920320.json
name: Wan2.2图生视频性价比极致加速V5+lynx_2072999497908920320
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_2072999497908920320.json
hash: 188f432a8e1d54d5
coverage: 0.785714
learned_at: 2026-10-15 22:47:14
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, WanVideoModelLoader, easy seed, WanVideoTorchCompileSettings, easy globalSeed, GetNode, LoadWanVideoT5TextEncoder, Note, easy showAnything, PreviewImage, easy showAnything, WanVideoModelLoader, Int, PrimitiveNode, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, Int, Int, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoTextEncodeCached, LynxEncodeFaceIP, RH_Captioner, LoadLynxResampler, LynxInsightFaceCrop, WanVideoImageToVideoEncode, ImageResizeKJv2, WanVideoAddLynxEmbeds, WanVideoVAELoader, LoadImage, String Literal, WanVideoExtraModelSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_2072999497908920320.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_2072999497908920320.json`

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

覆盖率 **79%**（44/56）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`easy seed`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`LoadWanVideoT5TextEncoder`、`Int`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`RH_Captioner`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoAddLynxEmbeds`、`WanVideoVAELoader`、`LoadImage`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
