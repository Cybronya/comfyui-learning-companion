---
name: unknown_workflow_controlnet_face_detailer_clip
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.896
common_nodes: [ApplyEcomIDAdvanced, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EcomIDFaceAnalysis, EcomID_PulidModelLoader, FaceDetailer, LoadImage, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/图生图/ECOMID最强一键换脸_1906692970094153729.json, 图片生成/图生图/SDXL ECOMID最强一键换脸_1912030837712584706.json, 平台全量/EcomID 高清换脸丨极高相似度EcomID 换脸_1912425718477979650.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_face_detailer_clip

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/ECOMID最强一键换脸_1906692970094153729.json、图片生成/图生图/SDXL ECOMID最强一键换脸_1912030837712584706.json、平台全量/EcomID 高清换脸丨极高相似度EcomID 换脸_1912425718477979650.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyEcomIDAdvanced`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EcomIDFaceAnalysis`
- `EcomID_PulidModelLoader`
- `FaceDetailer`
- `LoadImage`
- `SaveImage`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `EcomIDEvaClipLoader` —— 2/3 个有
- `InstantID_IPA_ModelLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `InstantIDModelLoader` —— 1/3 个有
- `PulidEvaClipLoader` —— 1/3 个有
- `SAMLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
