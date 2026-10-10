---
key: 视频生成/文生视频/Wan2.5 文生视频-自动提示词_1971456908559368193.json
name: Wan2.5 文生视频-自动提示词_1971456908559368193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.5 文生视频-自动提示词_1971456908559368193.json
hash: 34084d713b205a4a
coverage: 0.625
learned_at: 2026-10-10 23:08:10
nodes: [SaveVideo, SaveImage, MarkdownNote, easy ifElse, CR Text Replace, LoadAudio, LoadImage, RH_Wan25_T2V, TextBox, easy showAnything, easy cleanGpuUsed, RH_Prompter, easy showAnything, PrimitiveBoolean, TextBox, TextBox]
patterns: []
missing: [CR Text Replace, easy cleanGpuUsed]
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.5 文生视频-自动提示词_1971456908559368193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.5 文生视频-自动提示词_1971456908559368193.json`

## 结构

**生成流程**：Output → Other

**节点**（16 个）：
- `SaveVideo`
- `SaveImage`
- `MarkdownNote`
- `easy ifElse`
- `CR Text Replace`
- `LoadAudio`
- `LoadImage`
- `RH_Wan25_T2V`
- `TextBox`
- `easy showAnything`
- `easy cleanGpuUsed`
- `RH_Prompter`
- `easy showAnything`
- `PrimitiveBoolean`
- `TextBox`
- `TextBox`

## 知识

覆盖率 **62%**（10/16）

**有卡**：`SaveVideo`、`SaveImage`、`LoadAudio`、`LoadImage`、`RH_Wan25_T2V`、`TextBox`、`RH_Prompter`、`PrimitiveBoolean`

**缺卡**（2）：`CR Text Replace`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、RH_Prompter、SaveImage、SaveVideo、LoadAudio、PrimitiveBoolean、Textbox、TextBox

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
