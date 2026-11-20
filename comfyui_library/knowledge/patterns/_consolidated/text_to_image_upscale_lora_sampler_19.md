---
name: text_to_image_upscale_lora_sampler_19
type: Text To Image
frequency: 12
level: moderate
coverage: 0.877917
common_nodes: [CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, MuyeTextEditOutput, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, VAEDecode, VOSR2ModelLoader, VOSR2Upscale]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS文生图 - 摄影Style - 4步加速_2115669310256533506.json, 图片生成/文生图/MOSS文生图 - 摄影Style - 4步加速_2116403436492255234.json, 图片生成/文生图/MOSS文生图-4步出图-VOSR高清放大_2112043829208641537.json, 图片生成/文生图/MOSS文生图_-_摄影Style_-_4步加速_2115978602155167745.json, 图片生成/文生图/MOSS文生图_可4步加速_2116796986094612482.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2115435036278353921.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2115660408798404609.json, 平台全量/MOSS 二次元-4步-15秒-快速出图（文生图）_2118155813704519681.json, 平台全量/MOSS 亚洲人像 4步快速出图（文生图）_2117621442044063745.json, 平台全量/MOSS文生图 - Cospaly&韩系脸模 - 8步加速_2120150948025815042.json, 平台全量/MOSS文生图 - 摄影Style - 4步加速_2118188698406838274.json, 平台全量/MOSS文生图 - 网红&时尚摄影 - 8步加速_2120144907498250241.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/MOSS文生图 - 摄影Style - 4步加速_2115669310256533506.json、图片生成/文生图/MOSS文生图 - 摄影Style - 4步加速_2116403436492255234.json、图片生成/文生图/MOSS文生图-4步出图-VOSR高清放大_2112043829208641537.json、图片生成/文生图/MOSS文生图_-_摄影Style_-_4步加速_2115978602155167745.json、图片生成/文生图/MOSS文生图_可4步加速_2116796986094612482.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `VAEDecode`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 10/12 个有
- `PreviewImage` —— 10/12 个有
- `CLIPLoader` —— 2/12 个有
- `EnhancedLoadDiffusionModel` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `MOSSMergePreset` —— 2/12 个有
- `VAELoader` —— 2/12 个有
- `LoadImage` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 50 | 12 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 12 | 44% |
| 采样算法 | er_sde | - | 12 | 83% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 50，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，12 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 er_sde，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高发问题（9/12 个样本）：Steps较低可能导致细节不足
