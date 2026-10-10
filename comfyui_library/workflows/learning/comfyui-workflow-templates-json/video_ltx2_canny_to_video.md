---
key: comfyui-workflow-templates-json/video_ltx2_canny_to_video.json
name: video_ltx2_canny_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_canny_to_video.json
hash: 68e5cb0ecfff5e11
official: true
coverage: 0.578947
learned_at: 2026-10-10 22:50:21
nodes: [Canny, GetVideoComponents, ImageFromBatch, ResizeImageMaskNode, ResizeImageMaskNode, PrimitiveInt, ImageScaleBy, MarkdownNote, LoadVideo, LoadImage, PreviewImage, SaveVideo, PrimitiveInt, MarkdownNote, PrimitiveInt, SaveVideo, PrimitiveBoolean, 68857357-cbc2-4c3a-a786-c3a58d43f9b1, 4ba16137-671b-4a0a-9b09-fff1ba6ac7d8]
patterns: []
missing: [4ba16137-671b-4a0a-9b09-fff1ba6ac7d8, 68857357-cbc2-4c3a-a786-c3a58d43f9b1]
discoveries: [次要节点 `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8` 知识库中没有该节点类型的任何知识, 次要节点 `68857357-cbc2-4c3a-a786-c3a58d43f9b1` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_ltx2_canny_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_canny_to_video.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `Canny`
- `GetVideoComponents`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `ImageScaleBy`
- `MarkdownNote`
- `LoadVideo`
- `LoadImage`
- `PreviewImage`
- `SaveVideo`
- `PrimitiveInt`
- `MarkdownNote`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveBoolean`
- `68857357-cbc2-4c3a-a786-c3a58d43f9b1`
- `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8`

## 知识

覆盖率 **58%**（11/19）

**有卡**：`Canny`、`GetVideoComponents`、`ImageFromBatch`、`ResizeImageMaskNode`、`ImageScaleBy`、`LoadVideo`、`LoadImage`、`SaveVideo`、`PrimitiveBoolean`

**缺卡**（2）：`4ba16137-671b-4a0a-9b09-fff1ba6ac7d8`、`68857357-cbc2-4c3a-a786-c3a58d43f9b1`

**用到的条目**：LoadImage、Canny、ResizeImageMaskNode、SaveVideo、GetVideoComponents、ImageFromBatch、ImageScaleBy、LoadVideo

## 学习发现

- 次要节点 `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8` 知识库中没有该节点类型的任何知识
- 次要节点 `68857357-cbc2-4c3a-a786-c3a58d43f9b1` 知识库中没有该节点类型的任何知识
