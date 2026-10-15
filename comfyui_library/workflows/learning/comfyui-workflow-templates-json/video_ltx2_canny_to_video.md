---
key: comfyui-workflow-templates-json/video_ltx2_canny_to_video.json
name: video_ltx2_canny_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_ltx2_canny_to_video.json
hash: 68e5cb0ecfff5e11
official: true
coverage: 0.684211
learned_at: 2026-10-15 22:24:57
nodes: [Canny, GetVideoComponents, ImageFromBatch, ResizeImageMaskNode, ResizeImageMaskNode, PrimitiveInt, ImageScaleBy, MarkdownNote, LoadVideo, LoadImage, PreviewImage, SaveVideo, PrimitiveInt, MarkdownNote, PrimitiveInt, SaveVideo, PrimitiveBoolean, 68857357-cbc2-4c3a-a786-c3a58d43f9b1, 4ba16137-671b-4a0a-9b09-fff1ba6ac7d8]
patterns: []
missing: []
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

覆盖率 **68%**（13/19）

**有卡**：`Canny`、`GetVideoComponents`、`ImageFromBatch`、`ResizeImageMaskNode`、`ImageScaleBy`、`LoadVideo`、`LoadImage`、`SaveVideo`、`PrimitiveBoolean`、`68857357-cbc2-4c3a-a786-c3a58d43f9b1`、`4ba16137-671b-4a0a-9b09-fff1ba6ac7d8`

**用到的条目**：LoadImage、Canny、ResizeImageMaskNode、SaveVideo、GetVideoComponents、ImageFromBatch、ImageScaleBy、LoadVideo
