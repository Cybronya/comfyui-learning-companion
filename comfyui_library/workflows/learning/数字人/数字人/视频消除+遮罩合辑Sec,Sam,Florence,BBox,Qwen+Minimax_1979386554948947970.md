---
key: 数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json
name: 视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json
hash: 8234bed7c94e19db
coverage: 0.747368
learned_at: 2026-10-26 02:05:23
nodes: [DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, Note, ImageFromBatch, WanVideoVAELoader, WanVideoModelLoader, WanVideoEncode, WanVideoEncode, GrowMask, LoadWanVideoT5TextEncoder, ImageCompositeMasked, SolidMask, MaskToImage, WanVideoSampler, SeCVideoSegmentation, SeCModelLoader, DrawMaskOnImage, SetNode, easy showAnything, easy showAnything, easy showAnything, VHS_VideoCombine, GetNode, WanVideoTextEncode, GetNode, DrawMaskOnImage, GrowMask, DrawMaskOnImage, GrowMask, DrawMaskOnImage, Mask Switch (JPS), GetNode, ImageFromBatch, InvertMask, InvertMask, GrowMask, InvertMask, InvertMask, InvertMask, easy cleanGpuUsed, PreviewImage, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, easy cleanGpuUsed, SeCVideoSegmentation, SeCModelLoader, LayerMask: MaskPreview, PreviewImage, WanVideoDecode, GetNode, GetNode, RH_Translator, ImageFromBatch, BBoxesToSAM2, MaskPreview+, SeCVideoSegmentation, SeCModelLoader, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, DownloadAndLoadQwenModel, easy cleanGpuUsed, QwenVLDetection, LayerMask: SAM2Ultra, MaskToImage, easy showAnything, easy showAnything, easy showAnything, Reroute, WanVideoMiniMaxRemoverEmbeds, easy int, LayerMask: SAM2Ultra, MuyeTextEditOutput, PointsEditor, DownloadAndLoadSAM2Model, Sam2Segmentation, Fast Groups Bypasser (rgthree), VHS_VideoCombine, easy showAnything, VHS_VideoInfo, easy showAnything, Note, VHS_LoadVideo, GrowMask, VHS_VideoCombine, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频消除+遮罩合辑Sec,Sam,Florence,BBox,Qwen+Minimax_1979386554948947970.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（95 个）：
- `DrawMaskOnImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `Note`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoEncode`
- `WanVideoEncode`
- `GrowMask`
- `LoadWanVideoT5TextEncoder`
- `ImageCompositeMasked`
- `SolidMask`
- `MaskToImage`
- `WanVideoSampler` ★核心
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `DrawMaskOnImage`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `DrawMaskOnImage`
- `GrowMask`
- `DrawMaskOnImage`
- `GrowMask`
- `DrawMaskOnImage`
- `Mask Switch (JPS)`
- `GetNode`
- `ImageFromBatch`
- `InvertMask`
- `InvertMask`
- `GrowMask`
- `InvertMask`
- `InvertMask`
- `InvertMask`
- `easy cleanGpuUsed`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `easy cleanGpuUsed`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `RH_Translator`
- `ImageFromBatch`
- `BBoxesToSAM2`
- `MaskPreview+`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `DownloadAndLoadQwenModel`
- `easy cleanGpuUsed`
- `QwenVLDetection`
- `LayerMask: SAM2Ultra`
- `MaskToImage`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `Reroute`
- `WanVideoMiniMaxRemoverEmbeds`
- `easy int`
- `LayerMask: SAM2Ultra`
- `MuyeTextEditOutput`
- `PointsEditor`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `easy showAnything`
- `VHS_VideoInfo`
- `easy showAnything`
- `Note`
- `VHS_LoadVideo`
- `GrowMask`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（71/95）

**有卡**：`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`ImageFromBatch`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoEncode`、`GrowMask`、`LoadWanVideoT5TextEncoder`、`ImageCompositeMasked`、`SolidMask`、`MaskToImage`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`Mask Switch (JPS)`、`InvertMask`、`easy cleanGpuUsed`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: MaskPreview`、`WanVideoDecode`、`RH_Translator`、`BBoxesToSAM2`、`MaskPreview+`、`DownloadAndLoadQwenModel`、`QwenVLDetection`、`LayerMask: SAM2Ultra`、`WanVideoMiniMaxRemoverEmbeds`、`easy int`、`MuyeTextEditOutput`、`PointsEditor`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、MuyeTextEditOutput、LayerMask: MaskPreview
