---
key: comfyui-workflow-templates-json/template_rob_realistic_2k_images_quick_variations.json
name: template_rob_realistic_2k_images_quick_variations
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_rob_realistic_2k_images_quick_variations.json
hash: 6eb4a34dc0560fab
official: true
coverage: 0.625
learned_at: 2026-10-10 22:49:08
nodes: [LoadImage, ImageCompare, SaveImage, c19ae9b8-d43c-40d3-8ae7-eea7d345a587, SaveImage, 010af74f-5a21-43f4-b520-14374608c312, GrokImageNode, PreviewAny]
patterns: []
missing: [010af74f-5a21-43f4-b520-14374608c312, c19ae9b8-d43c-40d3-8ae7-eea7d345a587]
discoveries: [次要节点 `010af74f-5a21-43f4-b520-14374608c312` 知识库中没有该节点类型的任何知识, 次要节点 `c19ae9b8-d43c-40d3-8ae7-eea7d345a587` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/template_rob_realistic_2k_images_quick_variations.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template_rob_realistic_2k_images_quick_variations.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `LoadImage`
- `ImageCompare`
- `SaveImage`
- `c19ae9b8-d43c-40d3-8ae7-eea7d345a587`
- `SaveImage`
- `010af74f-5a21-43f4-b520-14374608c312`
- `GrokImageNode`
- `PreviewAny`

## 知识

覆盖率 **62%**（5/8）

**有卡**：`LoadImage`、`ImageCompare`、`SaveImage`、`GrokImageNode`

**缺卡**（2）：`010af74f-5a21-43f4-b520-14374608c312`、`c19ae9b8-d43c-40d3-8ae7-eea7d345a587`

**用到的条目**：LoadImage、SaveImage、GrokImageNode、ImageCompare、sd15-t2i-basic、sd15-t2i-lora、node、ki

## 学习发现

- 次要节点 `010af74f-5a21-43f4-b520-14374608c312` 知识库中没有该节点类型的任何知识
- 次要节点 `c19ae9b8-d43c-40d3-8ae7-eea7d345a587` 知识库中没有该节点类型的任何知识
