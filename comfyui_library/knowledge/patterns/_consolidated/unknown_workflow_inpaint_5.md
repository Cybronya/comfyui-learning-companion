---
name: unknown_workflow_inpaint_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.708
common_nodes: [BiRefNet_Hugo, ETN_Translate, GrowMask, INPAINT_ExpandMask, InspyrenetRembg, InvertMask, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: RmBgUltra V2, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageRemoveAlpha, LoadImage, PreviewImage, RMBG, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/全能抠图 能应对毛发 玻璃_1921584351258279938.json, 图片生成/图生图/全能自动抠图工作流_1987847916989648897.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能抠图 能应对毛发 玻璃_1921584351258279938.json、图片生成/图生图/全能自动抠图工作流_1987847916989648897.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNet_Hugo`
- `ETN_Translate`
- `GrowMask`
- `INPAINT_ExpandMask`
- `InspyrenetRembg`
- `InvertMask`
- `JoinImageWithAlpha`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: RmBgUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `PreviewImage`
- `RMBG`
- `SaveImage`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
