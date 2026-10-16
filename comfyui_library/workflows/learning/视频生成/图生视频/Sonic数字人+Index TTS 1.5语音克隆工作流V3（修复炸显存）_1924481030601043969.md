---
key: 视频生成/图生视频/Sonic数字人+Index TTS 1.5语音克隆工作流V3（修复炸显存）_1924481030601043969.json
name: Sonic数字人+Index TTS 1.5语音克隆工作流V3（修复炸显存）_1924481030601043969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1924481030601043969.json
hash: b8b2f868c0df53aa
coverage: 0.904762
learned_at: 2026-10-15 22:29:50
nodes: [LayerUtility: PurgeVRAM, SONICSampler, VHS_VideoCombine, Note Plus (mtb), LoadImage, Note _O, SaveAudio, SONIC_PreData, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SONICTLoader, IndexTTSRun, ImpactSwitch, ImageOnlyCheckpointLoader, Note, LoadAudio, LoadAudio, CR Prompt Text]
patterns: []
missing: []
parameters: {"checkpoint": "svd_xt_1_1.safetensors"}
---

# 视频生成/图生视频/Sonic数字人+Index TTS 1.5语音克隆工作流V3（修复炸显存）_1924481030601043969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924481030601043969.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（21 个）：
- `LayerUtility: PurgeVRAM`
- `SONICSampler` ★核心
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `LoadImage`
- `Note _O`
- `SaveAudio`
- `SONIC_PreData`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SONICTLoader`
- `IndexTTSRun`
- `ImpactSwitch`
- `ImageOnlyCheckpointLoader` ★核心
- `Note`
- `LoadAudio`
- `LoadAudio`
- `CR Prompt Text`

## 关键参数

- `checkpoint` = `svd_xt_1_1.safetensors`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`LayerUtility: PurgeVRAM`、`SONICSampler`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImage`、`Note _O`、`SaveAudio`、`SONIC_PreData`、`easy cleanGpuUsed`、`SONICTLoader`、`IndexTTSRun`、`ImageOnlyCheckpointLoader`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：LoadImage、SONICSampler、ImageOnlyCheckpointLoader、CR Prompt Text、SaveAudio、LoadAudio、VHS_VideoCombine、IndexTTSRun
