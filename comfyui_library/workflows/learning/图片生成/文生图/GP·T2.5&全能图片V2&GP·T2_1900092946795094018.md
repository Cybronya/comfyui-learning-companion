---
key: GP·T2.5&全能图片V2&GP·T2_1900092946795094018.json
name: GP·T2.5&全能图片V2&GP·T2_1900092946795094018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/GP·T2.5&全能图片V2&GP·T2_1900092946795094018.json
hash: 9dbc536d2b9cab10
coverage: 0.809524
learned_at: 2026-10-10 20:58:39
nodes: [LoadImage, LoadImage, SaveImage, LoadImage, LoadImage, LoadImage, RH_RhartImageG2ImageToImage, RH_Nano_Banana2_Gemini31Flash, 忽略多组孤海, LoadImage, RH_RhartImageG25SunburstImageToImage, SaveImage, LoadImage, SaveImage, JjkText, easy int, SeedVR2, SeedVR2BlockSwap, SaveImage, LoadImage, Image Comparer (rgthree)]
patterns: []
missing: [easy int, 忽略多组孤海]
discoveries: [次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# GP·T2.5&全能图片V2&GP·T2_1900092946795094018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/GP·T2.5&全能图片V2&GP·T2_1900092946795094018.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（21 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `忽略多组孤海`
- `LoadImage`
- `RH_RhartImageG25SunburstImageToImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `JjkText`
- `easy int`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`LoadImage`、`SaveImage`、`RH_RhartImageG2ImageToImage`、`RH_Nano_Banana2_Gemini31Flash`、`RH_RhartImageG25SunburstImageToImage`、`SeedVR2`、`SeedVR2BlockSwap`

**缺卡**（2）：`easy int`、`忽略多组孤海`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、SaveImage、RH_Nano_Banana2_Gemini31Flash、RH_RhartImageG25SunburstImageToImage、RH_RhartImageG2ImageToImage、sd15-t2i-basic

## 学习发现

- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
