---
name: unknown_workflow_video_184
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.863
common_nodes: [LoadImage, LoadSAM3Model, MaskPreview, MaskToImage, PreviewAny, PreviewImage, SAM3AddVideoPrompt, SAM3BBoxCollector, SAM3CloseVideoSession, SAM3InitVideoSession, SAM3PointCollector, SAM3PropagateVideo, SAM3Segmentation, SAM3VideoModelLoader, SAM3VideoOutput, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/文生图/sam3组件_1993229787548368897.json, 平台全量/ComfyUI-SAM3抠图教程，SAM3大模型能够分割一切，物体识别达到人类水平80%！_1992865354202370050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_184

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/sam3组件_1993229787548368897.json、平台全量/ComfyUI-SAM3抠图教程，SAM3大模型能够分割一切，物体识别达到人类水平80%！_1992865354202370050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `LoadSAM3Model`
- `MaskPreview`
- `MaskToImage`
- `PreviewAny`
- `PreviewImage`
- `SAM3AddVideoPrompt`
- `SAM3BBoxCollector`
- `SAM3CloseVideoSession`
- `SAM3InitVideoSession`
- `SAM3PointCollector`
- `SAM3PropagateVideo`
- `SAM3Segmentation`
- `SAM3VideoModelLoader`
- `SAM3VideoOutput`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `VHS_VideoInfoSource` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
