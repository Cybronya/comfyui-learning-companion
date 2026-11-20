---
name: unknown_workflow_upscale_vae_16
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.903909
common_nodes: [SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [平台全量/SeeVR2 高清放大-2_2004809846040002562.json, 平台全量/SeeVR2 高清放大_1994652065563615234.json, 平台全量/seedvr2_image_hd_2072576890270998529.json, 平台全量/seedvr2放大_1997914737767776258.json, 平台全量/test_seedvr2_image_hd_2084940767050686466.json, 平台全量/图像修复对比工作流_2044959696179695617.json, 平台全量/图片放大（老程）_2019656875989536770.json, 平台全量/图片高清放大工作流_2068239366807449601.json, 平台全量/图片高清放大：SeedVR2_2054731074751746050.json, 平台全量/极速一键无损图片高清放大seedvr2_2057070787257004034.json, 平台全量/高清放大丨极致还原丨8K丨SeedVR2_2002953396099379202.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_16

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/SeeVR2 高清放大-2_2004809846040002562.json、平台全量/SeeVR2 高清放大_1994652065563615234.json、平台全量/seedvr2_image_hd_2072576890270998529.json、平台全量/seedvr2放大_1997914737767776258.json、平台全量/test_seedvr2_image_hd_2084940767050686466.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `Image Comparer (rgthree)` —— 6/11 个有
- `JoinImageWithAlpha` —— 2/11 个有
- `MuyeLoadImage` —— 2/11 个有
- `Label (rgthree)` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
