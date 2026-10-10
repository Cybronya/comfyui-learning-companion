---
key: 视频生成/文生视频/wan2.1+2.2 基础综合版_2001569276173664257.json
name: wan2.1+2.2 基础综合版_2001569276173664257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1+2.2 基础综合版_2001569276173664257.json
hash: 5bc405bc2f28f5a0
coverage: 0.678571
learned_at: 2026-10-11 02:57:39
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, FantasyTalkingModelLoader, MultiTalkModelLoader, FantasyPortraitModelLoader, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, WanVideoApplyNAG, WanVideoClipVisionEncode, WanVideoEmptyEmbeds, CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadImage, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoImageToVideoEncode, Anything Everywhere, Anything Everywhere, WanVideoLoraSelectMulti, Note, Anything Everywhere, INTConstant, INTConstant, Note, Note, Note, Note, WanVideoSampler, Note, WanVideoSampler, Note, WanVideoDecode, WanVideoVAELoader, WanVideoLoraSelectMulti, ImageResizeKJv2, Note, CreateCFGScheduleFloatList, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, Note, WanVideoVACEModelSelect, Note, Note, Note, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1+2.2 基础综合版_2001569276173664257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.1+2.2 基础综合版_2001569276173664257.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `FantasyTalkingModelLoader`
- `MultiTalkModelLoader`
- `FantasyPortraitModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoApplyNAG`
- `WanVideoClipVisionEncode`
- `WanVideoEmptyEmbeds`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoLoraSelectMulti`
- `Note`
- `Anything Everywhere`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `ImageResizeKJv2`
- `Note`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `Note`
- `WanVideoVACEModelSelect`
- `Note`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **68%**（38/56）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`FantasyTalkingModelLoader`、`MultiTalkModelLoader`、`FantasyPortraitModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoApplyNAG`、`WanVideoClipVisionEncode`、`WanVideoEmptyEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`LoadImage`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelectMulti`、`INTConstant`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoVACEModelSelect`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
