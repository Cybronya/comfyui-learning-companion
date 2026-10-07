---
key: comfyui-workflow-templates-json/template_sirolim_image_script_video.json
name: template_sirolim_image_script_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_sirolim_image_script_video.json
hash: 68f350f74fa386ce
official: true
coverage: 0.333333
learned_at: 2026-10-07 21:36:28
nodes: [PreviewAny, PreviewAny, PreviewAny, a03ed0e4-3a0d-41cd-aadd-b5d67704085f, c44367fd-75c5-458f-b021-73da52bf832b, df0c6995-6d81-44a3-86ef-0e3971682e89, MarkdownNote, LoadImage, PrimitiveNode, PreviewAny, GeminiNanoBanana2, PreviewImage, SaveVideo, KlingOmniProImageToVideoNode, GeminiNode]
patterns: []
missing: [a03ed0e4-3a0d-41cd-aadd-b5d67704085f, c44367fd-75c5-458f-b021-73da52bf832b, df0c6995-6d81-44a3-86ef-0e3971682e89]
discoveries: [次要节点 `a03ed0e4-3a0d-41cd-aadd-b5d67704085f` 知识库中没有该节点类型的任何知识, 次要节点 `c44367fd-75c5-458f-b021-73da52bf832b` 知识库中没有该节点类型的任何知识, 次要节点 `df0c6995-6d81-44a3-86ef-0e3971682e89` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/template_sirolim_image_script_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template_sirolim_image_script_video.json`

## 结构

**生成流程**：Output → Other

**节点**（15 个）：
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `a03ed0e4-3a0d-41cd-aadd-b5d67704085f`
- `c44367fd-75c5-458f-b021-73da52bf832b`
- `df0c6995-6d81-44a3-86ef-0e3971682e89`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveNode`
- `PreviewAny`
- `GeminiNanoBanana2`
- `PreviewImage`
- `SaveVideo`
- `KlingOmniProImageToVideoNode`
- `GeminiNode`

## 知识

覆盖率 **33%**（5/15）

**有卡**：`LoadImage`、`GeminiNanoBanana2`、`SaveVideo`、`KlingOmniProImageToVideoNode`、`GeminiNode`

**缺卡**（3）：`a03ed0e4-3a0d-41cd-aadd-b5d67704085f`、`c44367fd-75c5-458f-b021-73da52bf832b`、`df0c6995-6d81-44a3-86ef-0e3971682e89`

**用到的条目**：LoadImage、SaveVideo、GeminiNanoBanana2、GeminiNode、KlingOmniProImageToVideoNode、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `a03ed0e4-3a0d-41cd-aadd-b5d67704085f` 知识库中没有该节点类型的任何知识
- 次要节点 `c44367fd-75c5-458f-b021-73da52bf832b` 知识库中没有该节点类型的任何知识
- 次要节点 `df0c6995-6d81-44a3-86ef-0e3971682e89` 知识库中没有该节点类型的任何知识
