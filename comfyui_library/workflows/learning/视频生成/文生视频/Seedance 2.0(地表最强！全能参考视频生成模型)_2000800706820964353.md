---
key: 视频生成/文生视频/Seedance 2.0(地表最强！全能参考视频生成模型)_2000800706820964353.json
name: Seedance 2.0(地表最强！全能参考视频生成模型)_2000800706820964353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance 2.0(地表最强！全能参考视频生成模型)_2000800706820964353.json
hash: 1ebd75412a3b0e82
coverage: 0.666667
learned_at: 2026-10-11 02:57:37
nodes: [MarkdownNote, ShowAnything|Mie, ShowAnything|Mie, SaveVideo, CR Prompt Text, RH_RhartVideoSparkvideo20MultimodalVideo, LoadAudio, LoadVideo, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: [ShowAnything|Mie, ShowAnything|Mie, CR Prompt Text]
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Seedance 2.0(地表最强！全能参考视频生成模型)_2000800706820964353.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance 2.0(地表最强！全能参考视频生成模型)_2000800706820964353.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `MarkdownNote`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `SaveVideo`
- `CR Prompt Text`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `LoadAudio`
- `LoadVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **67%**（8/12）

**有卡**：`SaveVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`LoadAudio`、`LoadVideo`、`LoadImage`

**缺卡**（3）：`ShowAnything|Mie`、`ShowAnything|Mie`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
