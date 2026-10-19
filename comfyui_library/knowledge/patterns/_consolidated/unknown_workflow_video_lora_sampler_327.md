---
name: unknown_workflow_video_lora_sampler_327
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.914143
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [easy seed]
members: [视频生成/图生视频/1996855253331058690.json, 视频生成/图生视频/1951528284905525250.json, 视频生成/图生视频/2059069738726285313.json, 视频生成/图生视频/1951645924265283586.json, 视频生成/图生视频/1954716501561491457.json, 视频生成/文生视频/1975384215250448386.json, 视频生成/文生视频/1966039188808396801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_327

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1996855253331058690.json、视频生成/图生视频/1951528284905525250.json、视频生成/图生视频/2059069738726285313.json、视频生成/图生视频/1951645924265283586.json、视频生成/图生视频/1954716501561491457.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `JWInteger` —— 3/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `RIFE VFI` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `ImpactInt` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `ModelScopeImageGeneration` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy promptConcat` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy seed
