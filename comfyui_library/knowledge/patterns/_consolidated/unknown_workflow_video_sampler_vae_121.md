---
name: unknown_workflow_video_sampler_vae_121
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.679
common_nodes: [AddLabel, DownloadAndLoadFlorence2Model, Florence2Run, GetImageRangeFromBatch, LoadWanVideoT5TextEncoder, PreviewImage, ReCamMasterPoseVisualizer, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoReCamMasterCameraEmbed, WanVideoReCamMasterDefaultCamera, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WidgetToString]
problems: []
missing: []
members: [视频生成/图生视频/1915621811168677889.json, 视频生成/图生视频/1911342097738465281.json, 视频生成/图生视频/1911957387463356417.json, 视频生成/图生视频/1912793596637184001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_121

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1915621811168677889.json、视频生成/图生视频/1911342097738465281.json、视频生成/图生视频/1911957387463356417.json、视频生成/图生视频/1912793596637184001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GetImageRangeFromBatch`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `ReCamMasterPoseVisualizer`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoReCamMasterCameraEmbed`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WidgetToString`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoVRAMManagement` —— 3/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有
- `WanVideoTextEmbedBridge` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
