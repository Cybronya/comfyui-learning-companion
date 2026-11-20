---
name: text_to_image_sampler_clip_unet_16
type: Text To Image
frequency: 21
level: weak
coverage: 0.860143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json, 图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json, 图片生成/文生图/Krea2_写实人像_2083068524297277442.json, 图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json, 图片生成/文生图/Krea2_写实人像（双采版）_2077640931263737858.json, 图片生成/文生图/Krea2_写实人像（双采版）_2079377240273547266.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087070012069736450.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087380793143422978.json, 图片生成/文生图/Krea2人物四视图工作流，人物角色角色设计文生图工具_2107516751167713281.json, 图片生成/文生图/Krea2写实文生图Raw+Turbo 纹身风格高写实输出_2098846918221848578.json, 图片生成/文生图/Krea2古装汉服肚兜美女文生图处理生成工作流_2101415318026539010.json, 图片生成/文生图/Krea2古装汉服肚兜美女文生图处理生成工作流_2101767889689858049.json, 图片生成/文生图/Krea2小昔涟角色cos｜游戏美少女文生图生成_2095931663795712001.json, 图片生成/文生图/Krea2建构文生图｜创意图像一键生成直出_2091593303815970818.json, 图片生成/文生图/Krea2美感画质V2文生图处理生成工作流_2101784111047340033.json, 图片生成/文生图/Krea2美感画质双提升V2｜宋画电影感文生图工作流_2097774802739220481.json, 图片生成/文生图/Krea2美感画质双提升V2｜文生图质感升级_2097972474452467713.json, 图片生成/文生图/东方美学制作流｜中国风场景特效文生图出片_2100824969306533890.json, 图片生成/文生图/东方美学风格文生图艺术处理生成工作流工具包_2101014716817690626.json, 图片生成/文生图/巨构大场面一键生成｜Krea2文生图创作利器_2091764677775814658.json, 图片生成/文生图/画质美感双提升｜Krea2文生图一键优化_2093733215847665666.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json、图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json、图片生成/文生图/Krea2_写实人像_2083068524297277442.json、图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json、图片生成/文生图/Krea2_写实人像（双采版）_2077640931263737858.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 17/21 个有
- `孤海注释` —— 15/21 个有
- `LoraLoaderModelOnly` —— 14/21 个有
- `JjkText` —— 13/21 个有
- `PrimitiveStringMultiline` —— 13/21 个有
- `ResolutionSelector` —— 13/21 个有
- `solarL_SaveImagesToZip` —— 13/21 个有
- `KSamplerAdvanced` —— 9/21 个有
- `ConditioningKrea2Rebalance` —— 8/21 个有
- `Lora Loader Stack (rgthree)` —— 8/21 个有
- `PrimitiveInt` —— 8/21 个有
- `CompressImages` —— 4/21 个有
- `ModelSamplingAuraFlow` —— 3/21 个有
- `LatentUpscaleBy` —— 2/21 个有
- `PrimitiveFloat` —— 2/21 个有
- `Int` —— 1/21 个有
- `LayerUtility: PurgeVRAM V2` —— 1/21 个有
- `Text` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 21 | 0% |
| 高度 | 80 | 80 - 1024 | 21 | 0% |
| 采样步数 | 4 | 4 - 12 | 21 | 59% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 21 | 46% |
| 采样算法 | er_sde | - | 21 | 62% |
| 调度器 | beta | - | 21 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，21 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，21 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 12，21 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，21 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 er_sde，21 个样本，一致性 62%
- 调度器 最常用 beta，21 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（30/21 个样本）：Steps较低可能导致细节不足
