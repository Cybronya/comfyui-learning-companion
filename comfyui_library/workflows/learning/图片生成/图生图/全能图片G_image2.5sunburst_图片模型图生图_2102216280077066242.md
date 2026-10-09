---
key: 图片生成/图生图/全能图片G_image2.5sunburst_图片模型图生图_2102216280077066242.json
name: 全能图片G_image2.5sunburst_图片模型图生图_2102216280077066242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片G_image2.5sunburst_图片模型图生图_2102216280077066242.json
hash: 6d9018ef12ef4fd5
coverage: 0.777778
learned_at: 2026-10-09 22:27:09
nodes: [easy saveText, LoadImage, LoadImage, LoadImage, SaveImage, LoadImage, RH_RhartImageG25OfficialTokenSunburstEdit, JjkText, LoadImage]
patterns: []
missing: [easy saveText]
discoveries: [次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/全能图片G_image2.5sunburst_图片模型图生图_2102216280077066242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102216280077066242.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `easy saveText`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `RH_RhartImageG25OfficialTokenSunburstEdit`
- `JjkText`
- `LoadImage`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`LoadImage`、`SaveImage`、`RH_RhartImageG25OfficialTokenSunburstEdit`

**缺卡**（1）：`easy saveText`

**用到的条目**：LoadImage、SaveImage、RH_RhartImageG25OfficialTokenSunburstEdit、sd15-t2i-basic、sd15-t2i-lora、SaveText、Text、CS_Preview_Any

## 学习发现

- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
