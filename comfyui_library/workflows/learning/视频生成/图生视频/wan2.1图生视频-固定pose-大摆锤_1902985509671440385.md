---
key: 视频生成/图生视频/wan2.1图生视频-固定pose-大摆锤_1902985509671440385.json
name: wan2.1图生视频-固定pose-大摆锤_1902985509671440385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1902985509671440385.json
hash: 540418738ada91fc
coverage: 0.670732
learned_at: 2026-10-15 22:29:24
nodes: [Note, CLIPTextEncode, Int, Note _O, WanVideoTorchCompileSettings, SetNode, SetNode, CR Text Input Switch (4 way), CR String To Boolean, GetNode, JjkText, SetNode, Int, Note _O, Int, WanVideoVRAMManagement, SetNode, LoadWanVideoClipTextEncoder, WanVideoImageClipEncode, ImpactSwitch, SetNode, CR String To Number, CR String To Number, SetNode, Bjornulf_ShowInt, SetNode, Bjornulf_ShowInt, ImpactSwitch, Int, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, Bjornulf_AnythingToText, GetNode, Int, Bjornulf_AnythingToText, Note _O, GetNode, JjkText, LoadWanVideoClipTextEncoder, WanVideoVAELoader, Bjornulf_ShowInt, Int, WanVideoBlockSwap, WanVideoEnhanceAVideo, Int, ImpactSwitch, Int, Bjornulf_AnythingToText, CR String To Number, Note _O, Bjornulf_AnythingToText, Bjornulf_AnythingToText, SetNode, Bjornulf_ShowInt, ImpactSwitch, WanVideoLoraSelect, JjkText, JjkText, SetNode, GetNode, Bjornulf_ShowInt, GetNode, GetNode, WanVideoImageClipEncode, GetNode, Bjornulf_ShowStringText, Int, GetNode, VHS_VideoCombine, Int, Int, WanVideoTextEncode, WanVideoDecode, JjkText, Int, WanVideoModelLoader, CR String To Number, LoadImage, WanVideoSampler, WanVideoTeaCache, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1图生视频-固定pose-大摆锤_1902985509671440385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1902985509671440385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（82 个）：
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
- `Int`
- `Note _O`
- `Int`
- `WanVideoVRAMManagement`
- `SetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoImageClipEncode`
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
- `Note _O`
- `GetNode`
- `JjkText`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `Bjornulf_ShowInt`
- `Int`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `Int`
- `ImpactSwitch`
- `Int`
- `Bjornulf_AnythingToText`
- `CR String To Number`
- `Note _O`
- `Bjornulf_AnythingToText`
- `Bjornulf_AnythingToText`
- `SetNode`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `JjkText`
- `JjkText`
- `SetNode`
- `GetNode`
- `Bjornulf_ShowInt`
- `GetNode`
- `GetNode`
- `WanVideoImageClipEncode`
- `GetNode`
- `Bjornulf_ShowStringText`
- `Int`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `JjkText`
- `Int`
- `WanVideoModelLoader`
- `CR String To Number`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **67%**（55/82）

**有卡**：`CLIPTextEncode`、`Int`、`Note _O`、`WanVideoTorchCompileSettings`、`CR Text Input Switch (4 way)`、`CR String To Boolean`、`WanVideoVRAMManagement`、`LoadWanVideoClipTextEncoder`、`WanVideoImageClipEncode`、`CR String To Number`、`Bjornulf_ShowInt`、`Bjornulf_AnythingToText`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoLoraSelect`、`Bjornulf_ShowStringText`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoModelLoader`、`LoadImage`、`WanVideoSampler`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`

**用到的条目**：CLIPTextEncode、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode
