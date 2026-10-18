---
key: 视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json
name: Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json
hash: 34e019a7c8509557
coverage: 0.833333
learned_at: 2026-10-15 22:32:16
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, LoadLynxResampler, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoTextEncodeCached, WanVideoTextEncodeCached, Note, Note, WanVideoVACEModelSelect, Note, MarkdownNote, WanVideoAddLynxEmbeds, LynxEncodeFaceIP, WanVideoSampler, WanVideoDecode, ImageFromBatch+, ImageFromBatch+, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, JWInteger, VHS_VideoCombine, LynxInsightFaceCrop, PreviewImage, PreviewImage, Wan22PromptSelector, CR Text, Text Concatenate, RH_LLMAPI_NODE, easy showAnything, ImpactSwitch, WanVideoLoraSelectMulti, WanVideoModelLoader, VHS_LoadVideo, LoadImage, ImageResizeKJ, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, WanVideoVACEEncode, LayerMask: SegmentAnythingUltra V3, ImageFromBatch, SeCModelLoader, SeCVideoSegmentation, MaskPreview+, LayerMask: LoadSegmentAnythingModels, GrowMask, BlockifyMask, DrawMaskOnImage, GetImageSizeAndCount, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_T2V_lynx+VACE视频换脸_1977718414808678401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977718414808678401.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（54 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoadLynxResampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `WanVideoVACEModelSelect`
- `Note`
- `MarkdownNote`
- `WanVideoAddLynxEmbeds`
- `LynxEncodeFaceIP`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `JWInteger`
- `VHS_VideoCombine`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `PreviewImage`
- `Wan22PromptSelector`
- `CR Text`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `ImpactSwitch`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJ`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `LayerMask: SegmentAnythingUltra V3`
- `ImageFromBatch`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `MaskPreview+`
- `LayerMask: LoadSegmentAnythingModels`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadLynxResampler`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`WanVideoVACEModelSelect`、`WanVideoAddLynxEmbeds`、`LynxEncodeFaceIP`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`ImageConcatMulti`、`VHS_VideoCombine`、`JWInteger`、`LynxInsightFaceCrop`、`Wan22PromptSelector`、`CR Text`、`Text Concatenate`、`RH_LLMAPI_NODE`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`LayerMask: SegmentAnythingUltra V3`、`ImageFromBatch`、`SeCModelLoader`、`SeCVideoSegmentation`、`MaskPreview+`、`LayerMask: LoadSegmentAnythingModels`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
