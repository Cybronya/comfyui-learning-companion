---
key: 视频生成/图生视频/WAN2.2 图生视频 极致臻享 2K版_1971101417341652994.json
name: WAN2.2 图生视频 极致臻享 2K版_1971101417341652994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971101417341652994.json
hash: 36be0697c327e600
coverage: 0.489362
learned_at: 2026-10-15 22:31:55
nodes: [SetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, SetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, WanVideoImageToVideoEncode, WanVideoTextEncodeSingle, GetNode, easy negative, WanVideoTextEncode, WanVideoApplyNAG, SetNode, SetNode, SetNode, Int, Int, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy mathInt, easy mathInt, GetNode, WanVideoDecode, GetNode, SetNode, GetNode, GetNode, SetNode, ImpactSwitch, GetNode, SetNode, WanVideoSampler, DownloadAndLoadGIMMVFIModel, easy ifElse, WanVideoSetBlockSwap, LoadJsonFromText, LoadJsonFromText, LoadJsonFromText, GetNode, LoadJsonFromText, GetNode, ImpactControlBridge, GIMMVFI_interpolate, GetNode, ImageScaleToMegapixels, GetNode, CR Text, MarkdownNote, ImpactSwitch, ImpactInt, SetNode, MarkdownNote, MarkdownNote, SetNode, MarkdownNote, ImpactInt, ImpactInt, Seed (rgthree), VHS_VideoCombine, VHS_VideoCombine, Note Plus (mtb), MarkdownNote, LoadImage, GetNode, RH_Captioner, GLM_Vision_ImageToPrompt, GetNode, StringFunction|pysssss, easy showAnything, SetNode, RH_LLMAPI_NODE, RHHiddenNodes, ImpactSwitch, WanVideoModelLoader, WanVideoVAELoader, UpscaleModelLoader, WanVideoSampler, LoadJsonFromText, WanVideoSetLoRAs, easy ifElse, RHHiddenNodes, WanVideoModelLoader, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2 图生视频 极致臻享 2K版_1971101417341652994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971101417341652994.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（94 个）：
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `easy negative`
- `WanVideoTextEncode`
- `WanVideoApplyNAG`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImpactSwitch`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `easy ifElse`
- `WanVideoSetBlockSwap`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `LoadJsonFromText`
- `GetNode`
- `LoadJsonFromText`
- `GetNode`
- `ImpactControlBridge`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageScaleToMegapixels`
- `GetNode`
- `CR Text`
- `MarkdownNote`
- `ImpactSwitch`
- `ImpactInt`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `MarkdownNote`
- `ImpactInt`
- `ImpactInt`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `MarkdownNote`
- `LoadImage`
- `GetNode`
- `RH_Captioner`
- `GLM_Vision_ImageToPrompt`
- `GetNode`
- `StringFunction|pysssss`
- `easy showAnything`
- `SetNode`
- `RH_LLMAPI_NODE`
- `RHHiddenNodes`
- `ImpactSwitch`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `UpscaleModelLoader`
- `WanVideoSampler` ★核心
- `LoadJsonFromText`
- `WanVideoSetLoRAs`
- `easy ifElse`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `SetNode`

## 知识

覆盖率 **49%**（46/94）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeSingle`、`easy negative`、`WanVideoTextEncode`、`WanVideoApplyNAG`、`Int`、`easy mathInt`、`WanVideoDecode`、`WanVideoSampler`、`DownloadAndLoadGIMMVFIModel`、`LoadJsonFromText`、`ImpactControlBridge`、`GIMMVFI_interpolate`、`ImageScaleToMegapixels`、`CR Text`、`ImpactInt`、`Seed (rgthree)`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImage`、`RH_Captioner`、`GLM_Vision_ImageToPrompt`、`StringFunction|pysssss`、`RH_LLMAPI_NODE`、`RHHiddenNodes`、`WanVideoModelLoader`、`WanVideoVAELoader`、`UpscaleModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
