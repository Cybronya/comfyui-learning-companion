---
key: 视频生成/图生视频/WAN2.1 万相图生视频 搬运优化版_1905868237639454722.json
name: WAN2.1 万相图生视频 搬运优化版_1905868237639454722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1 万相图生视频 搬运优化版_1905868237639454722.json
hash: 34a98a4b579d4878
coverage: 0.774194
learned_at: 2026-10-15 22:29:26
nodes: [Int, Int, Int, Bjornulf_AnythingToText, Int, Int, Int, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, ImpactSwitch, ImpactSwitch, CR String To Number, CR String To Number, easy showAnything, easy int, easy int, easy int, ImpactSwitch, easy mathInt, easy mathInt, easy showAnything, ImpactSwitch, GetNode, easy mathInt, easy showAnything, easy showAnything, ImageResizeAdvanced, RH_Captioner, easy textSwitch, Bjornulf_ShowStringText, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoImageClipEncode, WanVideoSampler, WanVideoTextEncode, Note, FILM VFI, LayerUtility: ImageScaleRestore V2, WanVideoDecode, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, Note, Note, JjkText, SetNode, Int, Note _O, Note _O, Int, LoadImage, Int, Note _O]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 万相图生视频 搬运优化版_1905868237639454722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1905868237639454722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（62 个）：
- `Int`
- `Int`
- `Int`
- `Bjornulf_AnythingToText`
- `Int`
- `Int`
- `Int`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `ImpactSwitch`
- `ImpactSwitch`
- `CR String To Number`
- `CR String To Number`
- `easy showAnything`
- `easy int`
- `easy int`
- `easy int`
- `ImpactSwitch`
- `easy mathInt`
- `easy mathInt`
- `easy showAnything`
- `ImpactSwitch`
- `GetNode`
- `easy mathInt`
- `easy showAnything`
- `easy showAnything`
- `ImageResizeAdvanced`
- `RH_Captioner`
- `easy textSwitch`
- `Bjornulf_ShowStringText`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `Note`
- `FILM VFI`
- `LayerUtility: ImageScaleRestore V2`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `JjkText`
- `SetNode`
- `Int`
- `Note _O`
- `Note _O`
- `Int`
- `LoadImage`
- `Int`
- `Note _O`

## 知识

覆盖率 **77%**（48/62）

**有卡**：`Int`、`Bjornulf_AnythingToText`、`CR String To Number`、`easy int`、`easy mathInt`、`ImageResizeAdvanced`、`RH_Captioner`、`easy textSwitch`、`Bjornulf_ShowStringText`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoTextEncode`、`FILM VFI`、`LayerUtility: ImageScaleRestore V2`、`WanVideoDecode`、`VHS_VideoCombine`、`Note _O`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
