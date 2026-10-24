---
name: unknown_workflow_controlnet_face_detailer_clip
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [ApplyEcomIDAdvanced, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EcomIDEvaClipLoader, EcomIDFaceAnalysis, EcomID_PulidModelLoader, FaceDetailer, InstantID_IPA_ModelLoader, LoadImage, PreviewImage, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/图生图/ECOMID最强一键换脸_1906692970094153729.json, 图片生成/图生图/SDXL ECOMID最强一键换脸_1912030837712584706.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_face_detailer_clip

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ECOMID最强一键换脸_1906692970094153729.json、图片生成/图生图/SDXL ECOMID最强一键换脸_1912030837712584706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyEcomIDAdvanced`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EcomIDEvaClipLoader`
- `EcomIDFaceAnalysis`
- `EcomID_PulidModelLoader`
- `FaceDetailer`
- `InstantID_IPA_ModelLoader`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UltralyticsDetectorProvider`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
