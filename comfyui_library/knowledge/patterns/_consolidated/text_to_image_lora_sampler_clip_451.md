---
name: text_to_image_lora_sampler_clip_451
type: Text To Image
frequency: 4
level: weak
coverage: 0.88375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptySD3LatentImage, ImageResizeKJv2, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶四视图生成流+超真实人物质感生成_2095811366279008257.json, 图片生成/文生图/四视图生成流超真实｜人物质感文生图反推一步出_2096232972402905089.json, 图片生成/文生图/角色四视图生成流｜超真实人物质感文生图制作_2095945717763366913.json, 数字人/数字人/四视图一站生成｜MiniMaxH3数字人辅助k2_2096597022622175233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_451

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/▶四视图生成流+超真实人物质感生成_2095811366279008257.json、图片生成/文生图/四视图生成流超真实｜人物质感文生图反推一步出_2096232972402905089.json、图片生成/文生图/角色四视图生成流｜超真实人物质感文生图制作_2095945717763366913.json、数字人/数字人/四视图一站生成｜MiniMaxH3数字人辅助k2_2096597022622175233.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `DapaoGPTImage2AllroundNode` —— 3/4 个有
- `DapaoGPTLLMChatNode` —— 3/4 个有
- `DapaoImageRatioLimitNode` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `Note Plus (mtb)` —— 3/4 个有
- `PrimitiveString` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
