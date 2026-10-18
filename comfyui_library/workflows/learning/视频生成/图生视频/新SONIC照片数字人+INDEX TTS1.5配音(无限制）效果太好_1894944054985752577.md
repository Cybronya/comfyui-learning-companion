---
key: 视频生成/图生视频/新SONIC照片数字人+INDEX TTS1.5配音(无限制）效果太好_1894944054985752577.json
name: 新SONIC照片数字人+INDEX TTS1.5配音(无限制）效果太好_1894944054985752577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/新SONIC照片数字人+INDEX TTS1.5配音(无限制）效果太好_1894944054985752577.json
hash: a583b67af798bac2
coverage: 0.818182
learned_at: 2026-10-15 22:29:16
nodes: [LoadImage, SONICTLoader, SONIC_PreData, SONICSampler, ImageOnlyCheckpointLoader, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, LoadAudio, IndexTTSRun, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "svd_xt_1_1.safetensors"}
---

# 视频生成/图生视频/新SONIC照片数字人+INDEX TTS1.5配音(无限制）效果太好_1894944054985752577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894944054985752577.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（11 个）：
- `LoadImage`
- `SONICTLoader`
- `SONIC_PreData`
- `SONICSampler` ★核心
- `ImageOnlyCheckpointLoader` ★核心
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `IndexTTSRun`
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `svd_xt_1_1.safetensors`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`LoadImage`、`SONICTLoader`、`SONIC_PreData`、`SONICSampler`、`ImageOnlyCheckpointLoader`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`LoadAudio`、`IndexTTSRun`

**用到的条目**：LoadImage、SONICSampler、ImageOnlyCheckpointLoader、LoadAudio、VHS_VideoCombine、IndexTTSRun、SONIC_PreData、SONICTLoader
