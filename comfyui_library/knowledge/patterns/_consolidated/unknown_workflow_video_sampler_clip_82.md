---
name: unknown_workflow_video_sampler_clip_82
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.732
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1909949777759666177.json, 视频生成/图生视频/1919985178293239809.json, 视频生成/图生视频/1906320189389213697.json, 视频生成/图生视频/1928288843513118721.json, 视频生成/图生视频/1930856714751684610.json, 视频生成/图生视频/1904901928008994817.json, 视频生成/图生视频/1912043048983851010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1909949777759666177.json、视频生成/图生视频/1919985178293239809.json、视频生成/图生视频/1906320189389213697.json、视频生成/图生视频/1928288843513118721.json、视频生成/图生视频/1930856714751684610.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
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
- `AddLabel` —— 6/7 个有
- `CLIPLoader` —— 6/7 个有
- `CLIPTextEncode` —— 6/7 个有
- `GetImageSizeAndCount` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `ImageResize+` —— 6/7 个有
- `WanVideoExperimentalArgs` —— 6/7 个有
- `WanVideoTextEmbedBridge` —— 6/7 个有
- `CLIPVisionLoader` —— 5/7 个有
- `EmptyImage` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 4/7 个有
- `WanVideoVRAMManagement` —— 4/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `WanVideoEnhanceAVideo` —— 2/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `Get resolution [Crystools]` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `JWImageResizeByLongerSide` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
