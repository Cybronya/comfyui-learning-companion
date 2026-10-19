---
name: unknown_workflow_video_lora_sampler_522
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96325
common_nodes: [CreateCFGScheduleFloatList, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950400282711736322.json, 视频生成/图生视频/1950132208273154049.json, 视频生成/图生视频/1979902570766438402.json, 视频生成/图生视频/1953038544099020801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_522

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1950400282711736322.json、视频生成/图生视频/1950132208273154049.json、视频生成/图生视频/1979902570766438402.json、视频生成/图生视频/1953038544099020801.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Primitive integer [Crystools]` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `ImageListToImageBatch` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `easy imageBatchToImageList` —— 2/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `DF_Integer` —— 1/4 个有
- `PreViewVideo` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
