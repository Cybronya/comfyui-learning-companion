---
name: unknown_workflow_video_lora_sampler_438
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9942
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1963239484815028226.json, 视频生成/图生视频/1950010533321859074.json, 视频生成/图生视频/1981177939989499906.json, 视频生成/图生视频/1950432359721123842.json, 视频生成/图生视频/1964951415749791746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_438

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1963239484815028226.json、视频生成/图生视频/1950010533321859074.json、视频生成/图生视频/1981177939989499906.json、视频生成/图生视频/1950432359721123842.json、视频生成/图生视频/1964951415749791746.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `RH_Captioner` —— 3/5 个有
- `RH_LLMAPI_NODE` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `ImageListToImageBatch` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `Primitive integer [Crystools]` —— 2/5 个有
- `easy imageBatchToImageList` —— 2/5 个有
- `easy int` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `LayerUtility: TextJoinV2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
