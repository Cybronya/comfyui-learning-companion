---
name: unknown_workflow_video_lora_sampler_933
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9245
common_nodes: [CR Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, Int, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, RHHiddenNodes, SimpleMath+, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy anythingIndexSwitch, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json, 视频生成/文生视频/Wan2.2文生视频万相2.2+Lightx64+Fastwan+自动扩词_1950891540908548097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_933

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/SmoothMixWan22T2V2.0+SIMGA精准调度+LLM自动扩词最强文生视频_1972294263423889410.json、视频生成/文生视频/Wan2.2文生视频万相2.2+Lightx64+Fastwan+自动扩词_1950891540908548097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `SimpleMath+`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `WanVideoEasyCache` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoLoraSelectMulti` —— 1/2 个有
- `WanVideoScheduler` —— 1/2 个有
- `WanVideoSigmaToStep` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
