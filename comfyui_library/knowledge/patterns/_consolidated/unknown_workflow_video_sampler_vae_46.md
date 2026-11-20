---
name: unknown_workflow_video_sampler_vae_46
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8819
common_nodes: [GetImageSize+, GrowMaskWithBlur, ImageCompositeMasked, ImageFromBatch, LoadImage, MaskToImage, PreviewImage, RepeatImageBatch, SolidMask, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/视频去水印通用版_非会员无角标导出_2028747956966395905.json, 平台全量/视频去水印-通用版_2012716190602366978.json, 平台全量/视频去水印_2045186143859253250.json, 平台全量/视频去水印实用版 视频修复 视频放大修复 非会员无角标无水印导出_2031973034495578114.json, 平台全量/视频去水印工作流_2011390777447948290.json, 平台全量/视频去水印通用版 内含去除RH水印视频导出_2035696944688926722.json, 平台全量/视频去水印通用版 内含去除RH水印视频导出_2035704632781049858.json, 平台全量/视频去水印通用版 内含去除RH水印视频导出_2100897416819068929.json, 平台全量/视频去水印通用版_非R会员无角标导出_2049753554348457986.json, 平台全量/视频精准去水印与无痕修复_2060026970926313474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_46

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/视频去水印通用版_非会员无角标导出_2028747956966395905.json、平台全量/视频去水印-通用版_2012716190602366978.json、平台全量/视频去水印_2045186143859253250.json、平台全量/视频去水印实用版 视频修复 视频放大修复 非会员无角标无水印导出_2031973034495578114.json、平台全量/视频去水印工作流_2011390777447948290.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `GetImageSize+`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `RepeatImageBatch`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `VHS_VideoInfoLoaded` —— 9/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
