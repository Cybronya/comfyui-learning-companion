---
key: 图片生成/反推提示词/全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090.json
name: 全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090.json
hash: 8ba315b7968341b3
coverage: 0.5
learned_at: 2026-10-06 21:38:13
nodes: [SaveImage, PreviewImage, SaveImage, PreviewImage, RH_RhartImageG25OfficialTokenFlareEdit, LoadImage, LoadImage, LoadImage, LoadImage, RH_RhartImageG25OfficialTokenSunburstTextToImage, 忽略多组孤海, 忽略多组孤海]
patterns: []
missing: [RH_RhartImageG25OfficialTokenFlareEdit, RH_RhartImageG25OfficialTokenSunburstTextToImage, 忽略多组孤海, 忽略多组孤海]
discoveries: [次要节点 `RH_RhartImageG25OfficialTokenFlareEdit` 知识库中没有该节点类型的任何知识, 次要节点 `RH_RhartImageG25OfficialTokenSunburstTextToImage` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/反推提示词/全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `RH_RhartImageG25OfficialTokenFlareEdit`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG25OfficialTokenSunburstTextToImage`
- `忽略多组孤海`
- `忽略多组孤海`

## 知识

覆盖率 **50%**（6/12）

**有卡**：`SaveImage`、`LoadImage`

**缺卡**（4）：`RH_RhartImageG25OfficialTokenFlareEdit`、`RH_RhartImageG25OfficialTokenSunburstTextToImage`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：LoadImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `RH_RhartImageG25OfficialTokenFlareEdit` 知识库中没有该节点类型的任何知识
- 次要节点 `RH_RhartImageG25OfficialTokenSunburstTextToImage` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
