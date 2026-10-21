---
name: text_to_image_lora_sampler_clip_144
type: Text To Image
frequency: 8
level: strong
coverage: 0.870125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerAdvanced, Lora Loader Stack (rgthree), LoraLoaderModelOnly, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2建构文生图｜创意图像一键生成直出_2091593303815970818.json, 图片生成/文生图/Krea2美感画质V2文生图处理生成工作流_2101784111047340033.json, 图片生成/文生图/Krea2美感画质双提升V2｜宋画电影感文生图工作流_2097774802739220481.json, 图片生成/文生图/Krea2美感画质双提升V2｜文生图质感升级_2097972474452467713.json, 图片生成/文生图/东方美学制作流｜中国风场景特效文生图出片_2100824969306533890.json, 图片生成/文生图/东方美学风格文生图艺术处理生成工作流工具包_2101014716817690626.json, 图片生成/文生图/巨构大场面一键生成｜Krea2文生图创作利器_2091764677775814658.json, 图片生成/文生图/画质美感双提升｜Krea2文生图一键优化_2093733215847665666.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Krea2建构文生图｜创意图像一键生成直出_2091593303815970818.json、图片生成/文生图/Krea2美感画质V2文生图处理生成工作流_2101784111047340033.json、图片生成/文生图/Krea2美感画质双提升V2｜宋画电影感文生图工作流_2097774802739220481.json、图片生成/文生图/Krea2美感画质双提升V2｜文生图质感升级_2097972474452467713.json、图片生成/文生图/东方美学制作流｜中国风场景特效文生图出片_2100824969306533890.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `Lora Loader Stack (rgthree)`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `LatentUpscaleBy` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `ResolutionSelector` —— 2/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
