---
name: unknown_workflow_video_sampler_vae_71
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.777143
common_nodes: [ImageConcatMulti, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1935507618146484226.json, 视频生成/图生视频/1935607588300193793.json, 视频生成/图生视频/1935586332242530306.json, 视频生成/图生视频/2055192187125682177.json, 视频生成/图生视频/1935509475614707714.json, 视频生成/图生视频/1934523459177250818.json, 视频生成/文生视频/1938855885659627522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_71

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1935507618146484226.json、视频生成/图生视频/1935607588300193793.json、视频生成/图生视频/1935586332242530306.json、视频生成/图生视频/2055192187125682177.json、视频生成/图生视频/1935509475614707714.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageConcatMulti`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 6/7 个有
- `CR Text` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `JWInteger` —— 6/7 个有
- `MathExpression|pysssss` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `WanVideoClipVisionEncode` —— 6/7 个有
- `WanVideoExperimentalArgs` —— 6/7 个有
- `WanVideoImageToVideoEncode` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoSLG` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `easy imageRemBg` —— 6/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `ImageConcanate` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `AddLabel` —— 2/7 个有
- `EmptyImage` —— 2/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `easy imageScaleDownToSize` —— 2/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `InspyrenetRembg` —— 1/7 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/7 个有
- `PDIMAGE_LongerSize` —— 1/7 个有
- `WanVideoEnhanceAVideo` —— 1/7 个有
- `WanVideoVACEEncode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
