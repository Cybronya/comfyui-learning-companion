---
name: unknown_workflow_video_lora_sampler_70
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.710778
common_nodes: [GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1995877090840961026.json, 视频生成/图生视频/2009487877079568385.json, 视频生成/图生视频/2058467606604111873.json, 视频生成/图生视频/2062267802035253249.json, 视频生成/图生视频/2079497212211585026.json, 视频生成/图生视频/2058626047352070146.json, 视频生成/图生视频/1996439442132975617.json, 视频生成/图生视频/2041796686720274433.json, 视频生成/图生视频/2042065496551464962.json, 视频生成/图生视频/2042132307506634753.json, 视频生成/图生视频/2043214843913707521.json, 视频生成/图生视频/2043550053435969538.json, 视频生成/图生视频/2043574604777656322.json, 视频生成/图生视频/2043973328846725122.json, 视频生成/图生视频/2045029868080996354.json, 视频生成/图生视频/2045827374817742849.json, 视频生成/图生视频/1995843794539098113.json, 视频生成/图生视频/2009443481458057217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1995877090840961026.json、视频生成/图生视频/2009487877079568385.json、视频生成/图生视频/2058467606604111873.json、视频生成/图生视频/2062267802035253249.json、视频生成/图生视频/2079497212211585026.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 18 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 17/18 个有
- `GetImageSizeAndCount` —— 17/18 个有
- `OnnxDetectionModelLoader` —— 17/18 个有
- `WanVideoContextOptions` —— 17/18 个有
- `WanVideoLoraSelect` —— 17/18 个有
- `WanVideoScheduler` —— 17/18 个有
- `WanVideoBlockSwap` —— 16/18 个有
- `WanVideoSetBlockSwap` —— 16/18 个有
- `ImageConcatMulti` —— 15/18 个有
- `PreviewImage` —— 15/18 个有
- `PoseDetectionOneToAllAnimation` —— 14/18 个有
- `CR Prompt Text` —— 12/18 个有
- `DrawViTPose` —— 4/18 个有
- `PoseAndFaceDetection` —— 4/18 个有
- `easy int` —— 4/18 个有
- `SimpleMath+` —— 3/18 个有
- `WanVideoTorchCompileSettings` —— 3/18 个有
- `CR Text` —— 2/18 个有
- `CR Text Concatenate` —— 2/18 个有
- `ImpactInt` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `DF_Int_to_Float` —— 1/18 个有
- `INTConstant` —— 1/18 个有
- `MathExpression|pysssss` —— 1/18 个有
- `Note Plus (mtb)` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有
- `VHS_VideoInfo` —— 1/18 个有
- `WanVideoImageResizeToClosest` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有
- `easy clearCacheAll` —— 1/18 个有
- `easy positive` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
