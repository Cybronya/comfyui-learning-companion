---
key: 视频生成/文生视频/WAN2.2-AllInOne参考编辑_1963894519111700482.json
name: WAN2.2-AllInOne参考编辑_1963894519111700482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne参考编辑_1963894519111700482.json
hash: e8bafc55461d7839
coverage: 0.898305
learned_at: 2026-10-10 23:05:56
nodes: [WanVideoDecode, WanVideoVACEEncode, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelect, INTConstant, INTConstant, INTConstant, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, Sam2Segmentation, DownloadAndLoadSAM2Model, QwenVLDetection, VHS_VideoCombine, RH_Captioner, WanVideoVACEModelSelect, DownloadAndLoadQwenModel, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler, ImageBatchToList, GrowMaskWithBlur, GetImageSize+, MaskBatchToList, VHS_LoadVideo, SolidMask, MaskToImage, LoadImage, ImageCompositeMasked, RH_Captioner, LoadWanVideoT5TextEncoder, LayerMask: ObjectDetectorFL2, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, PreviewImage, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, ImageResizeKJ, ImageResizeKJ, GrowMaskWithBlur, InpaintPreprocessor, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, VHS_LoadVideo, INTConstant, WanVideoVACEEncode, INTConstant, WanVideoSampler, INTConstant, LoadImage, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: [LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM V2, GetImageSize+]
discoveries: [次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: ObjectDetectorFL2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2Ultra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/WAN2.2-AllInOne参考编辑_1963894519111700482.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne参考编辑_1963894519111700482.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（59 个）：
- `WanVideoDecode`
- `WanVideoVACEEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `QwenVLDetection`
- `VHS_VideoCombine`
- `RH_Captioner`
- `WanVideoVACEModelSelect`
- `DownloadAndLoadQwenModel`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `ImageBatchToList`
- `GrowMaskWithBlur`
- `GetImageSize+`
- `MaskBatchToList`
- `VHS_LoadVideo`
- `SolidMask`
- `MaskToImage`
- `LoadImage`
- `ImageCompositeMasked`
- `RH_Captioner`
- `LoadWanVideoT5TextEncoder`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `PreviewImage`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `GrowMaskWithBlur`
- `InpaintPreprocessor`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `VHS_LoadVideo`
- `INTConstant`
- `WanVideoVACEEncode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `INTConstant`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **90%**（53/59）

**有卡**：`WanVideoDecode`、`WanVideoVACEEncode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`QwenVLDetection`、`VHS_VideoCombine`、`RH_Captioner`、`WanVideoVACEModelSelect`、`DownloadAndLoadQwenModel`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`ImageBatchToList`、`GrowMaskWithBlur`、`MaskBatchToList`、`VHS_LoadVideo`、`SolidMask`、`MaskToImage`、`LoadImage`、`ImageCompositeMasked`、`ImageResizeKJ`、`InpaintPreprocessor`

**缺卡**（5）：`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2Ultra`、`LayerUtility: PurgeVRAM V2`、`GetImageSize+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: ObjectDetectorFL2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2Ultra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
