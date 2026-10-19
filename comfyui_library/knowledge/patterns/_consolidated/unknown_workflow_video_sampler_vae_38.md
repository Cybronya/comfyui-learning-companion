---
name: unknown_workflow_video_sampler_vae_38
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8268
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934577756585795586.json, 视频生成/图生视频/1934068571276533761.json, 视频生成/图生视频/1934656036613595137.json, 视频生成/图生视频/1943184080722944001.json, 视频生成/图生视频/1943311960978956289.json, 视频生成/图生视频/1934272711260856322.json, 视频生成/图生视频/1981344492861169666.json, 视频生成/图生视频/1943209482220691457.json, 视频生成/图生视频/1943184983563657218.json, 视频生成/图生视频/1934978229164023809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1934577756585795586.json、视频生成/图生视频/1934068571276533761.json、视频生成/图生视频/1934656036613595137.json、视频生成/图生视频/1943184080722944001.json、视频生成/图生视频/1943311960978956289.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 7/10 个有
- `GIMMVFI_interpolate` —— 7/10 个有
- `GetImageSizeAndCount` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `WanVideoVACEEncode` —— 7/10 个有
- `WanVideoVACEStartToEndFrame` —— 7/10 个有
- `GetImageRangeFromBatch` —— 6/10 个有
- `Int` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `WanVideoExperimentalArgs` —— 6/10 个有
- `WanVideoMagCache` —— 6/10 个有
- `WanVideoLoraSelect` —— 5/10 个有
- `WanVideoVACEModelSelect` —— 5/10 个有
- `GetNode` —— 3/10 个有
- `ImageBatchMulti` —— 3/10 个有
- `ImageSmartSharpen+` —— 3/10 个有
- `MaskBatchMulti` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `WanVideoImageToVideoEncode` —— 3/10 个有
- `CR Upscale Image` —— 2/10 个有
- `WanVideoEasyCache` —— 2/10 个有
- `WanVideoFreeInitArgs` —— 2/10 个有
- `WanVideoSetRadialAttention` —— 2/10 个有
- `FlashVSRNode` —— 1/10 个有
- `Manual XY Entry Info` —— 1/10 个有
- `PMRF` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SeedVR2` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `Video_Upscale_With_Model` —— 1/10 个有
- `WanVideoExtraModelSelect` —— 1/10 个有
- `WanVideoTeaCache` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
