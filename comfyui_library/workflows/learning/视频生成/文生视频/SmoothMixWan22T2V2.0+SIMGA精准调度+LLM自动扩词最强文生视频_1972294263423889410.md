---
key: 视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json
name: SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json
hash: c5448a7c55764734
coverage: 0.904762
learned_at: 2026-10-15 22:47:01
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoDecode, WanVideoBlockSwap, GetImageSizeAndCount, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoVAELoader, LayerUtility: PurgeVRAM V2, Int, WanVideoExperimentalArgs, CreateCFGScheduleFloatList, Float, SimpleMath+, PrimitiveNode, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM V2, WanVideoSigmaToStep, Int, PrimitiveString, Fast Groups Bypasser (rgthree), easy anythingIndexSwitch, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, Wan22PromptSelector, VHS_VideoCombine, VHS_VideoCombine, WanVideoScheduler, WanVideoScheduler, INTConstant, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoEmptyEmbeds, WanVideoLoraSelectMulti, WanVideoTextEncode, CR Text, RHHiddenNodes, easy showAnything]
patterns: []
missing: []
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

覆盖率 **90%**（38/42）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM V2`、`Int`、`WanVideoExperimentalArgs`、`CreateCFGScheduleFloatList`、`Float`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoSigmaToStep`、`easy anythingIndexSwitch`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoSampler`、`Wan22PromptSelector`、`WanVideoScheduler`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoTextEncode`、`CR Text`、`RHHiddenNodes`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs、WanVideoLoraSelectMulti
