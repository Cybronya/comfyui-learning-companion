---
key: 视频生成/文生视频/(贞贞AI工坊)全能视频V3.1 Pro文生视频特价版（基准1元_8S）_1980614790232064001.json
name: (贞贞AI工坊)全能视频V3.1 Pro文生视频特价版（基准1元_8S）_1980614790232064001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(贞贞AI工坊)全能视频V3.1 Pro文生视频特价版（基准1元_8S）_1980614790232064001.json
hash: 45506bb415b61a17
coverage: 0.357143
learned_at: 2026-10-11 02:44:59
nodes: [easy showAnything, PrimitiveNode, easy showAnything, Note, Note, Note, Note, Note, SaveVideo, Comfly_Googel_Veo3, CR Prompt Text, Comfly_api_set, HfSaveImage, LoadImage]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(贞贞AI工坊)全能视频V3.1 Pro文生视频特价版（基准1元_8S）_1980614790232064001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(贞贞AI工坊)全能视频V3.1 Pro文生视频特价版（基准1元_8S）_1980614790232064001.json`

## 结构

**生成流程**：Output → Other

**节点**（14 个）：
- `easy showAnything`
- `PrimitiveNode`
- `easy showAnything`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SaveVideo`
- `Comfly_Googel_Veo3`
- `CR Prompt Text`
- `Comfly_api_set`
- `HfSaveImage`
- `LoadImage`

## 知识

覆盖率 **36%**（5/14）

**有卡**：`SaveVideo`、`Comfly_Googel_Veo3`、`Comfly_api_set`、`HfSaveImage`、`LoadImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、HfSaveImage、Comfly_api_set、Comfly_Googel_Veo3、sd15-t2i-basic、sd15-t2i-lora、SaveImage

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
