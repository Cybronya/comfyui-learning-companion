---
name: text_to_image_sampler_clip_unet_21
type: Text To Image
frequency: 16
level: weak
coverage: 0.926937
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Image2.5全能图像文生图 高品质文本到图像生成_2098269388993548289.json, 图片生成/文生图/Image2.5文生图 顶级_2101616440351748097.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2101592299229761537.json, 图片生成/文生图/Image2.5文生图顶级处理生成工作流工具_2102116515188400130.json, 图片生成/文生图/Image2.5文生图顶级工作流｜高质量图片生成｜文案配图一步到位_2101886755678015490.json, 图片生成/文生图/Image2.5文生图高质量图片生成工具｜高级感图像一键生成_2101936480737382401.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097508758569181185.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097516972694138882.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097522180136460290.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097528893510082561.json, 图片生成/文生图/Krea2 场景生图｜轻量精简版_2098694122218541057.json, 图片生成/文生图/Krea2场景生图轻量精简版｜文生图快速铺场景氛围大图_2099170680729325570.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098928781699407874.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Image2.5全能图像文生图 高品质文本到图像生成_2098269388993548289.json、图片生成/文生图/Image2.5文生图 顶级_2101616440351748097.json、图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json、图片生成/文生图/Image2.5文生图 高质量图片生成工具_2101592299229761537.json、图片生成/文生图/Image2.5文生图顶级处理生成工作流工具_2102116515188400130.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `solarL_SaveImagesToZip` —— 15/16 个有
- `CR Text` —— 10/16 个有
- `ModelSamplingAuraFlow` —— 9/16 个有
- `PathchSageAttentionKJ` —— 9/16 个有
- `easy loraStack` —— 9/16 个有
- `easy loraStackApply` —— 9/16 个有
- `孤海注释` —— 7/16 个有
- `RH_RhartImageG25SunburstTextToImage` —— 6/16 个有
- `PreviewImage` —— 3/16 个有
- `EmptyImage` —— 2/16 个有
- `RH_RhartImageG25FlareTextToImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 16 | 80% |
| 采样算法 | er_sde | - | 16 | 94% |
| 调度器 | beta | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 1024 | 16 | 0% |
| 高度 | 80 | 80 - 1024 | 16 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，16 个样本，取值集中（一致性 80%）
- 采样算法 最常用 er_sde，16 个样本，一致性 94%
- 调度器 最常用 beta，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 0%
- 高发问题（27/16 个样本）：Steps较低可能导致细节不足
