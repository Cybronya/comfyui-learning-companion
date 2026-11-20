---
name: image_to_image_upscale_lora_sampler_21
type: Image To Image
frequency: 7
level: moderate
coverage: 0.86
common_nodes: [CLIPLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, PDIMAGE_LongerSize, UNETLoader, VAEDecode, VAEEncode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSave]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113875961979691010.json, 图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113886437203595266.json, 图片生成/图生图/无提示词_极速图生图_Krea 2+MJ美学_2108177950792314881.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2107987954869301250.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2108449947493429250.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2110562308006178817.json, 图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2111006118758670337.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113875961979691010.json、图片生成/图生图/Krea 2+MJ美学图生图_无提示词极速版_2113886437203595266.json、图片生成/图生图/无提示词_极速图生图_Krea 2+MJ美学_2108177950792314881.json、图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2107987954869301250.json、图片生成/图生图/最强动漫转真实_Krea2双采+高清放大_2108449947493429250.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Seed (rgthree)` —— 4/7 个有
- `workflow>Krea 2 Ostris Edit` —— 4/7 个有
- `CR Apply LoRA Stack` —— 3/7 个有
- `CR LoRA Stack` —— 3/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `TextEncodeKrea2OstrisEdit` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.15 | 0.15 - 1 | 7 | 18% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.15，观测区间 0.15 - 1，7 个样本，取值分散，一致性仅 18%
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
