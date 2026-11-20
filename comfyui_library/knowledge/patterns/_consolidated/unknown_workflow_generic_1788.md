---
name: unknown_workflow_generic_1788
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/融图 香蕉模型_1961094180934193154.json, 平台全量/场景生成人物模特  全能图片V1 2 pro 真实人物生成 结合场景光影一致人物生成_1996479440513286145.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1788

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/融图 香蕉模型_1961094180934193154.json、平台全量/场景生成人物模特  全能图片V1 2 pro 真实人物生成 结合场景光影一致人物生成_1996479440513286145.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
