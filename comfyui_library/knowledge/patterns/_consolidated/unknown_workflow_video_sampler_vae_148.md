---
name: unknown_workflow_video_sampler_vae_148
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.87625
common_nodes: [DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ImageFromBatch+, ImageRepeat, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_MergeImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/电商生成场景类似的视频_1929385061676912642.json, 平台全量/直播真实视频转动漫_1948589664174256129.json, 视频生成/图生视频/直播让图片跳舞_1926646859241263106.json, 视频生成/图生视频/进阶版直播真实视频转动漫_1948659044000104450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/电商生成场景类似的视频_1929385061676912642.json、平台全量/直播真实视频转动漫_1948589664174256129.json、视频生成/图生视频/直播让图片跳舞_1926646859241263106.json、视频生成/图生视频/进阶版直播真实视频转动漫_1948659044000104450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `ImageFromBatch+`
- `ImageRepeat`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoFreeInitArgs` —— 2/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
