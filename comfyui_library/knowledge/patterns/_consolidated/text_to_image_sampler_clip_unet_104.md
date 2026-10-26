---
name: text_to_image_sampler_clip_unet_104
type: Text To Image
frequency: 7
level: weak
coverage: 0.835143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json, 图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json, 图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json, 图片生成/文生图/Anima-light+Lavender+测试+对比工作流_2109923237093273602.json, 图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2110456587952410625.json, 图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2113472885594611714.json, 图片生成/文生图/VividMuse Z-Image MJ风格｜艺术人像文生图生成_2096331581739851778.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_104

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Anima Yume1.5对比测试流｜动漫角色出图评测_2098763284521508866.json、图片生成/文生图/Anima Yume1.5测试 对比工作流_2098318586065547265.json、图片生成/文生图/Anima Yume1.5测试对比工作流 动漫角色文生图版本对比_2098730726186381313.json、图片生成/文生图/Anima-light+Lavender+测试+对比工作流_2109923237093273602.json、图片生成/文生图/Anima-light与Lavender测试对比工作流，文生图图生图热门IP_2110456587952410625.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
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
- `PrimitiveInt` —— 6/7 个有
- `TTResolutionSelector` —— 6/7 个有
- `easy anythingIndexSwitch` —— 6/7 个有
- `easy mathInt` —— 6/7 个有
- `JjkText` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `solarL_SaveImagesToZip` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `ImageOnlyCheckpointLoader` —— 3/7 个有
- `BasicScheduler` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `KSamplerAdvanced` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SigmasPreview` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 7 | 4% |
| 高度 | 80 | 80 - 512 | 7 | 4% |
| 采样步数 | 4 | 4 - 36 | 7 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 4.5 | 7 | 95% |
| 采样算法 | er_sde | - | 7 | 71% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，7 个样本，取值分散，一致性仅 4%
- 高度 中位数 80，观测区间 80 - 512，7 个样本，取值分散，一致性仅 4%
- 采样步数 中位数 4，观测区间 4 - 36，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 4.5，7 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，7 个样本，一致性 71%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
