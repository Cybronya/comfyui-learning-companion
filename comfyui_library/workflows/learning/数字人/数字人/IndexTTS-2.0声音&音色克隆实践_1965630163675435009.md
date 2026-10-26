---
key: 数字人/数字人/IndexTTS-2.0声音&音色克隆实践_1965630163675435009.json
name: IndexTTS-2.0声音&音色克隆实践_1965630163675435009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/IndexTTS-2.0声音&音色克隆实践_1965630163675435009.json
hash: d369a76a702993ea
coverage: 1
learned_at: 2026-10-26 01:54:39
nodes: [LoadAudio, JWStringMultiline, MelBandRoFormerModelLoader, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MelBandRoFormerSampler, MelBandRoFormerModelLoader, MelBandRoFormerModelLoader, LoadAudio, MelBandRoFormerSampler, MelBandRoFormerSampler, LoadAudio, JWStringMultiline, MelBandRoFormerModelLoader, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MelBandRoFormerSampler, JWStringMultiline, JWStringMultiline, IndexTTS2Run, LoadAudio, JWStringMultiline, MelBandRoFormerModelLoader, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MelBandRoFormerSampler, JWStringMultiline, JWStringMultiline, IndexTTS2Run, LoadAudio, JWStringMultiline, MelBandRoFormerModelLoader, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MelBandRoFormerSampler, IndexTTS2Run, PreviewAudio, LoadAudio, LoadAudio, PreviewAudio, PreviewAudio, PreviewAudio, IndexTTS2Run, LoadImage, SaveImage]
patterns: []
missing: []
---

# 数字人/数字人/IndexTTS-2.0声音&音色克隆实践_1965630163675435009.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/IndexTTS-2.0声音&音色克隆实践_1965630163675435009.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（48 个）：
- `LoadAudio`
- `JWStringMultiline`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `LoadAudio`
- `JWStringMultiline`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `JWStringMultiline`
- `JWStringMultiline`
- `IndexTTS2Run`
- `LoadAudio`
- `JWStringMultiline`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `JWStringMultiline`
- `JWStringMultiline`
- `IndexTTS2Run`
- `LoadAudio`
- `JWStringMultiline`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `IndexTTS2Run`
- `PreviewAudio`
- `LoadAudio`
- `LoadAudio`
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `IndexTTS2Run`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **100%**（48/48）

**有卡**：`LoadAudio`、`JWStringMultiline`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`IndexTTS2Run`、`PreviewAudio`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、MelBandRoFormerSampler、SaveImage、PreviewAudio、LoadAudio、JWStringMultiline、IndexTTS2Run、MelBandRoFormerModelLoader
