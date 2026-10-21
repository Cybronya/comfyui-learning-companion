---
name: unknown_workflow_video_lora_sampler_402
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9026
common_nodes: [CR Prompt Text, Float, INTConstant, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveFloat, PrimitiveInt, RHHiddenNodes, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, SimpleMath+, easy anythingIndexSwitch, CR Prompt Text]
members: [视频生成/图生视频/1977975025720512514.json, 视频生成/图生视频/1975370725919952897.json, 视频生成/图生视频/1972900147308990465.json, 视频生成/图生视频/1968343084901781506.json, 视频生成/文生视频/1977975025720512514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_402

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1977975025720512514.json、视频生成/图生视频/1975370725919952897.json、视频生成/图生视频/1972900147308990465.json、视频生成/图生视频/1968343084901781506.json、视频生成/文生视频/1977975025720512514.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 3/5 个有
- `PrimitiveString` —— 3/5 个有
- `easy anythingIndexSwitch` —— 3/5 个有
- `StringToFloatList` —— 2/5 个有
- `WanVideoEasyCache` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM V2、SimpleMath+、easy anythingIndexSwitch、CR Prompt Text
