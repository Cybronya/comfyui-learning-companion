---
name: unknown_workflow_upscale_vae_10
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.784
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/花型设计图高清_2108474871826182146.json, 图片生成/图生图/花型高清_2111753801672773634.json, 平台全量/SEEDVR2.5图片超清修复极速版_2065613776669462530.json, 平台全量/SEEDVR2放大_2025855321327017985.json, 平台全量/SVR2高清修复修复_2034167369525895169.json, 平台全量/SeedVR2-Image_2080618481539698689.json, 平台全量/SeedVR2-图片高清放大工作流_2076244587592638465.json, 平台全量/SeedVR2.5.1图像高清放大_1991838615928107010.json, 平台全量/SeedVR2.5.1图像高清放大效果非常好_1992067155384487937.json, 平台全量/SeedVR2.5.1图片高清放大_1992468759749218305.json, 平台全量/SeedVR2.5最新版 史上最强图像无损高清放大_2000920538589655041.json, 平台全量/SeedVR2_图片放大_2030076513076383745.json, 平台全量/SeedVR2图像高清放大工作流_2049095129985716226.json, 平台全量/SeedVR2图片放大_2078377939732877313.json, 平台全量/图片高清修复SeedVR2.5_2005642594820517890.json, 平台全量/图片高清修复SeedVR2.5_2013935198743830529.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_10

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/花型设计图高清_2108474871826182146.json、图片生成/图生图/花型高清_2111753801672773634.json、平台全量/SEEDVR2.5图片超清修复极速版_2065613776669462530.json、平台全量/SEEDVR2放大_2025855321327017985.json、平台全量/SVR2高清修复修复_2034167369525895169.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 16 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 13/16 个有
- `ImageScaleBy` —— 10/16 个有
- `PrimitiveInt` —— 6/16 个有
- `Int` —— 3/16 个有
- `PreviewImage` —— 2/16 个有
- `SimpleMath+` —— 2/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
