---
name: unknown_workflow_video_lora_sampler_694
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.99225
common_nodes: [GrowMaskWithBlur, ImageBatchToList, ImageCompositeMasked, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, MaskListToMaskBatch, MaskToImage, SaveText, SolidMask, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageToBase64, easy seed]
problems: []
missing: []
members: [平台全量/亲测效果最好的一个，速度快，全自动一键去除视频去字幕绩消除水印_2037462566095556609.json, 平台全量/全自动一键去除视频去字幕_2034078282748006401.json, 平台全量/全自动一键去除视频去字幕绩消除水印_2037114959926140930.json, 数字人/数字人/视频去字幕_2002210720995524609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_694

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/亲测效果最好的一个，速度快，全自动一键去除视频去字幕绩消除水印_2037462566095556609.json、平台全量/全自动一键去除视频去字幕_2034078282748006401.json、平台全量/全自动一键去除视频去字幕绩消除水印_2037114959926140930.json、数字人/数字人/视频去字幕_2002210720995524609.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageBatchToList`
- `ImageCompositeMasked`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `MaskListToMaskBatch`
- `MaskToImage`
- `SaveText`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageToBase64`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Vignette` —— 2/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
