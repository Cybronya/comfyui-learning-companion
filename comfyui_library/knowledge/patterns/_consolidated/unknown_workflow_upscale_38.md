---
name: unknown_workflow_upscale_38
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.683
common_nodes: [BiRefNet_ModelLoader_Zho, BiRefNet_Zho, InspyrenetRembg, LayerMask: BiRefNetUltra, LayerMask: SegmentAnythingUltra V2, LoadImage, PreviewImage, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json, 图片生成/图生图/抠图_2062353508631928833.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json、图片生成/图生图/抠图_2062353508631928833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNet_ModelLoader_Zho`
- `BiRefNet_Zho`
- `InspyrenetRembg`
- `LayerMask: BiRefNetUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有
- `YUAN_TXTConvertAny` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
