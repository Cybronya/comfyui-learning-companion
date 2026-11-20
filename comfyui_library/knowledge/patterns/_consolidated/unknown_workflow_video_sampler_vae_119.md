---
name: unknown_workflow_video_sampler_vae_119
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9856
common_nodes: [GrowMaskWithBlur, ImageCompositeMasked, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, MaskToImage, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [平台全量/超强全自动水印去除-豆包-即梦-小云雀-seedance2_2044708716452257793.json, 数字人/数字人/Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114.json, 数字人/数字人/全能视频Sor 2 新版去水印 视频移动水印_1987445207627182081.json, 数字人/数字人/去除移动水印 全能视频S水印_1984039894601400321.json, 数字人/数字人/固定水印去除 Minimax Remover 定点遮罩消除  自定义遮罩_2033107626417983489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_119

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/超强全自动水印去除-豆包-即梦-小云雀-seedance2_2044708716452257793.json、数字人/数字人/Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114.json、数字人/数字人/全能视频Sor 2 新版去水印 视频移动水印_1987445207627182081.json、数字人/数字人/去除移动水印 全能视频S水印_1984039894601400321.json、数字人/数字人/固定水印去除 Minimax Remover 定点遮罩消除  自定义遮罩_2033107626417983489.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcatMulti`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `BboxDetectorCombined_v2` —— 4/5 个有
- `LayerUtility: ColorImage V2` —— 4/5 个有
- `MaskListToMaskBatch` —— 4/5 个有
- `UltralyticsDetectorProvider` —— 4/5 个有
- `ImageToMask_AS` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RepeatImageBatch` —— 1/5 个有
- `SAM3Segment` —— 1/5 个有
- `easy int` —— 1/5 个有
- `preview_mask` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
