---
name: unknown_workflow_video_lora_sampler_498
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9706
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json, 视频生成/图生视频/Wan2.2动态壁纸生成器_1963239484815028226.json, 视频生成/图生视频/【动态壁纸】Wan2.2动态壁纸生成器 一键自动循环壁纸MAX版高清_1981177939989499906.json, 视频生成/图生视频/图生视频（人物展示、产品宣传与创意设计）_1979902570766438402.json, 视频生成/图生视频/最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_498

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json、视频生成/图生视频/Wan2.2动态壁纸生成器_1963239484815028226.json、视频生成/图生视频/【动态壁纸】Wan2.2动态壁纸生成器 一键自动循环壁纸MAX版高清_1981177939989499906.json、视频生成/图生视频/图生视频（人物展示、产品宣传与创意设计）_1979902570766438402.json、视频生成/图生视频/最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `ImageListToImageBatch` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `Primitive integer [Crystools]` —— 4/5 个有
- `easy imageBatchToImageList` —— 4/5 个有
- `RH_Captioner` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `DF_Integer` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
