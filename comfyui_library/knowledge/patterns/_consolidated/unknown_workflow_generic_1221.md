---
name: unknown_workflow_generic_1221
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7335
common_nodes: [GetImageSize, GetVideoComponents, LoadImage, LoadVideo, PreviewAny, SaveVideo, Video Slice]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_beeble_switchx_video_edit.json, comfyui-workflow-templates-json/video_bernini_r_video_editing.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1221

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/api_beeble_switchx_video_edit.json、comfyui-workflow-templates-json/video_bernini_r_video_editing.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize`
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `PreviewAny`
- `SaveVideo`
- `Video Slice`

**可变部分**（部分 workflow 才有）：
- `69c3c422-bcfe-4955-bc23-8bac307287a8` —— 1/2 个有
- `BatchImagesNode` —— 1/2 个有
- `BeebleSwitchXVideoEdit` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
