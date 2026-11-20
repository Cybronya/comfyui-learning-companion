---
name: unknown_workflow_video_sampler_vae_176
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.635333
common_nodes: [DownloadAndLoadFlorence2Model, Florence2Run, GetImageSizeAndCount, GrowMaskWithBlur, ImageCompositeMasked, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskToImage, Primitive integer [Crystools], SolidMask, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy clearCacheAll, easy imageSize, easy showAnything]
problems: []
missing: []
members: [平台全量/MiniMax-Remover去除视频移动水印_1935890656063909890.json, 平台全量/视频一键去水印【AI小王子】_2076839296698507265.json, 平台全量/视频移动水印擦除_MiniMax-Remover多套方法全集_1935357461597716482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_176

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/MiniMax-Remover去除视频移动水印_1935890656063909890.json、平台全量/视频一键去水印【AI小王子】_2076839296698507265.json、平台全量/视频移动水印擦除_MiniMax-Remover多套方法全集_1935357461597716482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `Primitive integer [Crystools]`
- `SolidMask`
- `Text Multiline`
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
- `easy clearCacheAll`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `BBoxesToSAM2` —— 1/3 个有
- `DownloadAndLoadQwenModel` —— 1/3 个有
- `DownloadAndLoadSAM2Model` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageBatchToList+` —— 1/3 个有
- `LayerMask: SAM2Ultra` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PointsEditor` —— 1/3 个有
- `PreviewBridge` —— 1/3 个有
- `QwenVLDetection` —— 1/3 个有
- `Sam2Segmentation` —— 1/3 个有
- `VHS_DuplicateMasks` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
