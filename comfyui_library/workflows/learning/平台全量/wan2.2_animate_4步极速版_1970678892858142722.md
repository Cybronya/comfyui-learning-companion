---
key: 平台全量/wan2.2_animate_4步极速版_1970678892858142722.json
name: wan2.2_animate_4步极速版_1970678892858142722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2_animate_4步极速版_1970678892858142722.json
hash: 97d4a188c7940e59
coverage: 0.894737
learned_at: 2026-11-14 01:19:38
nodes: [easy setNode, easy setNode, easy setNode, WanVideoClipVisionEncode, Reroute, FaceMaskFromPoseKeypoints, easy setNode, WanVideoDecode, easy getNode, easy setNode, easy getNode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, easy setNode, easy textIndexSwitch, easy seed, easy getNode, PixelPerfectResolution, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, WanVideoAnimateEmbeds, easy setNode, easy setNode, easy setNode, easy setNode, easy int, ImageResizeKJv2, easy getNode, easy getNode, ShowText|pysssss, WanVideoSampler, WanVideoTorchCompileSettings, easy setNode, WanVideoBlockSwap, WanVideoSetBlockSwap, easy getNode, Text Multiline, ImageCropByMaskAndResize, Note, Note, Note, Note, DWPreprocessor, easy positive, LoadImage, StringConcatenate, AILab_MiniCPM_4_V_Advanced, easy int, Note, Note, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, easy int, easy int, easy float, CM_FloatToInt, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/wan2.2_animate_4步极速版_1970678892858142722.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2_animate_4步极速版_1970678892858142722.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（76 个）：
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `WanVideoClipVisionEncode`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `easy setNode`
- `WanVideoDecode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `easy setNode`
- `easy textIndexSwitch`
- `easy seed`
- `easy getNode`
- `PixelPerfectResolution`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `WanVideoAnimateEmbeds`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy int`
- `ImageResizeKJv2`
- `easy getNode`
- `easy getNode`
- `ShowText|pysssss`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `easy setNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `easy getNode`
- `Text Multiline`
- `ImageCropByMaskAndResize`
- `Note`
- `Note`
- `Note`
- `Note`
- `DWPreprocessor`
- `easy positive`
- `LoadImage`
- `StringConcatenate`
- `AILab_MiniCPM_4_V_Advanced`
- `easy int`
- `Note`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `easy int`
- `easy int`
- `easy float`
- `CM_FloatToInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **89%**（68/76）

**有卡**：`easy setNode`、`WanVideoClipVisionEncode`、`FaceMaskFromPoseKeypoints`、`WanVideoDecode`、`easy getNode`、`VHS_VideoCombine`、`ImageConcatMulti`、`easy textIndexSwitch`、`easy seed`、`PixelPerfectResolution`、`WanVideoAnimateEmbeds`、`easy int`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`Text Multiline`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`easy positive`、`LoadImage`、`StringConcatenate`、`AILab_MiniCPM_4_V_Advanced`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`easy float`、`CM_FloatToInt`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
