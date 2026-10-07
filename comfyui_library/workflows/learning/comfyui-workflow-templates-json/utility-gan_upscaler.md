---
key: comfyui-workflow-templates-json/utility-gan_upscaler.json
name: utility-gan_upscaler
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility-gan_upscaler.json
hash: 7df9fb1b355252bc
official: true
coverage: 0.857143
learned_at: 2026-10-07 21:36:41
nodes: [LoadVideo, ImageUpscaleWithModel, CreateVideo, GetVideoComponents, UpscaleModelLoader, SaveVideo, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/utility-gan_upscaler.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility-gan_upscaler.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（7 个）：
- `LoadVideo`
- `ImageUpscaleWithModel`
- `CreateVideo`
- `GetVideoComponents`
- `UpscaleModelLoader`
- `SaveVideo`
- `MarkdownNote`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`LoadVideo`、`ImageUpscaleWithModel`、`CreateVideo`、`GetVideoComponents`、`UpscaleModelLoader`、`SaveVideo`

**用到的条目**：ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader、SaveVideo、CreateVideo、GetVideoComponents、LoadVideo、sd15-t2i-basic
