---
key: comfyui-workflow-templates-json/image_ideogram4_t2i.json
name: image_ideogram4_t2i
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_ideogram4_t2i.json
hash: 3137e5d520fbb721
official: true
coverage: 0.25
learned_at: 2026-10-07 21:35:44
nodes: [ResolutionSelector, 83e6e004-48ea-408e-9024-eb49c3d7dc14, MarkdownNote, MarkdownNote, PreviewAny, f5f04613-ee09-4cd9-9ada-a880360891d4, SaveImage, MarkdownNote]
patterns: []
missing: [83e6e004-48ea-408e-9024-eb49c3d7dc14, f5f04613-ee09-4cd9-9ada-a880360891d4]
discoveries: [次要节点 `83e6e004-48ea-408e-9024-eb49c3d7dc14` 知识库中没有该节点类型的任何知识, 次要节点 `f5f04613-ee09-4cd9-9ada-a880360891d4` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_ideogram4_t2i.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_ideogram4_t2i.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（8 个）：
- `ResolutionSelector`
- `83e6e004-48ea-408e-9024-eb49c3d7dc14`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewAny`
- `f5f04613-ee09-4cd9-9ada-a880360891d4`
- `SaveImage`
- `MarkdownNote`

## 知识

覆盖率 **25%**（2/8）

**有卡**：`ResolutionSelector`、`SaveImage`

**缺卡**（2）：`83e6e004-48ea-408e-9024-eb49c3d7dc14`、`f5f04613-ee09-4cd9-9ada-a880360891d4`

**用到的条目**：ResolutionSelector、SaveImage、sd15-t2i-basic、sd15-t2i-lora、EmptyLatentImage、height 调整经验、width 调整经验、easy_imagesize

## 学习发现

- 次要节点 `83e6e004-48ea-408e-9024-eb49c3d7dc14` 知识库中没有该节点类型的任何知识
- 次要节点 `f5f04613-ee09-4cd9-9ada-a880360891d4` 知识库中没有该节点类型的任何知识
