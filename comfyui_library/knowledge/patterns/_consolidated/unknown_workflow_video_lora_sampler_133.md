---
name: unknown_workflow_video_lora_sampler_133
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.797333
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [CR Prompt Text]
members: [图片生成/文生图/(KJ版)Wan2.2 文生视频加速版V1（高级镜头运动）_1950219384603197442.json, 图片生成/文生图/1950229173782667265.json, 视频生成/图生视频/1950186803727876098.json, 视频生成/图生视频/1950195066095714306.json, 视频生成/图生视频/1951706628657721345.json, 视频生成/图生视频/1952379981454356482.json, 视频生成/图生视频/1958329812857327618.json, 视频生成/图生视频/1950822532939186177.json, 视频生成/图生视频/1950805737444417537.json, 视频生成/图生视频/1950560356596961282.json, 视频生成/图生视频/1958716775745667074.json, 视频生成/图生视频/1976954244421046273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_133

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/(KJ版)Wan2.2 文生视频加速版V1（高级镜头运动）_1950219384603197442.json、图片生成/文生图/1950229173782667265.json、视频生成/图生视频/1950186803727876098.json、视频生成/图生视频/1950195066095714306.json、视频生成/图生视频/1951706628657721345.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 11/12 个有
- `INTConstant` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `GetImageSizeAndCount` —— 9/12 个有
- `JWInteger` —— 9/12 个有
- `LoadImage` —— 8/12 个有
- `WanVideoImageToVideoEncode` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/12 个有
- `ImageFromBatch+` —— 5/12 个有
- `LayerUtility: PurgeVRAM` —— 5/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `GetNode` —— 4/12 个有
- `SetNode` —— 4/12 个有
- `WanVideoEmptyEmbeds` —— 4/12 个有
- `ImageResizeKJv2` —— 3/12 个有
- `WanVideoEasyCache` —— 3/12 个有
- `Int` —— 2/12 个有
- `MathExpression|pysssss` —— 2/12 个有
- `PreviewImage` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `Seed_` —— 1/12 个有
- `easy bookmark` —— 1/12 个有
- `easy imageSize` —— 1/12 个有
- `easy positive` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
