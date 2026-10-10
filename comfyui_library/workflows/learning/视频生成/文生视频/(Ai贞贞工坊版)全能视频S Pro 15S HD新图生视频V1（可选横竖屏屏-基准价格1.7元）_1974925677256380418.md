---
key: 视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新图生视频V1（可选横竖屏屏-基准价格1.7元）_1974925677256380418.json
name: (Ai贞贞工坊版)全能视频S Pro 15S HD新图生视频V1（可选横竖屏屏-基准价格1.7元）_1974925677256380418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新图生视频V1（可选横竖屏屏-基准价格1.7元）_1974925677256380418.json
hash: c1201ff0951c257c
coverage: 0.416667
learned_at: 2026-10-10 22:57:58
nodes: [easy showAnything, Note, SaveImage, easy showAnything, CR Prompt Text, LoadImage, Note, Comfly_sora2, Note, SaveVideo, Note, Comfly_api_set]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新图生视频V1（可选横竖屏屏-基准价格1.7元）_1974925677256380418.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(Ai贞贞工坊版)全能视频S Pro 15S HD新图生视频V1（可选横竖屏屏-基准价格1.7元）_1974925677256380418.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `easy showAnything`
- `Note`
- `SaveImage`
- `easy showAnything`
- `CR Prompt Text`
- `LoadImage`
- `Note`
- `Comfly_sora2`
- `Note`
- `SaveVideo`
- `Note`
- `Comfly_api_set`

## 知识

覆盖率 **42%**（5/12）

**有卡**：`SaveImage`、`LoadImage`、`Comfly_sora2`、`SaveVideo`、`Comfly_api_set`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveImage、SaveVideo、Comfly_api_set、Comfly_sora2、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
