---
key: 视频生成/图生视频/首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json
name: 首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972900147308990465.json
hash: ed263cf406d4bc02
coverage: 0.909091
learned_at: 2026-10-15 22:32:01
nodes: [WanVideoVACEModelSelect, WanVideoExperimentalArgs, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadImage, LoadImage, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, ImageResizeKJv2, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, Int, WanVideoEnhanceAVideo, LayerUtility: PurgeVRAM V2, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, INTConstant, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoSLG, PrimitiveInt, WanVideoSigmaToStep, CreateCFGScheduleFloatList, Float, LoadWanVideoT5TextEncoder, easy anythingIndexSwitch, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, PrimitiveString, SimpleMath+, RHHiddenNodes, WanVideoTextEncode, CR Prompt Text, Note, WanVideoScheduler, WanVideoScheduler]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972900147308990465.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `WanVideoVACEModelSelect`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `Int`
- `WanVideoEnhanceAVideo`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `PrimitiveInt`
- `WanVideoSigmaToStep`
- `CreateCFGScheduleFloatList`
- `Float`
- `LoadWanVideoT5TextEncoder`
- `easy anythingIndexSwitch`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `PrimitiveString`
- `SimpleMath+`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `Note`
- `WanVideoScheduler`
- `WanVideoScheduler`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`WanVideoVACEModelSelect`、`WanVideoExperimentalArgs`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`ImageResizeKJv2`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`Int`、`WanVideoEnhanceAVideo`、`LayerUtility: PurgeVRAM V2`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoSigmaToStep`、`CreateCFGScheduleFloatList`、`Float`、`LoadWanVideoT5TextEncoder`、`easy anythingIndexSwitch`、`WanVideoLoraSelectMulti`、`SimpleMath+`、`RHHiddenNodes`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoScheduler`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
