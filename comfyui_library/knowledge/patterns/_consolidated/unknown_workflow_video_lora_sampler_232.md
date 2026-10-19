---
name: unknown_workflow_video_lora_sampler_232
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.891889
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2017911981818253314.json, 视频生成/图生视频/2046206194833952769.json, 视频生成/图生视频/1955263438596423682.json, 视频生成/图生视频/2014217620324618242.json, 视频生成/图生视频/1950145303941922817.json, 视频生成/图生视频/1963873192061521922.json, 视频生成/图生视频/1949391348926971905.json, 视频生成/图生视频/1958716775745667074.json, 视频生成/图生视频/1954808332802506754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_232

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2017911981818253314.json、视频生成/图生视频/2046206194833952769.json、视频生成/图生视频/1955263438596423682.json、视频生成/图生视频/2014217620324618242.json、视频生成/图生视频/1950145303941922817.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `GetImageSizeAndCount` —— 6/9 个有
- `WanVideoSetBlockSwap` —— 6/9 个有
- `WanVideoSetLoRAs` —— 6/9 个有
- `INTConstant` —— 5/9 个有
- `LayerUtility: PurgeVRAM` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `JWInteger` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `GetImageSize` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `InversionDemoLazyIndexSwitch` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `Random Number` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
