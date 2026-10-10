---
key: 视频生成/文生视频/(贞贞AI工坊)全能视频V3.1文生视频特价版（基准0.3元_8S）_1980613635166916610.json
name: (贞贞AI工坊)全能视频V3.1文生视频特价版（基准0.3元_8S）_1980613635166916610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(贞贞AI工坊)全能视频V3.1文生视频特价版（基准0.3元_8S）_1980613635166916610.json
hash: 9dbd3dcfc004fd5a
coverage: 0.357143
learned_at: 2026-10-11 02:44:59
nodes: [easy showAnything, PrimitiveNode, Note, easy showAnything, Note, Note, Note, Note, Comfly_Googel_Veo3, SaveVideo, CR Prompt Text, SaveImage, LoadImage, Comfly_api_set]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(贞贞AI工坊)全能视频V3.1文生视频特价版（基准0.3元_8S）_1980613635166916610.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(贞贞AI工坊)全能视频V3.1文生视频特价版（基准0.3元_8S）_1980613635166916610.json`

## 结构

**生成流程**：Output → Other

**节点**（14 个）：
- `easy showAnything`
- `PrimitiveNode`
- `Note`
- `easy showAnything`
- `Note`
- `Note`
- `Note`
- `Note`
- `Comfly_Googel_Veo3`
- `SaveVideo`
- `CR Prompt Text`
- `SaveImage`
- `LoadImage`
- `Comfly_api_set`

## 知识

覆盖率 **36%**（5/14）

**有卡**：`Comfly_Googel_Veo3`、`SaveVideo`、`SaveImage`、`LoadImage`、`Comfly_api_set`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveImage、SaveVideo、Comfly_api_set、Comfly_Googel_Veo3、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
