---
name: unknown_workflow_video_sampler_vae_184
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.733333
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, DownloadAndLoadSAM2Model, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMask, ImageCompositeMasked, ImageFromBatch, InvertMask, LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LoadWanVideoT5TextEncoder, Mask Switch (JPS), MaskPreview+, MaskToImage, MuyeTextEditOutput, PointsEditor, PreviewImage, QwenVLDetection, RH_Translator, Sam2Segmentation, SeCModelLoader, SeCVideoSegmentation, SetNode, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy int, easy showAnything]
problems: []
missing: []
members: [平台全量/视频物件遮罩消除_2021760218622861314.json, "数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json", 数字人/数字人/视频消除，任意擦除，最强视频遮罩（Sec Sam BBox等）不同消除方式_2037359402281340929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_184

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频物件遮罩消除_2021760218622861314.json、数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json、数字人/数字人/视频消除，任意擦除，最强视频遮罩（Sec Sam BBox等）不同消除方式_2037359402281340929.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `InvertMask`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LoadWanVideoT5TextEncoder`
- `Mask Switch (JPS)`
- `MaskPreview+`
- `MaskToImage`
- `MuyeTextEditOutput`
- `PointsEditor`
- `PreviewImage`
- `QwenVLDetection`
- `RH_Translator`
- `Sam2Segmentation`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DiffuEraserLoader` —— 1/3 个有
- `DiffuEraserSampler` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
