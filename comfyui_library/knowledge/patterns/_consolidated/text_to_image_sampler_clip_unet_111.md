---
name: text_to_image_sampler_clip_unet_111
type: Text To Image
frequency: 6
level: weak
coverage: 0.826667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json, 图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json, 图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json, 图片生成/文生图/Anima-light+Lavender+测试+对比工作流_2109923237093273602.json, 图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2110456587952410625.json, 图片生成/文生图/VividMuse Z-Image MJ风格｜艺术人像文生图生成_2096331581739851778.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_111

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json、图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json、图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json、图片生成/文生图/Anima-light+Lavender+测试+对比工作流_2109923237093273602.json、图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2110456587952410625.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 5/6 个有
- `TTResolutionSelector` —— 5/6 个有
- `easy anythingIndexSwitch` —— 5/6 个有
- `easy mathInt` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `JjkText` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `solarL_SaveImagesToZip` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `ImageOnlyCheckpointLoader` —— 3/6 个有
- `BasicScheduler` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `SigmasPreview` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 6 | 9% |
| 高度 | 80 | 80 - 512 | 6 | 9% |
| 采样步数 | 4 | 4 - 36 | 6 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 4.5 | 6 | 95% |
| 采样算法 | er_sde | - | 6 | 67% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，6 个样本，取值分散，一致性仅 9%
- 高度 中位数 80，观测区间 80 - 512，6 个样本，取值分散，一致性仅 9%
- 采样步数 中位数 4，观测区间 4 - 36，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 4.5，6 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，6 个样本，一致性 67%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
