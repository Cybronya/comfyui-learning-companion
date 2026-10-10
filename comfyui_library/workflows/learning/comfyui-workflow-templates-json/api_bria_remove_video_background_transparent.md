---
key: comfyui-workflow-templates-json/api_bria_remove_video_background_transparent.json
name: api_bria_remove_video_background_transparent
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bria_remove_video_background_transparent.json
hash: a9a2c93d63339455
official: true
coverage: 1
learned_at: 2026-10-10 22:43:25
nodes: [BriaTransparentVideoBackground, LoadVideo, JoinImageWithAlpha, SaveWEBM, GetVideoComponents]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bria_remove_video_background_transparent.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bria_remove_video_background_transparent.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（5 个）：
- `BriaTransparentVideoBackground`
- `LoadVideo`
- `JoinImageWithAlpha`
- `SaveWEBM`
- `GetVideoComponents`

## 知识

覆盖率 **100%**（5/5）

**有卡**：`BriaTransparentVideoBackground`、`LoadVideo`、`JoinImageWithAlpha`、`SaveWEBM`、`GetVideoComponents`

**用到的条目**：SaveWEBM、GetVideoComponents、JoinImageWithAlpha、LoadVideo、BriaTransparentVideoBackground、sd15-t2i-basic、sd15-t2i-lora、SaveImage
