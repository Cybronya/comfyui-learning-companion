---
name: unknown_workflow_video_sampler_vae_91
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.983667
common_nodes: [GrowMaskWithBlur, ImageCompositeMasked, LayerUtility: ColorImage V2, LayerUtility: ImageScaleByAspectRatio V2, MaskToImage, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/反推提示词/动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545.json, 平台全量/MINImax视频去水印(即梦，可灵，海螺等视频水印)_1985679416581861377.json, 平台全量/MINImax视频去水印（可自动去除移动字幕）_1935841145756770305.json, 平台全量/[书墨🛫]视频物体移除_1935770238313295873.json, 平台全量/【书墨🛫】视频移动水印去除_1935718600240263170.json, 平台全量/去除视频动态_静态水印+视频超分（无损）放大_2035400733750726658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_91

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545.json、平台全量/MINImax视频去水印(即梦，可灵，海螺等视频水印)_1985679416581861377.json、平台全量/MINImax视频去水印（可自动去除移动字幕）_1935841145756770305.json、平台全量/[书墨🛫]视频物体移除_1935770238313295873.json、平台全量/【书墨🛫】视频移动水印去除_1935718600240263170.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskToImage`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `BboxDetectorCombined_v2` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `MaskListToMaskBatch` —— 5/6 个有
- `UltralyticsDetectorProvider` —— 5/6 个有
- `LoadWanVideoT5TextEncoder` —— 4/6 个有
- `WanVideoTextEncode` —— 4/6 个有
- `WanVideoTextEncodeCached` —— 3/6 个有
- `LayerMask: LoadFlorence2Model` —— 1/6 个有
- `LayerMask: ObjectDetectorFL2` —— 1/6 个有
- `LayerMask: SAM2VideoUltra` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Primitive string multiline [Crystools]` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `VHS_SelectImages` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
