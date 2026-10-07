---
key: comfyui-workflow-templates-json/video_ltx2_depth_to_video.json
name: video_ltx2_depth_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_depth_to_video.json
hash: a385cb63d253954e
official: true
coverage: 0.526316
learned_at: 2026-10-07 21:37:06
nodes: [ImageFromBatch, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, PreviewImage, SaveVideo, SaveVideo, PrimitiveInt, ResizeImageMaskNode, GetVideoComponents, LoadVideo, MarkdownNote, LoadImage, PrimitiveBoolean, MarkdownNote, 4ba16137-671b-4a0a-9b09-fff1ba6ac7d8, ImageScaleBy, 68857357-cbc2-4c3a-a786-c3a58d43f9b1, db5e983e-7d97-4014-b3b3-33a61ee67ddf]
patterns: []
missing: [4ba16137-671b-4a0a-9b09-fff1ba6ac7d8, 68857357-cbc2-4c3a-a786-c3a58d43f9b1, db5e983e-7d97-4014-b3b3-33a61ee67ddf]
discoveries: [次要节点 `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8` 知识库中没有该节点类型的任何知识, 次要节点 `68857357-cbc2-4c3a-a786-c3a58d43f9b1` 知识库中没有该节点类型的任何知识, 次要节点 `db5e983e-7d97-4014-b3b3-33a61ee67ddf` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_ltx2_depth_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_depth_to_video.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PreviewImage`
- `SaveVideo`
- `SaveVideo`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `GetVideoComponents`
- `LoadVideo`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveBoolean`
- `MarkdownNote`
- `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8`
- `ImageScaleBy`
- `68857357-cbc2-4c3a-a786-c3a58d43f9b1`
- `db5e983e-7d97-4014-b3b3-33a61ee67ddf`

## 知识

覆盖率 **53%**（10/19）

**有卡**：`ImageFromBatch`、`ResizeImageMaskNode`、`SaveVideo`、`GetVideoComponents`、`LoadVideo`、`LoadImage`、`PrimitiveBoolean`、`ImageScaleBy`

**缺卡**（3）：`4ba16137-671b-4a0a-9b09-fff1ba6ac7d8`、`68857357-cbc2-4c3a-a786-c3a58d43f9b1`、`db5e983e-7d97-4014-b3b3-33a61ee67ddf`

**用到的条目**：LoadImage、ResizeImageMaskNode、SaveVideo、GetVideoComponents、ImageFromBatch、ImageScaleBy、LoadVideo、PrimitiveBoolean

## 学习发现

- 次要节点 `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8` 知识库中没有该节点类型的任何知识
- 次要节点 `68857357-cbc2-4c3a-a786-c3a58d43f9b1` 知识库中没有该节点类型的任何知识
- 次要节点 `db5e983e-7d97-4014-b3b3-33a61ee67ddf` 知识库中没有该节点类型的任何知识
