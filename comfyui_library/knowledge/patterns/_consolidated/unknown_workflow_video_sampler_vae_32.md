---
name: unknown_workflow_video_sampler_vae_32
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.842545
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/分镜小工具 _ 图生视频_1940804451999629313.json, 视频生成/图生视频/B2-wan2.1 720p- MagCache加速版图生视频FusionX+NAG_1934577756585795586.json, 视频生成/图生视频/B2-wan2.1 720p图生视频FusionX+NAG_1934068571276533761.json, 视频生成/图生视频/FX超级图生视频_1934656036613595137.json, 视频生成/图生视频/FusionX VACE首尾帧视频_1943184080722944001.json, 视频生成/图生视频/MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json, 视频生成/图生视频/极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json, 视频生成/图生视频/首中尾帧万相wan2.1+VACE+FlashVSR高清丝滑变身图生视频_1981344492861169666.json, 视频生成/图生视频/🈚尾帧-kj版 图生视频（倒推首帧）_1943209482220691457.json, 视频生成/图生视频/🈚️尾帧-kj版本-wan+LIGHTX2V+VACE i2v-图生视频 尾帧倒推首帧_1943184983563657218.json, 视频生成/图生视频/🈚️首中尾帧-首尾帧插入中间帧-kj版本-wan+Lightx2v+VACE 图生视频_1934978229164023809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/分镜小工具 _ 图生视频_1940804451999629313.json、视频生成/图生视频/B2-wan2.1 720p- MagCache加速版图生视频FusionX+NAG_1934577756585795586.json、视频生成/图生视频/B2-wan2.1 720p图生视频FusionX+NAG_1934068571276533761.json、视频生成/图生视频/FX超级图生视频_1934656036613595137.json、视频生成/图生视频/FusionX VACE首尾帧视频_1943184080722944001.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ImageResizeKJ` —— 10/11 个有
- `DownloadAndLoadGIMMVFIModel` —— 7/11 个有
- `GIMMVFI_interpolate` —— 7/11 个有
- `GetImageSizeAndCount` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `WanVideoVACEEncode` —— 7/11 个有
- `WanVideoVACEStartToEndFrame` —— 7/11 个有
- `GetImageRangeFromBatch` —— 6/11 个有
- `Int` —— 6/11 个有
- `LayerUtility: PurgeVRAM V2` —— 6/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `WanVideoExperimentalArgs` —— 6/11 个有
- `WanVideoMagCache` —— 6/11 个有
- `WanVideoLoraSelect` —— 5/11 个有
- `WanVideoVACEModelSelect` —— 5/11 个有
- `WanVideoImageToVideoEncode` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `ImageBatchMulti` —— 3/11 个有
- `ImageSmartSharpen+` —— 3/11 个有
- `MaskBatchMulti` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `CR Upscale Image` —— 2/11 个有
- `WanVideoEasyCache` —— 2/11 个有
- `WanVideoFreeInitArgs` —— 2/11 个有
- `WanVideoSetRadialAttention` —— 2/11 个有
- `FlashVSRNode` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `Manual XY Entry Info` —— 1/11 个有
- `PMRF` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `SeedVR2` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有
- `Video_Upscale_With_Model` —— 1/11 个有
- `WanVideoExtraModelSelect` —— 1/11 个有
- `WanVideoTeaCache` —— 1/11 个有
- `easy imageSize` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
