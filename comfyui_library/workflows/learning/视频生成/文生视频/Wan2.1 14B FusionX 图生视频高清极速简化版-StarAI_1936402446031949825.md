---
key: 视频生成/文生视频/Wan2.1 14B FusionX 图生视频高清极速简化版-StarAI_1936402446031949825.json
name: Wan2.1 14B FusionX 图生视频高清极速简化版-StarAI_1936402446031949825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 14B FusionX 图生视频高清极速简化版-StarAI_1936402446031949825.json
hash: 26d855d2f4331bfc
coverage: 0.939394
learned_at: 2026-10-15 22:43:29
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoDecode, WanVideoTextEncodeSingle, WanVideoEmptyEmbeds, WanVideoExperimentalArgs, WanVideoSLG, WanVideoMagCache, WanVideoEnhanceAVideo, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoBlockSwap, RH_LLMAPI_NODE, easy showAnything, SimpleMath+, VHS_VideoCombine, VHS_VideoCombine, ImpactInt, ImpactInt, ImpactInt, easy textSwitch, CR Text, CR Text, Note Plus (mtb), WanVideoModelLoader, RHHiddenNodes, Int, WanVideoSampler, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, UpscaleModelLoader, ImageScaleToMegapixels, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 14B FusionX 图生视频高清极速简化版-StarAI_1936402446031949825.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1936402446031949825.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoTextEncodeSingle`
- `WanVideoEmptyEmbeds`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoMagCache`
- `WanVideoEnhanceAVideo`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoBlockSwap`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `easy textSwitch`
- `CR Text`
- `CR Text`
- `Note Plus (mtb)`
- `WanVideoModelLoader`
- `RHHiddenNodes`
- `Int`
- `WanVideoSampler` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `UpscaleModelLoader`
- `ImageScaleToMegapixels`
- `MarkdownNote`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoTextEncodeSingle`、`WanVideoEmptyEmbeds`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoMagCache`、`WanVideoEnhanceAVideo`、`WanVideoApplyNAG`、`WanVideoBlockSwap`、`RH_LLMAPI_NODE`、`SimpleMath+`、`VHS_VideoCombine`、`ImpactInt`、`easy textSwitch`、`CR Text`、`Note Plus (mtb)`、`WanVideoModelLoader`、`RHHiddenNodes`、`Int`、`WanVideoSampler`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`UpscaleModelLoader`、`ImageScaleToMegapixels`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、UpscaleModelLoader、UpscaleModelLoader、ImpactInt
