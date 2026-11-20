---
name: unknown_workflow_video_sampler_vae_50
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6632
common_nodes: [Any Switch (rgthree), DownloadAndLoadFlorence2Model, Florence2Run, GetImageRangeFromBatch, GetNode, GrowMaskWithBlur, ImageCompositeMasked, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, SetNode, SolidMask, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/最新视频去水印（三种方案任意切换）_1935175040575143938.json, 平台全量/最新视频去水印（三种方案任意切换）_1977342122468757506.json, 平台全量/极简-视频去文字水印_1951207757150101505.json, 平台全量/视频去字幕和水印_2041029377902780417.json, 平台全量/视频去字幕和水印_2046062618506432513.json, 平台全量/视频去字幕和水印_2048575374195433473.json, 平台全量/视频去水印（minimax-remover）_1938080032948404226.json, 平台全量/视频去水印（minimax-remover）_1992158027252035586.json, 平台全量/视频去除移动文字 水印_2029033243114217473.json, 数字人/数字人/视频去字幕和水印_2042434276649603073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_50

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/最新视频去水印（三种方案任意切换）_1935175040575143938.json、平台全量/最新视频去水印（三种方案任意切换）_1977342122468757506.json、平台全量/极简-视频去文字水印_1951207757150101505.json、平台全量/视频去字幕和水印_2041029377902780417.json、平台全量/视频去字幕和水印_2046062618506432513.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 10 个 workflow 都包含：
- `Any Switch (rgthree)`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `SetNode`
- `SolidMask`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 8/10 个有
- `JWInteger` —— 8/10 个有
- `PointsEditor` —— 8/10 个有
- `Sam2Segmentation` —— 8/10 个有
- `easy compare` —— 8/10 个有
- `easy ifElse` —— 8/10 个有
- `easy imageScaleDownToSize` —— 8/10 个有
- `LoadImage` —— 6/10 个有
- `PreviewBridge` —— 6/10 个有
- `SaveImage` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `BBoxesToSAM2` —— 2/10 个有
- `DownloadAndLoadQwenModel` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `LayerMask: LoadSAM2Model` —— 2/10 个有
- `LayerMask: MaskPreview` —— 2/10 个有
- `LayerMask: SAM2UltraV2` —— 2/10 个有
- `Mask Fill Holes` —— 2/10 个有
- `QwenVLDetection` —— 2/10 个有
- `easy batchAnything` —— 2/10 个有
- `easy clearCacheAll` —— 2/10 个有
- `easy forLoopEnd` —— 2/10 个有
- `easy forLoopStart` —— 2/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
