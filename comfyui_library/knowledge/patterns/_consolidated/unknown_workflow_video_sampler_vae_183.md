---
name: unknown_workflow_video_sampler_vae_183
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7235
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, DownloadAndLoadSAM2Model, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMask, ImageCompositeMasked, ImageFromBatch, InvertMask, LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LoadWanVideoT5TextEncoder, Mask Switch (JPS), MaskPreview+, MaskToImage, MuyeTextEditOutput, PointsEditor, PreviewImage, QwenVLDetection, RH_Translator, Sam2Segmentation, SeCModelLoader, SeCVideoSegmentation, SetNode, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy int, easy showAnything]
problems: []
missing: []
members: ["数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json", 数字人/数字人/视频消除，任意擦除，最强视频遮罩（Sec Sam BBox等）不同消除方式_2037359402281340929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_183

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json、数字人/数字人/视频消除，任意擦除，最强视频遮罩（Sec Sam BBox等）不同消除方式_2037359402281340929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
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
- `DiffuEraserLoader` —— 1/2 个有
- `DiffuEraserSampler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
