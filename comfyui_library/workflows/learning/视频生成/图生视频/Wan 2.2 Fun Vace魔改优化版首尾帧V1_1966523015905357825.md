---
key: 视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json
name: Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json
hash: c1c79bb60134e4c1
coverage: 0.974359
learned_at: 2026-10-15 22:31:38
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ImageResizeKJv2, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoLoraSelect, LoadImage, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoScheduler, WanVideoScheduler, VHS_VideoCombine, StringToFloatList, WanVideoDecode, LoadImage, ImageConcatMulti, ColorMatch, VHS_VideoCombine, INTConstant, Float, WanVideoSigmaToStep, PrimitiveInt, StringToFloatList, INTConstant, WanVideoLoraSelect, WanVideoTorchCompileSettings, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966523015905357825.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `VHS_VideoCombine`
- `StringToFloatList`
- `WanVideoDecode`
- `LoadImage`
- `ImageConcatMulti`
- `ColorMatch`
- `VHS_VideoCombine`
- `INTConstant`
- `Float`
- `WanVideoSigmaToStep`
- `PrimitiveInt`
- `StringToFloatList`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `CR Prompt Text`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoScheduler`、`VHS_VideoCombine`、`StringToFloatList`、`WanVideoDecode`、`ImageConcatMulti`、`ColorMatch`、`INTConstant`、`Float`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`CR Prompt Text`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
