---
name: text_to_image_sampler_clip_unet_120
type: Text To Image
frequency: 3
level: moderate
coverage: 0.862667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, JjkText, KSampler, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima二次元动漫灵动定格文生图_2057664936750436354.json, 图片生成/文生图/Anima文生图图生图洗图 自动提示词优化工作流_2105049035978665986.json, 图片生成/文生图/二次元动漫灵动定格文生图Anima_2057749862011203586.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima二次元动漫灵动定格文生图_2057664936750436354.json、图片生成/文生图/Anima文生图图生图洗图 自动提示词优化工作流_2105049035978665986.json、图片生成/文生图/二次元动漫灵动定格文生图Anima_2057749862011203586.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `FLS_SamplerV4` —— 1/3 个有
- `InversionDemoLazyIndexSwitch` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 3 | 45% |
| 高度 | 512 | 80 - 512 | 3 | 45% |
| 采样步数 | 40 | 4 - 40 | 3 | 39% |
| Prompt 约束强度(CFG) | 5 | 4.5 - 5 | 3 | 95% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，3 个样本，取值分散，一致性仅 45%
- 高度 中位数 512，观测区间 80 - 512，3 个样本，取值分散，一致性仅 45%
- 采样步数 中位数 40，观测区间 4 - 40，3 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4.5 - 5，3 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
