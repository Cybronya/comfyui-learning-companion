---
name: unknown_workflow_upscale_vae_27
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.744
common_nodes: [JoinImageWithAlpha, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2.5_4K_图像4K高清放大_1997923965844750337.json, 图片生成/图生图/SeedVR2.5_图像4K高清放大_1997976745368281090.json, 图片生成/图生图/【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185.json, 图片生成/图生图/印花级图案高清修复工作流 _ 无损放大 + 智能抠图 + 瑕疵修复_2078910452784001026.json, 图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_27

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5_4K_图像4K高清放大_1997923965844750337.json、图片生成/图生图/SeedVR2.5_图像4K高清放大_1997976745368281090.json、图片生成/图生图/【阡陌】SeedVR 2.5 超高清放大工作流_2011339031476445185.json、图片生成/图生图/印花级图案高清修复工作流 _ 无损放大 + 智能抠图 + 瑕疵修复_2078910452784001026.json、图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `JoinImageWithAlpha`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy int` —— 4/5 个有
- `ImageScaleRestore_UTK` —— 3/5 个有
- `KOOK_ImageCompression` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `RMBG` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
