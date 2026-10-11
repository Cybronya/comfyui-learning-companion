---
key: 视频生成/文生视频/Seedance2.5 文生视频工作流+全节点注释_2085924053302464514.json
name: Seedance2.5 文生视频工作流+全节点注释_2085924053302464514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.5 文生视频工作流+全节点注释_2085924053302464514.json
hash: 1ce543047e13b0ff
coverage: 0.4
learned_at: 2026-10-11 20:53:47
nodes: [SaveVideo, RH_BytedanceSeedance25TokenTextToVideo, JjkText, CR Text, Note, Note, Note, LoadImage, LoadImage, Note]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Seedance2.5 文生视频工作流+全节点注释_2085924053302464514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.5 文生视频工作流+全节点注释_2085924053302464514.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `SaveVideo`
- `RH_BytedanceSeedance25TokenTextToVideo`
- `JjkText`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`

## 知识

覆盖率 **40%**（4/10）

**有卡**：`SaveVideo`、`RH_BytedanceSeedance25TokenTextToVideo`、`LoadImage`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance25TokenTextToVideo、SaveVideo、sd15-t2i-basic、sd15-t2i-lora、Seed、Text、sampler_name 调整经验

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
