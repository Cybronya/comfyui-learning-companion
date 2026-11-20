---
name: image_to_image_upscale_lora_sampler_20
type: Image To Image
frequency: 8
level: weak
coverage: 0.859625
common_nodes: [CLIPLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, PDIMAGE_LongerSize, UNETLoader, VAEDecode, VAEEncode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSave]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113875961979691010.json, 图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113886437203595266.json, 图片生成/图生图/无提示词_极速图生图_Krea 2+MJ美学_2108177950792314881.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2107987954869301250.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2108449947493429250.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2110562308006178817.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2111006118758670337.json, 平台全量/Krea2 动漫转真实｜双采 + Vosr 2 高清放大_2118315317763076097.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113875961979691010.json、图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113886437203595266.json、图片生成/图生图/无提示词_极速图生图_Krea 2+MJ美学_2108177950792314881.json、图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2107987954869301250.json、图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2108449947493429250.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PDIMAGE_LongerSize`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageSave`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 5/8 个有
- `workflow>Krea 2 Ostris Edit` —— 4/8 个有
- `CR Apply LoRA Stack` —— 3/8 个有
- `CR LoRA Stack` —— 3/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `TextEncodeKrea2OstrisEdit` —— 3/8 个有
- `2e128825-a67c-4b93-96a9-2e26cd2e8b46` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 62% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 0.15 | 0.15 - 1 | 8 | 12% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 0.15，观测区间 0.15 - 1，8 个样本，取值分散，一致性仅 12%
- 高发问题（13/8 个样本）：Steps较低可能导致细节不足
