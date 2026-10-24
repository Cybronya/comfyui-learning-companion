---
name: unknown_workflow_controlnet_clip_checkpoint
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.903
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, DZ_Face_Detailer, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/instantID一键换脸工作流_1912743901986521090.json, 图片生成/图生图/一键换脸工作流V1_1924072740834168834.json, 图片生成/图生图/极速换脸（instantid）_2029491843662094338.json, 图片生成/图生图/自动换脸+高度融合（相似度接近100%）_1975052454855315457.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/instantID一键换脸工作流_1912743901986521090.json、图片生成/图生图/一键换脸工作流V1_1924072740834168834.json、图片生成/图生图/极速换脸（instantid）_2029491843662094338.json、图片生成/图生图/自动换脸+高度融合（相似度接近100%）_1975052454855315457.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DZ_Face_Detailer`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `VideoLinearCFGGuidance` —— 2/4 个有
- `CropFace` —— 1/4 个有
- `FaceAnalysisModels` —— 1/4 个有
- `FaceBoundingBox` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageBatch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
