---
key: 视频生成/文生视频/全能参考视频生成！Seedance 2.0 支持原生1080p！可真人，审核宽松！_2067456511793778689.json
name: 全能参考视频生成！Seedance 2.0 支持原生1080p！可真人，审核宽松！_2067456511793778689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能参考视频生成！Seedance 2.0 支持原生1080p！可真人，审核宽松！_2067456511793778689.json
hash: 17f01e703df1acaf
coverage: 0.619048
learned_at: 2026-10-11 20:21:33
nodes: [ShowAnything|Mie, ShowAnything|Mie, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, LoadImage, LoadImage, LoadVideo, LoadAudio, 忽略多组孤海, MarkdownNote, MarkdownNote, CR Prompt Text, RH_RhartVideoSparkvideo20MultimodalVideo, MarkdownNote, SaveVideo, LoadAudio]
patterns: []
missing: [ShowAnything|Mie, ShowAnything|Mie, 忽略多组孤海, CR Prompt Text]
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能参考视频生成！Seedance 2.0 支持原生1080p！可真人，审核宽松！_2067456511793778689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能参考视频生成！Seedance 2.0 支持原生1080p！可真人，审核宽松！_2067456511793778689.json`

## 结构

**生成流程**：Output → Other

**节点**（21 个）：
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadAudio`
- `忽略多组孤海`
- `MarkdownNote`
- `MarkdownNote`
- `CR Prompt Text`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `MarkdownNote`
- `SaveVideo`
- `LoadAudio`

## 知识

覆盖率 **62%**（13/21）

**有卡**：`LoadImage`、`LoadVideo`、`LoadAudio`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`SaveVideo`

**缺卡**（4）：`ShowAnything|Mie`、`ShowAnything|Mie`、`忽略多组孤海`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
