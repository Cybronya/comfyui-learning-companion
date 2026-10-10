---
key: comfyui-workflow-templates-json/templates-product_ad-v2.0.json
name: templates-product_ad-v2.0
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/templates-product_ad-v2.0.json
hash: 6a0cd63334b4e365
official: true
coverage: 0.8
learned_at: 2026-10-10 22:49:24
nodes: [ImageBatch, LoadImage, LoadImage, GetImageSize, ResizeAndPadImage, PrimitiveStringMultiline, RegexReplace, PrimitiveStringMultiline, SaveImage, GeminiImage2Node]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/templates-product_ad-v2.0.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/templates-product_ad-v2.0.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `ImageBatch`
- `LoadImage`
- `LoadImage`
- `GetImageSize`
- `ResizeAndPadImage`
- `PrimitiveStringMultiline`
- `RegexReplace`
- `PrimitiveStringMultiline`
- `SaveImage`
- `GeminiImage2Node`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`ImageBatch`、`LoadImage`、`GetImageSize`、`ResizeAndPadImage`、`RegexReplace`、`SaveImage`、`GeminiImage2Node`

**用到的条目**：LoadImage、GetImageSize、ResizeAndPadImage、GetImageSize、SaveImage、RegexReplace、ImageBatch、ImageBatch
