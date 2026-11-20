---
name: unknown_workflow_video_lora_sampler_589
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9305
common_nodes: [CR Prompt Text, Float, INTConstant, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveFloat, PrimitiveInt, RHHiddenNodes, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2FunVACE_高动态首尾帧_MPS+HPS_1975370725919952897.json, 视频生成/图生视频/首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json, 视频生成/图生视频/首尾帧高动态wan2.2FunVACE+MPS+HPS +SIMGA精准调度_1968343084901781506.json, 视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_589

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2FunVACE_高动态首尾帧_MPS+HPS_1975370725919952897.json、视频生成/图生视频/首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json、视频生成/图生视频/首尾帧高动态wan2.2FunVACE+MPS+HPS +SIMGA精准调度_1968343084901781506.json、视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `PrimitiveString` —— 2/4 个有
- `StringToFloatList` —— 2/4 个有
- `WanVideoEasyCache` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
