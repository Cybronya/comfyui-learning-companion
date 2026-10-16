---
key: 视频生成/图生视频/Wan2.2图生视频极致加速V5+lynx_1979417916649148417.json
name: Wan2.2图生视频极致加速V5+lynx_1979417916649148417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979417916649148417.json
hash: 65b654ca5f5a09f3
coverage: 0.785714
learned_at: 2026-10-15 22:32:23
nodes: [GetNode, SetNode, WanVideoSampler, WanVideoSampler, PrimitiveNode, VHS_VideoCombine, WanVideoTextEncode, easy seed, GetNode, Note, easy showAnything, easy showAnything, Int, PrimitiveNode, WanVideoSigmaToStep, PrimitiveNode, Int, Int, WanVideoTextEncodeCached, LynxEncodeFaceIP, RH_Captioner, LynxInsightFaceCrop, WanVideoImageToVideoEncode, WanVideoAddLynxEmbeds, easy globalSeed, WanVideoDecode, Note, PreviewImage, String Literal, LoadLynxResampler, ImageResizeKJv2, LoadImage, WanVideoScheduler, WanVideoScheduler, WanVideoSetRadialAttention, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetRadialAttention, WanVideoSetLoRAs, WanVideoSetBlockSwap, Note, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频极致加速V5+lynx_1979417916649148417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979417916649148417.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `easy seed`
- `GetNode`
- `Note`
- `easy showAnything`
- `easy showAnything`
- `Int`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `Int`
- `Int`
- `WanVideoTextEncodeCached`
- `LynxEncodeFaceIP`
- `RH_Captioner`
- `LynxInsightFaceCrop`
- `WanVideoImageToVideoEncode`
- `WanVideoAddLynxEmbeds`
- `easy globalSeed`
- `WanVideoDecode`
- `Note`
- `PreviewImage`
- `String Literal`
- `LoadLynxResampler` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSetRadialAttention`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetRadialAttention`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **79%**（44/56）

**有卡**：`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`easy seed`、`Int`、`WanVideoSigmaToStep`、`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`RH_Captioner`、`LynxInsightFaceCrop`、`WanVideoImageToVideoEncode`、`WanVideoAddLynxEmbeds`、`easy globalSeed`、`WanVideoDecode`、`String Literal`、`LoadLynxResampler`、`ImageResizeKJv2`、`LoadImage`、`WanVideoScheduler`、`WanVideoSetRadialAttention`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
