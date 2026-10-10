---
key: comfyui-workflow-templates-json/api_bytedance_seedream_5_0_layer_separation.json
name: api_bytedance_seedream_5_0_layer_separation
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_bytedance_seedream_5_0_layer_separation.json
hash: a0758965e3e502cc
official: true
coverage: 0.777778
learned_at: 2026-10-10 22:43:37
nodes: [LoadImage, BatchImagesNode, BatchMasksNode, SaveImageAdvanced, Note, ImageCompositor, JoinImageWithAlpha, ByteDanceSeedreamLayerSeparationNodeV2, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_bytedance_seedream_5_0_layer_separation.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_bytedance_seedream_5_0_layer_separation.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `LoadImage`
- `BatchImagesNode`
- `BatchMasksNode`
- `SaveImageAdvanced`
- `Note`
- `ImageCompositor`
- `JoinImageWithAlpha`
- `ByteDanceSeedreamLayerSeparationNodeV2`
- `MarkdownNote`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`LoadImage`、`BatchImagesNode`、`BatchMasksNode`、`SaveImageAdvanced`、`ImageCompositor`、`JoinImageWithAlpha`、`ByteDanceSeedreamLayerSeparationNodeV2`

**用到的条目**：LoadImage、ByteDanceSeedreamLayerSeparationNodeV2、SaveImageAdvanced、BatchImagesNode、JoinImageWithAlpha、BatchMasksNode、ImageCompositor、sd15-t2i-basic
