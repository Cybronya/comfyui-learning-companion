---
name: unknown_workflow_video_sampler_clip_159
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.737
common_nodes: [ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json, 视频生成/图生视频/Wan2.1_首尾帧视频_kijai_1925042033008779266.json, 视频生成/图生视频/Wan首尾帧视频生成-kijai版_1904901928008994817.json, 视频生成/图生视频/wan2.1图生视频480KJ稳定版_1912043048983851010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json、视频生成/图生视频/Wan2.1_首尾帧视频_kijai_1925042033008779266.json、视频生成/图生视频/Wan首尾帧视频生成-kijai版_1904901928008994817.json、视频生成/图生视频/wan2.1图生视频480KJ稳定版_1912043048983851010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageResize+`
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
- `CLIPLoader` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoTextEmbedBridge` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `WanVideoVRAMManagement` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `Get resolution [Crystools]` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
