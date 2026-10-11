---
key: 视频生成/文生视频/全能参考视频生成！Seedance 2.0(已支持原生1080p！可真人，审核宽松！_2048398173965651969.json
name: 全能参考视频生成！Seedance 2.0(已支持原生1080p！可真人，审核宽松！_2048398173965651969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能参考视频生成！Seedance 2.0(已支持原生1080p！可真人，审核宽松！_2048398173965651969.json
hash: e87b2d0bb422a5c6
coverage: 0.6
learned_at: 2026-10-11 19:49:46
nodes: [ShowAnything|Mie, ShowAnything|Mie, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, Fast Groups Bypasser (rgthree), LoadVideo, LoadImage, CR Prompt Text, RH_RhartVideoSparkvideo20MultimodalVideo, MarkdownNote, SaveVideo]
patterns: []
missing: [ShowAnything|Mie, ShowAnything|Mie, CR Prompt Text]
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能参考视频生成！Seedance 2.0(已支持原生1080p！可真人，审核宽松！_2048398173965651969.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能参考视频生成！Seedance 2.0(已支持原生1080p！可真人，审核宽松！_2048398173965651969.json`

## 结构

**生成流程**：Output → Other

**节点**（20 个）：
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadVideo`
- `LoadImage`
- `CR Prompt Text`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `MarkdownNote`
- `SaveVideo`

## 知识

覆盖率 **60%**（12/20）

**有卡**：`LoadAudio`、`LoadImage`、`LoadVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`SaveVideo`

**缺卡**（3）：`ShowAnything|Mie`、`ShowAnything|Mie`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
