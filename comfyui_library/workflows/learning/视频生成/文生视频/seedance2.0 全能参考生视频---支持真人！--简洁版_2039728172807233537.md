---
key: 视频生成/文生视频/seedance2.0 全能参考生视频---支持真人！--简洁版_2039728172807233537.json
name: seedance2.0 全能参考生视频---支持真人！--简洁版_2039728172807233537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/seedance2.0 全能参考生视频---支持真人！--简洁版_2039728172807233537.json
hash: 80d83a3b19478097
coverage: 0.555556
learned_at: 2026-10-11 19:49:44
nodes: [easy showAnything, LoadImage, LoadAudio, LoadVideo, SaveVideo, easy showAnything, CR Prompt Text, RH_RhartVideoSparkvideo20MultimodalVideo, Note]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/seedance2.0 全能参考生视频---支持真人！--简洁版_2039728172807233537.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/seedance2.0 全能参考生视频---支持真人！--简洁版_2039728172807233537.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `easy showAnything`
- `LoadImage`
- `LoadAudio`
- `LoadVideo`
- `SaveVideo`
- `easy showAnything`
- `CR Prompt Text`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `Note`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`LoadImage`、`LoadAudio`、`LoadVideo`、`SaveVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
