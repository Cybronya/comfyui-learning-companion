---
key: 视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新版文生视频V1（可选横竖版-基准价格1.7）_1977805810329944066.json
name: (Ai贞贞工坊版)全能视频S Pro 15S HD新版文生视频V1（可选横竖版-基准价格1.7）_1977805810329944066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新版文生视频V1（可选横竖版-基准价格1.7）_1977805810329944066.json
hash: b14d8ef0614bd74c
coverage: 0.4
learned_at: 2026-10-10 22:57:59
nodes: [LoadImage, easy showAnything, SaveVideo, easy showAnything, Note, Note, CR Prompt Text, Comfly_sora2, Note, Comfly_api_set]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新版文生视频V1（可选横竖版-基准价格1.7）_1977805810329944066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新版文生视频V1（可选横竖版-基准价格1.7）_1977805810329944066.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `LoadImage`
- `easy showAnything`
- `SaveVideo`
- `easy showAnything`
- `Note`
- `Note`
- `CR Prompt Text`
- `Comfly_sora2`
- `Note`
- `Comfly_api_set`

## 知识

覆盖率 **40%**（4/10）

**有卡**：`LoadImage`、`SaveVideo`、`Comfly_sora2`、`Comfly_api_set`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、Comfly_api_set、Comfly_sora2、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
