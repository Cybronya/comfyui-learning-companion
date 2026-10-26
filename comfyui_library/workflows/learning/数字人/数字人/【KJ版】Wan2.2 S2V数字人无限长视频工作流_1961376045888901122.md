---
key: 数字人/数字人/【KJ版】Wan2.2 S2V数字人无限长视频工作流_1961376045888901122.json
name: 【KJ版】Wan2.2 S2V数字人无限长视频工作流_1961376045888901122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【KJ版】Wan2.2 S2V数字人无限长视频工作流_1961376045888901122.json
hash: 1d337d0dd2f9a762
coverage: 0.767442
learned_at: 2026-10-26 01:59:46
nodes: [WanVideoVAELoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, GetNode, LoadImage, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, JWInteger, AudioCrop, easy showAnything, RH_LLMAPI_NODE, JWIntegerToString, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, AudioSeparation, LoadAudio, ImpactSwitch, CR Text, Audio Duration (mtb), PreviewAudio, WanVideoSampler, GetNode, GetNode, WanVideoDecode, VHS_VideoCombine, ImageFromBatch+, MathExpression|pysssss, PreviewAudio, WanVideoTextEncode, AudioEncoderEncode, AudioEncoderLoader, WanVideoEncode, WanVideoEmptyEmbeds, GetNode, WanVideoAddS2VEmbeds, WanVideoContextOptions, JWInteger]
patterns: []
missing: []
---

# 数字人/数字人/【KJ版】Wan2.2 S2V数字人无限长视频工作流_1961376045888901122.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【KJ版】Wan2.2 S2V数字人无限长视频工作流_1961376045888901122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `LoadImage`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `JWInteger`
- `AudioCrop`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `JWIntegerToString`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `AudioSeparation`
- `LoadAudio`
- `ImpactSwitch`
- `CR Text`
- `Audio Duration (mtb)`
- `PreviewAudio`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `MathExpression|pysssss`
- `PreviewAudio`
- `WanVideoTextEncode`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoAddS2VEmbeds`
- `WanVideoContextOptions`
- `JWInteger`

## 知识

覆盖率 **77%**（33/43）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`JWInteger`、`AudioCrop`、`RH_LLMAPI_NODE`、`JWIntegerToString`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`AudioSeparation`、`LoadAudio`、`CR Text`、`Audio Duration (mtb)`、`PreviewAudio`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageFromBatch+`、`MathExpression|pysssss`、`WanVideoTextEncode`、`AudioEncoderEncode`、`AudioEncoderLoader`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`WanVideoContextOptions`

**用到的条目**：LoadImage、WanVideoSampler、AudioEncoderLoader、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、AudioEncoderEncode
