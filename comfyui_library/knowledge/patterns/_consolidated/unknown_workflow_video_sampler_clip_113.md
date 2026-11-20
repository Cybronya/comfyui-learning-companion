---
name: unknown_workflow_video_sampler_clip_113
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.761333
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Fun-V1.1-InP首尾帧(Wan2.1)_1905144833516965890.json, 视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json, 视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json, 视频生成/图生视频/Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json, 视频生成/图生视频/wan2.1_FLF2V(首尾帧图片转视频）_1914979935533105154.json, 视频生成/图生视频/wan2.1图生视频480KJ稳定版_1912043048983851010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Fun-V1.1-InP首尾帧(Wan2.1)_1905144833516965890.json、视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json、视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json、视频生成/图生视频/Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json、视频生成/图生视频/wan2.1_FLF2V(首尾帧图片转视频）_1914979935533105154.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `ImageResize+` —— 4/6 个有
- `WanVideoExperimentalArgs` —— 4/6 个有
- `ImageResizeKJ` —— 3/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/6 个有
- `GIMMVFI_interpolate` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `WanVideoVRAMManagement` —— 2/6 个有
- `CLIPLoader` —— 1/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Get resolution [Crystools]` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `WanVideoTextEmbedBridge` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
