---
name: unknown_workflow_generic_1190
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.684
common_nodes: [4ba16137-671b-4a0a-9b09-fff1ba6ac7d8, 68857357-cbc2-4c3a-a786-c3a58d43f9b1, GetVideoComponents, ImageFromBatch, ImageScaleBy, LoadImage, LoadVideo, PreviewImage, PrimitiveBoolean, PrimitiveInt, ResizeImageMaskNode, SaveVideo]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_ltx2_canny_to_video.json, comfyui-workflow-templates-json/video_ltx2_depth_to_video.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1190

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/video_ltx2_canny_to_video.json、comfyui-workflow-templates-json/video_ltx2_depth_to_video.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `4ba16137-671b-4a0a-9b09-fff1ba6ac7d8`
- `68857357-cbc2-4c3a-a786-c3a58d43f9b1`
- `GetVideoComponents`
- `ImageFromBatch`
- `ImageScaleBy`
- `LoadImage`
- `LoadVideo`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 1/2 个有
- `db5e983e-7d97-4014-b3b3-33a61ee67ddf` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
