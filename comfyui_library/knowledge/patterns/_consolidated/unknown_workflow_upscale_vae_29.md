---
name: unknown_workflow_upscale_vae_29
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.789143
common_nodes: [ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2 高清放大(满血版)_2085993701389725698.json, 图片生成/图生图/小图无限放大_2005663574984982529.json, 平台全量/SeedVR2 图片高清放大速度快_2118146313866010625.json, 平台全量/SeedVR2 高清放大_2063878387688624130.json, 平台全量/SeedVR2高清放大_2069226588218155010.json, 平台全量/seedvr2放大_1979035331024556034.json, 数字人/数字人/SeedVR2 7BQ8_1993652307126583298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_29

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SeedVR2 高清放大(满血版)_2085993701389725698.json、图片生成/图生图/小图无限放大_2005663574984982529.json、平台全量/SeedVR2 图片高清放大速度快_2118146313866010625.json、平台全量/SeedVR2 高清放大_2063878387688624130.json、平台全量/SeedVR2高清放大_2069226588218155010.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `INTConstant` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `FaceAlignmentCropper` —— 1/7 个有
- `FaceShaperCropper` —— 1/7 个有
- `easy imageSizeBySide` —— 1/7 个有
- `图像缩放V2_孤海` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
