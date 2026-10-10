---
key: 视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 25S新文生视频V1（可选横竖屏频-基准价格1.7元）_1979390287166476289.json
name: (Ai贞贞工坊版)全能视频S Pro 25S新文生视频V1（可选横竖屏频-基准价格1.7元）_1979390287166476289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 25S新文生视频V1（可选横竖屏频-基准价格1.7元）_1979390287166476289.json
hash: 44e46bdd6bf75176
coverage: 0.416667
learned_at: 2026-10-10 22:58:00
nodes: [easy showAnything, easy showAnything, Note, CR Prompt Text, Note, SaveVideo, Comfly_sora2, Note, Comfly_api_set, Note, SaveImage, LoadImage]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 25S新文生视频V1（可选横竖屏频-基准价格1.7元）_1979390287166476289.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 25S新文生视频V1（可选横竖屏频-基准价格1.7元）_1979390287166476289.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `easy showAnything`
- `easy showAnything`
- `Note`
- `CR Prompt Text`
- `Note`
- `SaveVideo`
- `Comfly_sora2`
- `Note`
- `Comfly_api_set`
- `Note`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **42%**（5/12）

**有卡**：`SaveVideo`、`Comfly_sora2`、`Comfly_api_set`、`SaveImage`、`LoadImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveImage、SaveVideo、Comfly_api_set、Comfly_sora2、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
