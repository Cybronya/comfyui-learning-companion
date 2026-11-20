---
key: 平台全量/Wan2.2 Animate 高质量视频换背景_2010992426214760449.json
name: Wan2.2 Animate 高质量视频换背景_2010992426214760449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 高质量视频换背景_2010992426214760449.json
hash: 552c13e72763b56f
coverage: 0.657143
learned_at: 2026-11-14 01:05:05
nodes: [WanVideoTorchCompileSettings, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoContextOptions, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, CLIPVisionLoader, INTConstant, SetNode, MaskToImage, SetNode, SetNode, VHS_VideoCombine, DrawMaskOnImage, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, OnnxDetectionModelLoader, SeCModelLoader, GetImageSizeAndCount, ImageResizeKJv2, RH_LLMAPI_NODE, PreviewAny, GetNode, SetNode, GrowMaskWithBlur, WanVideoClipVisionEncode, WanVideoTextEncodeCached, MaskToImage, GetNode, GetNode, GetNode, TTP_text_mix, WanVideoSampler, SetNode, SeCVideoSegmentation, WanVideoDecode, Note, GetNode, GetNode, ImageCompositeMasked, GetImageSizeAndCount, VHS_VideoCombine, PoseAndFaceDetection, BlockifyMask, LayerMask: MaskInvert, GetNode, SetNode, AILab_QwenVL, ImageResize+, SetNode, ImageResize+, INTConstant, WanVideoAnimateEmbeds, WanVideoBlockSwap, VHS_LoadVideo, LoadImage, CR SDXL Aspect Ratio, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoInfo, SetNode, VHS_LoadVideo, LoadImage, RH_Translator]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 高质量视频换背景_2010992426214760449.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 高质量视频换背景_2010992426214760449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（70 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoContextOptions`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `INTConstant`
- `SetNode`
- `MaskToImage`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SeCModelLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `RH_LLMAPI_NODE`
- `PreviewAny`
- `GetNode`
- `SetNode`
- `GrowMaskWithBlur`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `TTP_text_mix`
- `WanVideoSampler` ★核心
- `SetNode`
- `SeCVideoSegmentation`
- `WanVideoDecode`
- `Note`
- `GetNode`
- `GetNode`
- `ImageCompositeMasked`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `LayerMask: MaskInvert`
- `GetNode`
- `SetNode`
- `AILab_QwenVL`
- `ImageResize+`
- `SetNode`
- `ImageResize+`
- `INTConstant`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `LoadImage`
- `CR SDXL Aspect Ratio`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `SetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `RH_Translator`

## 知识

覆盖率 **66%**（46/70）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoContextOptions`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`CLIPVisionLoader`、`INTConstant`、`MaskToImage`、`VHS_VideoCombine`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`SeCModelLoader`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`RH_LLMAPI_NODE`、`GrowMaskWithBlur`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`TTP_text_mix`、`WanVideoSampler`、`SeCVideoSegmentation`、`WanVideoDecode`、`ImageCompositeMasked`、`PoseAndFaceDetection`、`BlockifyMask`、`LayerMask: MaskInvert`、`AILab_QwenVL`、`ImageResize+`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`CR SDXL Aspect Ratio`、`VHS_VideoInfo`、`RH_Translator`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
