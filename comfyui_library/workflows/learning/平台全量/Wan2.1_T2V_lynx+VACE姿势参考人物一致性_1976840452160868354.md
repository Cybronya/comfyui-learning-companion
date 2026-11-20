---
key: 平台全量/Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354.json
name: Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354.json
hash: 0a6d59a64fbf4cdd
coverage: 0.745455
learned_at: 2026-11-14 01:04:42
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, LoadLynxResampler, Wan22PromptSelector, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImpactSwitch, Text Concatenate, easy showAnything, RH_LLMAPI_NODE, WanVideoDecode, WanVideoSampler, SetNode, WanVideoTextEncodeCached, JWInteger, VHS_LoadVideo, JWInteger, ImageFromBatch+, ImageFromBatch+, ImageConcatMulti, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, SetNode, PreviewImage, LynxInsightFaceCrop, LynxEncodeFaceIP, PreviewImage, PreviewImage, WanVideoTextEncodeCached, Note, Note, LoadImage, WanVideoVAELoader, SetNode, Note, MarkdownNote, VHS_VideoCombine, GetNode, CR Text, VHS_VideoCombine, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoVACEModelSelect, AIO_Preprocessor, ImpactSwitch, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, VHS_VideoCombine, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoAddLynxEmbeds, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1_T2V_lynx+VACE姿势参考人物一致性_1976840452160868354.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（55 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `LoadLynxResampler` ★核心
- `Wan22PromptSelector`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImpactSwitch`
- `Text Concatenate`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoTextEncodeCached`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `SetNode`
- `PreviewImage`
- `LynxInsightFaceCrop`
- `LynxEncodeFaceIP`
- `PreviewImage`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `LoadImage`
- `WanVideoVAELoader`
- `SetNode`
- `Note`
- `MarkdownNote`
- `VHS_VideoCombine`
- `GetNode`
- `CR Text`
- `VHS_VideoCombine`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoVACEModelSelect`
- `AIO_Preprocessor`
- `ImpactSwitch`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoAddLynxEmbeds`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（41/55）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadLynxResampler`、`Wan22PromptSelector`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`Text Concatenate`、`RH_LLMAPI_NODE`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`JWInteger`、`VHS_LoadVideo`、`ImageFromBatch+`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`LynxInsightFaceCrop`、`LynxEncodeFaceIP`、`LoadImage`、`WanVideoVAELoader`、`VHS_VideoCombine`、`CR Text`、`WanVideoExtraModelSelect`、`WanVideoLoraSelectMulti`、`WanVideoVACEModelSelect`、`AIO_Preprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoAddLynxEmbeds`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、LoadLynxResampler、WanVideoSampler、LynxEncodeFaceIP、WanVideoDecode
