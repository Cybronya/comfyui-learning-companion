---
key: 视频生成/图生视频/【KJ版】Wan2.2-Lightning4步首尾帧_1954845153740546050.json
name: 【KJ版】Wan2.2-Lightning4步首尾帧_1954845153740546050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954845153740546050.json
hash: fbea73a079cf8271
coverage: 0.74
learned_at: 2026-10-15 22:31:07
nodes: [JWInteger, JWInteger, LoadImage, LoadImage, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoSampler, WanVideoTextEncode, ImageConcanate, RH_LLMAPI_NODE, LoadWanVideoClipTextEncoder, CR Text, Note, WanVideoImageToVideoEncode, GetNode, GetNode, easy showAnything, WanVideoSampler, WanVideoDecode, Note, FloatToSigmas, WanVideoModelLoader, WanVideoLoraSelect, MathExpression|pysssss, StringToFloatList, MathExpression|pysssss, Primitive integer [Crystools], ImpactSwitch, ImageConcanate, ImageConcanate, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【KJ版】Wan2.2-Lightning4步首尾帧_1954845153740546050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954845153740546050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（50 个）：
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `ImageConcanate`
- `RH_LLMAPI_NODE`
- `LoadWanVideoClipTextEncoder` ★核心
- `CR Text`
- `Note`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Note`
- `FloatToSigmas`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `StringToFloatList`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `ImageConcanate`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（37/50）

**有卡**：`JWInteger`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoTextEncode`、`ImageConcanate`、`RH_LLMAPI_NODE`、`LoadWanVideoClipTextEncoder`、`CR Text`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`FloatToSigmas`、`MathExpression|pysssss`、`StringToFloatList`、`Primitive integer [Crystools]`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
