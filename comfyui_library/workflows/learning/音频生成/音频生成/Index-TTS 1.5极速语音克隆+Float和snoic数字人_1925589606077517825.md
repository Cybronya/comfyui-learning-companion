---
key: 音频生成/音频生成/Index-TTS 1.5极速语音克隆+Float和snoic数字人_1925589606077517825.json
name: Index-TTS 1.5极速语音克隆+Float和snoic数字人_1925589606077517825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Index-TTS 1.5极速语音克隆+Float和snoic数字人_1925589606077517825.json
hash: adce141011c750ba
coverage: 0.809524
learned_at: 2026-10-18 01:23:54
nodes: [FloatProcess, LoadImage, PrimitiveFloat, LoadAudio, ImageOnlyCheckpointLoader, Note _O, LayerUtility: PurgeVRAM, LoadFloatModels, Reroute, IndexTTSNode, SONICSampler, LoadAudio, Reroute, CR Text, SaveAudio, SONIC_PreData, SONICTLoader, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "svd_xt_1_1.safetensors"}
---

# 音频生成/音频生成/Index-TTS 1.5极速语音克隆+Float和snoic数字人_1925589606077517825.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Index-TTS 1.5极速语音克隆+Float和snoic数字人_1925589606077517825.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（21 个）：
- `FloatProcess`
- `LoadImage`
- `PrimitiveFloat`
- `LoadAudio`
- `ImageOnlyCheckpointLoader` ★核心
- `Note _O`
- `LayerUtility: PurgeVRAM`
- `LoadFloatModels`
- `Reroute`
- `IndexTTSNode`
- `SONICSampler` ★核心
- `LoadAudio`
- `Reroute`
- `CR Text`
- `SaveAudio`
- `SONIC_PreData`
- `SONICTLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

## 关键参数

- `checkpoint` = `svd_xt_1_1.safetensors`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`FloatProcess`、`LoadImage`、`LoadAudio`、`ImageOnlyCheckpointLoader`、`Note _O`、`LayerUtility: PurgeVRAM`、`LoadFloatModels`、`IndexTTSNode`、`SONICSampler`、`CR Text`、`SaveAudio`、`SONIC_PreData`、`SONICTLoader`、`VHS_VideoCombine`

**用到的条目**：LoadImage、SONICSampler、ImageOnlyCheckpointLoader、SaveAudio、LoadAudio、VHS_VideoCombine、IndexTTSNode、FloatProcess
