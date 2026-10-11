---
key: 视频生成/文生视频/seedance2.0 mini图生视频_2070010907375259649.json
name: seedance2.0 mini图生视频_2070010907375259649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/seedance2.0 mini图生视频_2070010907375259649.json
hash: 4794bb1344c10e47
coverage: 0.375
learned_at: 2026-10-11 20:21:32
nodes: [RH_RhartVideoSparkvideo20MiniImageToVideo, SaveVideo, LoadImage, PrimitiveNode, PrimitiveNode, PrimitiveNode, CR Text, MarkdownNote]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/seedance2.0 mini图生视频_2070010907375259649.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/seedance2.0 mini图生视频_2070010907375259649.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `RH_RhartVideoSparkvideo20MiniImageToVideo`
- `SaveVideo`
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `CR Text`
- `MarkdownNote`

## 知识

覆盖率 **38%**（3/8）

**有卡**：`RH_RhartVideoSparkvideo20MiniImageToVideo`、`SaveVideo`、`LoadImage`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、SaveVideo、RH_RhartVideoSparkvideo20MiniImageToVideo、sd15-t2i-basic、sd15-t2i-lora、node、Text、SaveImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
