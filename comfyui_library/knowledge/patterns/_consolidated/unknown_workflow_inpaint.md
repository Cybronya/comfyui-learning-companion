---
name: unknown_workflow_inpaint
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7078
common_nodes: [BiRefNet_Hugo, GrowMask, INPAINT_ExpandMask, InspyrenetRembg, InvertMask, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: RmBgUltra V2, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageRemoveAlpha, LoadImage, PreviewImage, RMBG, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/全能抠图 能应对毛发 玻璃_1921584351258279938.json, 图片生成/图生图/全能自动抠图工作流_1987847916989648897.json, 平台全量/【全能抠图】一键批量抠图 抠毛发 抠玻璃_1917838389754925057.json, 平台全量/全能抠图 八种抠图最全面_1935172450475024386.json, 平台全量/全能抠图 能应对毛发 玻璃_1916308814780366850.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/全能抠图 能应对毛发 玻璃_1921584351258279938.json、图片生成/图生图/全能自动抠图工作流_1987847916989648897.json、平台全量/【全能抠图】一键批量抠图 抠毛发 抠玻璃_1917838389754925057.json、平台全量/全能抠图 八种抠图最全面_1935172450475024386.json、平台全量/全能抠图 能应对毛发 玻璃_1916308814780366850.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `BiRefNet_Hugo`
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

**可变部分**（部分 workflow 才有）：
- `ETN_Translate` —— 4/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `Image Compare (mtb)` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
