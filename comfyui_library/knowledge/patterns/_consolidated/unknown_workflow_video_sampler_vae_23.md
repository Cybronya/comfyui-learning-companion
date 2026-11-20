---
name: unknown_workflow_video_sampler_vae_23
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.928923
common_nodes: [BboxDetectorCombined_v2, Fast Groups Bypasser (rgthree), GrowMaskWithBlur, ImageCompositeMasked, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskToImage, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/反推提示词/57shipinqushuiyin_2051294749801361410.json, 平台全量/WanVideo MiniMax Remover视频全自动去水印_1961258734213382145.json, 平台全量/【RICK】MinimaxRemover视频水印去除_1994744723745218562.json, 平台全量/最强无痕迹视频水印去除即梦 、可灵、豆包、全能视频V3 通用版_1948618194949943297.json, 平台全量/最强无痕迹视频水印去除即梦 、可灵、豆包、全能视频V3 通用版_2022180268001464322.json, 平台全量/视频去水印-横竖屏-通用版_2109538465628123137.json, 平台全量/视频去水印横竖屏通用版_2107823836732416001.json, 平台全量/视频去水印横竖屏通用版工作流_2039658831076139010.json, 平台全量/视频去水印横竖屏通用版工作流_2103075740681064450.json, 平台全量/视频去水印横竖屏通用版工作流_2103089629216985089.json, 平台全量/视频水印去除即梦 、可灵、豆包、全能视频V3 通用版（楚门的ai世界）_1947963403324272642.json, 平台全量/视频水印去除横竖屏通用版工作流_2039553479328403457.json, 数字人/数字人/视频水印去除即梦 、可灵、豆包、全能视频V3 通用版（楚门的ai世界）11111111111_1990403314384867330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/57shipinqushuiyin_2051294749801361410.json、平台全量/WanVideo MiniMax Remover视频全自动去水印_1961258734213382145.json、平台全量/【RICK】MinimaxRemover视频水印去除_1994744723745218562.json、平台全量/最强无痕迹视频水印去除即梦 、可灵、豆包、全能视频V3 通用版_1948618194949943297.json、平台全量/最强无痕迹视频水印去除即梦 、可灵、豆包、全能视频V3 通用版_2022180268001464322.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `Fast Groups Bypasser (rgthree)`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `SolidMask`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 12/13 个有
- `VHS_VideoCombine` —— 12/13 个有
- `easy cleanGpuUsed` —— 12/13 个有
- `GetImageRangeFromBatch` —— 11/13 个有
- `ImageConcatMulti` —— 11/13 个有
- `ImageListToBatch+` —— 11/13 个有
- `ImageToMask` —— 11/13 个有
- `PreviewBridge` —— 11/13 个有
- `VHS_DuplicateMasks` —— 11/13 个有
- `DiffuEraserLoader` —— 10/13 个有
- `DiffuEraserSampler` —— 10/13 个有
- `MaskListToMaskBatch` —— 2/13 个有
- `CreateVideo` —— 1/13 个有
- `DownloadAndLoadSAM2Model` —— 1/13 个有
- `LoadImage` —— 1/13 个有
- `PointsEditor` —— 1/13 个有
- `Sam2Segmentation` —— 1/13 个有
- `SaveVideo` —— 1/13 个有
- `WanVideoBlockSwap` —— 1/13 个有
- `WanVideoTorchCompileSettings` —— 1/13 个有
- `easy showAnything` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
