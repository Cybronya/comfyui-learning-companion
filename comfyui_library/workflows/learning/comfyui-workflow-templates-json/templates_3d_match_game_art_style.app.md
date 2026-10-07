---
key: comfyui-workflow-templates-json/templates_3d_match_game_art_style.app.json
name: templates_3d_match_game_art_style.app
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/templates_3d_match_game_art_style.app.json
hash: 2d29bcdb28266c75
official: true
coverage: 0.769231
learned_at: 2026-10-07 21:36:37
nodes: [RecraftRemoveBackgroundNode, PrimitiveStringMultiline, StringConcatenate, PrimitiveStringMultiline, StringConcatenate, LoadImage, BatchImagesNode, GeminiImage2Node, LoadImage, ImageCompare, SaveImage, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/templates_3d_match_game_art_style.app.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/templates_3d_match_game_art_style.app.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `RecraftRemoveBackgroundNode`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `LoadImage`
- `BatchImagesNode`
- `GeminiImage2Node`
- `LoadImage`
- `ImageCompare`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`RecraftRemoveBackgroundNode`、`StringConcatenate`、`LoadImage`、`BatchImagesNode`、`GeminiImage2Node`、`ImageCompare`、`SaveImage`

**用到的条目**：LoadImage、SaveImage、BatchImagesNode、StringConcatenate、GeminiImage2Node、ImageCompare、RecraftRemoveBackgroundNode、sd15-t2i-basic
