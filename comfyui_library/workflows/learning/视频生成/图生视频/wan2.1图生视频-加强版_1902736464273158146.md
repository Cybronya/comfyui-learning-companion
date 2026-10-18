---
key: 视频生成/图生视频/wan2.1图生视频-加强版_1902736464273158146.json
name: wan2.1图生视频-加强版_1902736464273158146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1图生视频-加强版_1902736464273158146.json
hash: bf4bdef3e83768af
coverage: 0.670455
learned_at: 2026-10-15 22:29:24
nodes: [Note, CLIPTextEncode, Int, Note _O, WanVideoTorchCompileSettings, SetNode, SetNode, CR Text Input Switch (4 way), CR String To Boolean, GetNode, JjkText, SetNode, SetNode, Note _O, Int, Note _O, Int, Int, SetNode, LoadImage, WanVideoVRAMManagement, WanVideoLoraSelect, SetNode, LoadWanVideoClipTextEncoder, WanVideoImageClipEncode, GetNode, ImpactSwitch, SetNode, CR String To Number, CR String To Number, SetNode, Bjornulf_ShowInt, SetNode, Bjornulf_ShowInt, ImpactSwitch, Int, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, GetNode, Int, Bjornulf_AnythingToText, RH_Captioner, GetNode, Note _O, GetNode, JjkText, Int, LoadWanVideoClipTextEncoder, WanVideoVAELoader, Bjornulf_ShowInt, LoadWanVideoT5TextEncoder, Int, JjkText, WanVideoImageClipEncode, easy textSwitch, Bjornulf_ShowStringText, WanVideoBlockSwap, WanVideoModelLoader, GetNode, WanVideoEnhanceAVideo, GetNode, VHS_VideoCombine, WanVideoDecode, WanVideoTextEncode, Int, ImpactSwitch, Int, Bjornulf_AnythingToText, CR String To Number, Note _O, Bjornulf_AnythingToText, Bjornulf_AnythingToText, CR String To Number, SetNode, GetNode, Bjornulf_ShowInt, GetNode, Bjornulf_ShowInt, Int, ImpactSwitch, JjkText, JjkText, WanVideoSampler, WanVideoTeaCache, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1图生视频-加强版_1902736464273158146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1902736464273158146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（88 个）：
- `Note`
- `CLIPTextEncode` ★核心
- `Int`
- `Note _O`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `CR Text Input Switch (4 way)`
- `CR String To Boolean`
- `GetNode`
- `JjkText`
- `SetNode`
- `SetNode`
- `Note _O`
- `Int`
- `Note _O`
- `Int`
- `Int`
- `SetNode`
- `LoadImage`
- `WanVideoVRAMManagement`
- `WanVideoLoraSelect`
- `SetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoImageClipEncode`
- `GetNode`
- `ImpactSwitch`
- `SetNode`
- `CR String To Number`
- `CR String To Number`
- `SetNode`
- `Bjornulf_ShowInt`
- `SetNode`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `Int`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `GetNode`
- `Int`
- `Bjornulf_AnythingToText`
- `RH_Captioner`
- `GetNode`
- `Note _O`
- `GetNode`
- `JjkText`
- `Int`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `Bjornulf_ShowInt`
- `LoadWanVideoT5TextEncoder`
- `Int`
- `JjkText`
- `WanVideoImageClipEncode`
- `easy textSwitch`
- `Bjornulf_ShowStringText`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `Int`
- `ImpactSwitch`
- `Int`
- `Bjornulf_AnythingToText`
- `CR String To Number`
- `Note _O`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `CR String To Number`
- `SetNode`
- `GetNode`
- `Bjornulf_ShowInt`
- `GetNode`
- `Bjornulf_ShowInt`
- `Int`
- `ImpactSwitch`
- `JjkText`
- `JjkText`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `Int`
- `Int`

## 知识

覆盖率 **67%**（59/88）

**有卡**：`CLIPTextEncode`、`Int`、`Note _O`、`WanVideoTorchCompileSettings`、`CR Text Input Switch (4 way)`、`CR String To Boolean`、`LoadImage`、`WanVideoVRAMManagement`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoImageClipEncode`、`CR String To Number`、`Bjornulf_ShowInt`、`Bjornulf_AnythingToText`、`RH_Captioner`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`easy textSwitch`、`Bjornulf_ShowStringText`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoTeaCache`

**用到的条目**：CLIPTextEncode、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode
