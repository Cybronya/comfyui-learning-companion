---
name: unknown_workflow_upscale_vae_41
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7518
common_nodes: [LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [平台全量/A.纯放大_2021840360942604289.json, 平台全量/▶SeedVR2图像放大_2045074853597810690.json, 平台全量/▶SeedVR2无损高清放大_2034983520405299202.json, 平台全量/▶无损高清放大4k可跑_2001472869601341441.json, 平台全量/【晨晨的AI应用包002】图片SeedVR2放大_2011285505522016258.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_41

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/A.纯放大_2021840360942604289.json、平台全量/▶SeedVR2图像放大_2045074853597810690.json、平台全量/▶SeedVR2无损高清放大_2034983520405299202.json、平台全量/▶无损高清放大4k可跑_2001472869601341441.json、平台全量/【晨晨的AI应用包002】图片SeedVR2放大_2011285505522016258.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `Float` —— 1/5 个有
- `GetImage` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `MinNode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
