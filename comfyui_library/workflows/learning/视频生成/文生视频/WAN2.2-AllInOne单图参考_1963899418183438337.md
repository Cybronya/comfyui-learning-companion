---
key: 视频生成/文生视频/WAN2.2-AllInOne单图参考_1963899418183438337.json
name: WAN2.2-AllInOne单图参考_1963899418183438337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne单图参考_1963899418183438337.json
hash: 6052018757f35187
coverage: 0.689655
learned_at: 2026-10-10 23:05:55
nodes: [GetImageSize, Image Blank, WanVideoVAELoader, PreviewImage, LayerMask: SAM2Ultra, easy ifElse, PreviewImage, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, ImageCompositeMasked, LayerUtility: PurgeVRAM, INTConstant, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoDecode, LoadWanVideoT5TextEncoder, INTConstant, INTConstant, WanVideoVACEEncode, ImageResizeKJv2, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSampler, String Literal, LoadImage]
patterns: []
missing: [Image Blank, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, String Literal]
discoveries: [次要节点 `Image Blank` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: ObjectDetectorFL2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2Ultra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/WAN2.2-AllInOne单图参考_1963899418183438337.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne单图参考_1963899418183438337.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `PreviewImage`
- `LayerMask: SAM2Ultra`
- `easy ifElse`
- `PreviewImage`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `ImageCompositeMasked`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `INTConstant`
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `String Literal`
- `LoadImage`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`GetImageSize`、`WanVideoVAELoader`、`ImageCompositeMasked`、`INTConstant`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVACEEncode`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`LoadImage`

**缺卡**（6）：`Image Blank`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2Ultra`、`LayerUtility: PurgeVRAM`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `Image Blank` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: ObjectDetectorFL2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2Ultra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
