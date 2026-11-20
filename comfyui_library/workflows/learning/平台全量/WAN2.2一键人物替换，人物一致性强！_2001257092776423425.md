---
key: 平台全量/WAN2.2一键人物替换，人物一致性强！_2001257092776423425.json
name: WAN2.2一键人物替换，人物一致性强！_2001257092776423425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2一键人物替换，人物一致性强！_2001257092776423425.json
hash: aa3641641bec4fde
coverage: 0.439024
learned_at: 2026-11-14 01:03:43
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, SetNode, GetNode, SetNode, GetNode, GetNode, easy sam3VideoSegmentation, GrowMask, easy sam3ModelLoader, DrawMaskOnImage, SetNode, SetNode, MarkdownNote, MarkdownNote, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RIFE VFI, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, SetNode, VHS_VideoCombine, BlockifyMask, GetNode, GetNode, WanVideoSetLoRAs, WanVideoVAELoader, GetNode, YOLOModelLoader, SetNode, SetNode, GetNode, GetNode, DWPreprocessor, INTConstant, Fast Groups Bypasser (rgthree), FloatConstant, DWPreprocessor, VHS_LoadVideo, WanVideoAnimateEmbeds, WanVideoBlockSwap, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoDecode, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, GetNode, GetNode, GetNode, LoadImage, BiRefNetRMBG, LayerUtility: PurgeVRAM, GetNode, SeedVR2LoadDiTModel, VHS_VideoCombine, WanVideoSampler, INTConstant]
patterns: []
missing: []
---

# 平台全量/WAN2.2一键人物替换，人物一致性强！_2001257092776423425.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2一键人物替换，人物一致性强！_2001257092776423425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（82 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy sam3VideoSegmentation`
- `GrowMask`
- `easy sam3ModelLoader`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RIFE VFI`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `GetNode`
- `YOLOModelLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `BiRefNetRMBG`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `SeedVR2LoadDiTModel`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `INTConstant`

## 知识

覆盖率 **44%**（36/82）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy sam3VideoSegmentation`、`GrowMask`、`easy sam3ModelLoader`、`DrawMaskOnImage`、`RIFE VFI`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`BlockifyMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`YOLOModelLoader`、`DWPreprocessor`、`INTConstant`、`FloatConstant`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`LoadImage`、`BiRefNetRMBG`、`LayerUtility: PurgeVRAM`、`SeedVR2LoadDiTModel`、`WanVideoSampler`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached
