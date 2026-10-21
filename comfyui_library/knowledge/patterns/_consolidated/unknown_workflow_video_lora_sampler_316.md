---
name: unknown_workflow_video_lora_sampler_316
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.995857
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1963239484815028226.json, 视频生成/图生视频/1950010533321859074.json, 视频生成/图生视频/1981177939989499906.json, 视频生成/图生视频/1950432359721123842.json, 视频生成/图生视频/1979902570766438402.json, 视频生成/图生视频/1953038544099020801.json, 视频生成/图生视频/1964951415749791746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_316

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1963239484815028226.json、视频生成/图生视频/1950010533321859074.json、视频生成/图生视频/1981177939989499906.json、视频生成/图生视频/1950432359721123842.json、视频生成/图生视频/1979902570766438402.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
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
- `MathExpression|pysssss` —— 5/7 个有
- `ImageListToImageBatch` —— 4/7 个有
- `ImpactInt` —— 4/7 个有
- `Primitive integer [Crystools]` —— 4/7 个有
- `easy imageBatchToImageList` —— 4/7 个有
- `GetImageSizeAndCount` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `easy int` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `LayerUtility: TextJoinV2` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
