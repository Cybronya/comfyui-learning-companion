---
key: 视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json
name: Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json
hash: 4631cd4ee315e4d3
coverage: 0.75
learned_at: 2026-10-15 22:32:15
nodes: [LoadLynxResampler, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, SetNode, PreviewImage, LynxInsightFaceCrop, LynxEncodeFaceIP, PreviewImage, Note, Note, Note, MarkdownNote, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoVACEModelSelect, AIO_Preprocessor, ImpactSwitch, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, VHS_VideoCombine, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, Text Concatenate, easy showAnything, WanVideoTextEncodeCached, WanVideoTextEncodeCached, PreviewImage, WanVideoDecode, ImageFromBatch+, ImageFromBatch+, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoTorchCompileSettings, CR Text, Wan22PromptSelector, GetNode, SetNode, WanVideoVAELoader, WanVideoAddLynxEmbeds, RH_LLMAPI_NODE, LoadImage, ImageConcatMulti, ImpactSwitch, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_T2V_lynx+VACE姿势参考_1977712133079191553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977712133079191553.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（52 个）：
- `LoadLynxResampler` ★核心
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `SetNode`
- `PreviewImage`
- `LynxInsightFaceCrop`
- `LynxEncodeFaceIP`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoVACEModelSelect`
- `AIO_Preprocessor`
- `ImpactSwitch`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Text Concatenate`
- `easy showAnything`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `CR Text`
- `Wan22PromptSelector`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoAddLynxEmbeds`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `ImageConcatMulti`
- `ImpactSwitch`
- `JWInteger`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`LoadLynxResampler`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`LynxInsightFaceCrop`、`LynxEncodeFaceIP`、`WanVideoExtraModelSelect`、`WanVideoVACEModelSelect`、`AIO_Preprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`Text Concatenate`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`CR Text`、`Wan22PromptSelector`、`WanVideoVAELoader`、`WanVideoAddLynxEmbeds`、`RH_LLMAPI_NODE`、`LoadImage`、`JWInteger`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader
