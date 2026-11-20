---
name: unknown_workflow_video_lora_sampler_929
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.546333
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJ, ImageSmartSharpen+, Int, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveStringMultiline, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🈚尾帧-kj版 图生视频（倒推首帧）_1943209482220691457.json, 视频生成/图生视频/🈚️尾帧-kj版本-wan+LIGHTX2V+VACE i2v-图生视频 尾帧倒推首帧_1943184983563657218.json, 视频生成/图生视频/🈚️首中尾帧-首尾帧插入中间帧-kj版本-wan+Lightx2v+VACE 图生视频_1934978229164023809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_929

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/🈚尾帧-kj版 图生视频（倒推首帧）_1943209482220691457.json、视频生成/图生视频/🈚️尾帧-kj版本-wan+LIGHTX2V+VACE i2v-图生视频 尾帧倒推首帧_1943184983563657218.json、视频生成/图生视频/🈚️首中尾帧-首尾帧插入中间帧-kj版本-wan+Lightx2v+VACE 图生视频_1934978229164023809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `ImageSmartSharpen+`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 2/3 个有
- `WanVideoEasyCache` —— 2/3 个有
- `WanVideoFreeInitArgs` —— 2/3 个有
- `WanVideoSetRadialAttention` —— 2/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `Manual XY Entry Info` —— 1/3 个有
- `MaskBatchMulti` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `Video_Upscale_With_Model` —— 1/3 个有
- `WanVideoMagCache` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
