---
key: 视频生成/图生视频/【KJ版】Wan2.2-8步首尾帧_1954815922643058689.json
name: 【KJ版】Wan2.2-8步首尾帧_1954815922643058689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954815922643058689.json
hash: e25a13b0793144fc
coverage: 0.764706
learned_at: 2026-10-15 22:31:07
nodes: [JWInteger, JWInteger, LoadImage, LoadImage, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, WanVideoClipVisionEncode, GetNode, GetNode, ImageConcanate, SetNode, RH_LLMAPI_NODE, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, LoadWanVideoClipTextEncoder, VHS_VideoCombine, VHS_VideoCombine, CR Text, Note, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncode, GetNode, GetNode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoDecode, MathExpression|pysssss, Primitive integer [Crystools], ImpactSwitch, VHS_VideoCombine, easy showAnything, ImageConcanate, LayerUtility: PurgeVRAM V2, ImageConcanate, CreateCFGScheduleFloatList, MathExpression|pysssss]
patterns: []
missing: []
---

# 视频生成/图生视频/【KJ版】Wan2.2-8步首尾帧_1954815922643058689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954815922643058689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（51 个）：
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `SetNode`
- `RH_LLMAPI_NODE`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `LoadWanVideoClipTextEncoder` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `Note`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `easy showAnything`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `CreateCFGScheduleFloatList`
- `MathExpression|pysssss`

## 知识

覆盖率 **76%**（39/51）

**有卡**：`JWInteger`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`ImageConcanate`、`RH_LLMAPI_NODE`、`WanVideoLoraSelect`、`WanVideoSampler`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`、`CR Text`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`LayerUtility: PurgeVRAM V2`、`CreateCFGScheduleFloatList`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
