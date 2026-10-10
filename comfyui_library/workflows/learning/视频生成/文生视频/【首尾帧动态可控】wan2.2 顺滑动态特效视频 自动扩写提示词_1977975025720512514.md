---
key: 视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json
name: 【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json
hash: f8c1587e3afdeb24
coverage: 0.790698
learned_at: 2026-10-10 23:10:22
nodes: [WanVideoVACEModelSelect, WanVideoExperimentalArgs, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, ImageResizeKJv2, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, Int, WanVideoEnhanceAVideo, LayerUtility: PurgeVRAM V2, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, INTConstant, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoSLG, PrimitiveInt, WanVideoSigmaToStep, CreateCFGScheduleFloatList, Float, LoadWanVideoT5TextEncoder, easy anythingIndexSwitch, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, PrimitiveString, SimpleMath+, RHHiddenNodes, Note, WanVideoScheduler, WanVideoScheduler, LoadImage, LoadImage, WanVideoTextEncode, CR Prompt Text]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, SimpleMath+, easy anythingIndexSwitch, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `WanVideoVACEModelSelect`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
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
- `Note`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `CR Prompt Text`

## 知识

覆盖率 **79%**（34/43）

**有卡**：`WanVideoVACEModelSelect`、`WanVideoExperimentalArgs`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`ImageResizeKJv2`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`Int`、`WanVideoEnhanceAVideo`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoSigmaToStep`、`CreateCFGScheduleFloatList`、`Float`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelectMulti`、`RHHiddenNodes`、`WanVideoScheduler`、`LoadImage`、`WanVideoTextEncode`

**缺卡**（5）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`easy anythingIndexSwitch`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
