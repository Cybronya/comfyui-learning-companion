---
key: 视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json
name: SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json
hash: c5448a7c55764734
coverage: 0.785714
learned_at: 2026-10-10 23:05:44
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoDecode, WanVideoBlockSwap, GetImageSizeAndCount, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoVAELoader, LayerUtility: PurgeVRAM V2, Int, WanVideoExperimentalArgs, CreateCFGScheduleFloatList, Float, SimpleMath+, PrimitiveNode, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM V2, WanVideoSigmaToStep, Int, PrimitiveString, Fast Groups Bypasser (rgthree), easy anythingIndexSwitch, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, Wan22PromptSelector, VHS_VideoCombine, VHS_VideoCombine, WanVideoScheduler, WanVideoScheduler, INTConstant, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoEmptyEmbeds, WanVideoLoraSelectMulti, WanVideoTextEncode, CR Text, RHHiddenNodes, easy showAnything]
patterns: []
missing: [CR Text, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleMath+, easy anythingIndexSwitch]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `WanVideoExperimentalArgs`
- `CreateCFGScheduleFloatList`
- `Float`
- `SimpleMath+`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSigmaToStep`
- `Int`
- `PrimitiveString`
- `Fast Groups Bypasser (rgthree)`
- `easy anythingIndexSwitch`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Wan22PromptSelector`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncode`
- `CR Text`
- `RHHiddenNodes`
- `easy showAnything`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`Int`、`WanVideoExperimentalArgs`、`CreateCFGScheduleFloatList`、`Float`、`LoadWanVideoT5TextEncoder`、`WanVideoSigmaToStep`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoSampler`、`Wan22PromptSelector`、`WanVideoScheduler`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoTextEncode`、`RHHiddenNodes`

**缺卡**（5）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`easy anythingIndexSwitch`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
