---
name: unknown_workflow_video_lora_sampler_810
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.796
common_nodes: [BBoxesToSAM2, BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadQwenModel, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMask, Image Comparer (rgthree), ImageAndMaskPreview, ImageCompositeMasked, ImageFromBatch, ImageResize+, ImageResizeKJv2, InvertMask, KSamplerAdvanced, LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview, MaskPreview+, MaskToImage, MuyeTextEditOutput, PointsEditor, PreviewImage, QwenVLDetection, RH_Translator, ReferenceLatent, SaveImage, SeCModelLoader, SeCVideoSegmentation, SetNode, SolidMask, Switch, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageScaleDown, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/去水印，去视频元素 视频编辑  多遮罩 Animate  Minimax_2044686078963097602.json, 数字人/数字人/超强 视频编辑，水印去除，物体移除 Minimax+Animate_2044414119616454658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_810

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/去水印，去视频元素 视频编辑  多遮罩 Animate  Minimax_2044686078963097602.json、数字人/数字人/超强 视频编辑，水印去除，物体移除 Minimax+Animate_2044414119616454658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxesToSAM2`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadQwenModel`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `InvertMask`
- `KSamplerAdvanced`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `MaskPreview+`
- `MaskToImage`
- `MuyeTextEditOutput`
- `PointsEditor`
- `PreviewImage`
- `QwenVLDetection`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SolidMask`
- `Switch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDown`
- `easy int`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
