---
key: 视频生成/文生视频/👾怪獸-最强视频模型Seedance2.0全参工作流👾_2047322708756664322.json
name: 👾怪獸-最强视频模型Seedance2.0全参工作流👾_2047322708756664322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/👾怪獸-最强视频模型Seedance2.0全参工作流👾_2047322708756664322.json
hash: ced8c3cdd4b79548
coverage: 0.85
learned_at: 2026-10-11 19:49:52
nodes: [LoadVideo, LoadVideo, LoadVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, SaveVideo, PreviewAny, RH_RhartVideoSparkvideo20MultimodalVideo, PreviewAny, CR Text]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/👾怪獸-最强视频模型Seedance2.0全参工作流👾_2047322708756664322.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/👾怪獸-最强视频模型Seedance2.0全参工作流👾_2047322708756664322.json`

## 结构

**生成流程**：Output → Other

**节点**（20 个）：
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `SaveVideo`
- `PreviewAny`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `PreviewAny`
- `CR Text`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`LoadVideo`、`LoadImage`、`LoadAudio`、`SaveVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
