---
key: 视频生成/图生视频/Wan2.2长视频生成20秒以上_1970311632809304066.json
name: Wan2.2长视频生成20秒以上_1970311632809304066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2长视频生成20秒以上_1970311632809304066.json
hash: c1ab9c5653fdd37a
coverage: 0.921875
learned_at: 2026-10-15 22:31:52
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoTextEncode, WanVideoApplyNAG, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoTextEncodeSingle, WanVideoTextEncode, WanVideoApplyNAG, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoTextEncodeSingle, WanVideoDecode, PreviewImage, WanVideoTextEncodeSingle, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, WanVideoModelLoader, Note, PrimitiveInt, PrimitiveInt, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, CLIPVisionLoader, GetImageSize, ImageFromBatch+, WanVideoClipVisionEncode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoDecode, DF_Int_to_Float, VHS_VideoCombine, ImageBatch, RH_Translator, WanVideoLoraSelectMulti, CR Text, LoadAudio, SimpleMath+, ImageResizeKJv2, CR SDXL Aspect Ratio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2长视频生成20秒以上_1970311632809304066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970311632809304066.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncode`
- `WanVideoApplyNAG`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncode`
- `WanVideoApplyNAG`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoTextEncodeSingle`
- `WanVideoDecode`
- `PreviewImage`
- `WanVideoTextEncodeSingle`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `GetImageSize`
- `ImageFromBatch+`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `DF_Int_to_Float`
- `VHS_VideoCombine`
- `ImageBatch`
- `RH_Translator`
- `WanVideoLoraSelectMulti`
- `CR Text`
- `LoadAudio`
- `SimpleMath+`
- `ImageResizeKJv2`
- `CR SDXL Aspect Ratio`
- `LoadImage`

## 知识

覆盖率 **92%**（59/64）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoTextEncode`、`WanVideoApplyNAG`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`SimpleMath+`、`CLIPVisionLoader`、`GetImageSize`、`ImageFromBatch+`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`DF_Int_to_Float`、`VHS_VideoCombine`、`ImageBatch`、`RH_Translator`、`WanVideoLoraSelectMulti`、`CR Text`、`LoadAudio`、`ImageResizeKJv2`、`CR SDXL Aspect Ratio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
