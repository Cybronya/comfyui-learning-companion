---
name: unknown_workflow_controlnet_ipadapter_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.576
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, DZ_Face_Detailer, FaceAnalysisModels, FaceBoundingBox, FaceEmbedDistance, IPAdapterFaceID, IPAdapterUnifiedLoaderFaceID, ImageBatch, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, LoadImage, MaskToImage, PreviewImage, SUPIR_Upscale, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/Instant ID 4张图换脸一致_2044811630093017090.json, 平台全量/Instant ID 人脸一致_1890367471809896450.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Instant ID 4张图换脸一致_2044811630093017090.json、平台全量/Instant ID 人脸一致_1890367471809896450.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DZ_Face_Detailer`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FaceEmbedDistance`
- `IPAdapterFaceID`
- `IPAdapterUnifiedLoaderFaceID`
- `ImageBatch`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SUPIR_Upscale`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
