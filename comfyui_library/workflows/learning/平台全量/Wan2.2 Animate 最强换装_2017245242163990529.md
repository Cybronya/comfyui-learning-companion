---
key: 平台全量/Wan2.2 Animate 最强换装_2017245242163990529.json
name: Wan2.2 Animate 最强换装_2017245242163990529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 最强换装_2017245242163990529.json
hash: 707cc50d570e7eb3
coverage: 0.549296
learned_at: 2026-11-14 01:05:02
nodes: [PreviewImage, SetNode, SetNode, SetNode, SetNode, PreviewImage, RMBG, GetNode, SetNode, LoadImage, Mask Fill Holes, BlockifyMask, SetNode, MaskPreview+, WanVideoModelLoader, ImageScale, AdjustBrightnessContrastSaturationNode, GetNode, easy imageConcat, GetNode, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, SetNode, WanVideoVAELoader, LoadImage, GetNode, GetNode, WanVideoSetBlockSwap, GetNode, DrawMaskOnImage, RepeatImageBatch, SetNode, SetNode, RepeatImageBatch, easy int, SetNode, PreviewImage, SaveImage, OpenposePreprocessor, ImageToMask, MaskToImage, easy imageSizeBySide, ImageResizeKJv2, easy cleanGpuUsed, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoDecode, GetNode, easy imageSize, ImageFromBatch, BlendInpaint, easy imageConcat, SetNode, Florence2Run, GetNode, DownloadAndLoadFlorence2Model, WanVideoTextEncodeCached, WanVideoSampler, SetNode]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 最强换装_2017245242163990529.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 最强换装_2017245242163990529.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（71 个）：
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `RMBG`
- `GetNode`
- `SetNode`
- `LoadImage`
- `Mask Fill Holes`
- `BlockifyMask`
- `SetNode`
- `MaskPreview+`
- `WanVideoModelLoader`
- `ImageScale`
- `AdjustBrightnessContrastSaturationNode`
- `GetNode`
- `easy imageConcat`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoVAELoader`
- `LoadImage`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `DrawMaskOnImage`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RepeatImageBatch`
- `easy int`
- `SetNode`
- `PreviewImage`
- `SaveImage`
- `OpenposePreprocessor`
- `ImageToMask`
- `MaskToImage`
- `easy imageSizeBySide`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `GetNode`
- `easy imageSize`
- `ImageFromBatch`
- `BlendInpaint`
- `easy imageConcat`
- `SetNode`
- `Florence2Run`
- `GetNode`
- `DownloadAndLoadFlorence2Model`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `SetNode`

## 知识

覆盖率 **55%**（39/71）

**有卡**：`RMBG`、`LoadImage`、`Mask Fill Holes`、`BlockifyMask`、`MaskPreview+`、`WanVideoModelLoader`、`ImageScale`、`AdjustBrightnessContrastSaturationNode`、`easy imageConcat`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`DrawMaskOnImage`、`RepeatImageBatch`、`easy int`、`SaveImage`、`OpenposePreprocessor`、`ImageToMask`、`MaskToImage`、`easy imageSizeBySide`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoDecode`、`easy imageSize`、`ImageFromBatch`、`BlendInpaint`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`WanVideoTextEncodeCached`、`WanVideoSampler`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、OpenposePreprocessor、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader
