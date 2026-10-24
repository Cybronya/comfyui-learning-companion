---
name: unknown_workflow_video_lora_sampler_537
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.784
common_nodes: [DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/翻跟头踢再过头万相图生视60---------_1942408642337386497.json, 视频生成/图生视频/跳连踢头万相图生视68_1942291396009332737.json, 视频生成/图生视频/踢飞001万相图生视60_1942258694929453057.json, 视频生成/文生视频/wan2.1 美女模特环绕360镜头_1948183432305225730.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_537

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/翻跟头踢再过头万相图生视60---------_1942408642337386497.json、视频生成/图生视频/跳连踢头万相图生视68_1942291396009332737.json、视频生成/图生视频/踢飞001万相图生视60_1942258694929453057.json、视频生成/文生视频/wan2.1 美女模特环绕360镜头_1948183432305225730.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/4 个有
- `LatentSyncNode` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VideoLengthAdjuster` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `ImageScaleToMegapixels` —— 2/4 个有
- `ImageSmartSharpen+` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `InspyrenetRembg` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
