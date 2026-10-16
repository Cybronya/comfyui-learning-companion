---
key: 视频生成/文生视频/Wan2.2文生视频万相2.2+Lightx64+Fastwan+自动扩词_1950891540908548097.json
name: Wan2.2文生视频万相2.2+Lightx64+Fastwan+自动扩词_1950891540908548097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950891540908548097.json
hash: 92e14a55c5104027
coverage: 0.944444
learned_at: 2026-10-15 22:43:37
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoBlockSwap, GetImageSizeAndCount, WanVideoEasyCache, WanVideoSampler, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoSampler, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, CreateCFGScheduleFloatList, INTConstant, INTConstant, Wan22PromptSelector, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, PrimitiveNode, CR Text, Int, Int, Int, SimpleMath+, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, RHHiddenNodes, WanVideoTextEncode, easy anythingIndexSwitch, easy showAnything]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频万相2.2+Lightx64+Fastwan+自动扩词_1950891540908548097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950891540908548097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoEasyCache`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `Wan22PromptSelector`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveNode`
- `CR Text`
- `Int`
- `Int`
- `Int`
- `SimpleMath+`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `easy anythingIndexSwitch`
- `easy showAnything`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoEasyCache`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`INTConstant`、`Wan22PromptSelector`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CR Text`、`Int`、`SimpleMath+`、`WanVideoLoraSelect`、`RHHiddenNodes`、`WanVideoTextEncode`、`easy anythingIndexSwitch`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
