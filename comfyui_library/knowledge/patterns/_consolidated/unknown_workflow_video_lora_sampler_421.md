---
name: unknown_workflow_video_lora_sampler_421
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.89
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json, 视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json, 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版_1950128875525332993.json, 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版非常逼真目前最牛_1950206171439390721.json, 视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_421

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json、视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json、视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版_1950128875525332993.json、视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版非常逼真目前最牛_1950206171439390721.json、视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/5 个有
- `PreViewVideo` —— 3/5 个有
- `Primitive integer [Crystools]` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `WanVideoEmptyEmbeds` —— 3/5 个有
- `DF_Integer` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `WanVideoImageToVideoEncode` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
