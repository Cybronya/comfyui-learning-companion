---
name: text_to_image_lora_sampler_clip_267
type: Text To Image
frequency: 7
level: strong
coverage: 0.903
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI短剧创作FLUX3加速版文生图｜提示词进去成图就出_2111332075042328577.json, 图片生成/文生图/FLUX3 Image Klein文生图修复版，中文繁体招牌王_2111942921883840514.json, 图片生成/文生图/FLUX3加速版文生图standard模式｜输入提示词一键直出_2111311147206004737.json, 图片生成/文生图/FLUX3加速版文生图，快速直出高清创意形象_2111542604138635266.json, 图片生成/文生图/FLUX3文生图sd-in 量化，提示词pe优化出图_2111939737857646594.json, 图片生成/文生图/Flux3多图编辑加速版，反推提示词图生图利器_2111941221856923650.json, 图片生成/文生图/flux3_klien3文生图，人像写真平面设计出图_2111559376304693250.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_267

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/AI短剧创作FLUX3加速版文生图｜提示词进去成图就出_2111332075042328577.json、图片生成/文生图/FLUX3 Image Klein文生图修复版，中文繁体招牌王_2111942921883840514.json、图片生成/文生图/FLUX3加速版文生图standard模式｜输入提示词一键直出_2111311147206004737.json、图片生成/文生图/FLUX3加速版文生图，快速直出高清创意形象_2111542604138635266.json、图片生成/文生图/FLUX3文生图sd-in 量化，提示词pe优化出图_2111939737857646594.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 6/7 个有
- `EmptyFlux2LatentImage` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `ManualSigmas` —— 6/7 个有
- `RandomNoise` —— 6/7 个有
- `SamplerCustomAdvanced` —— 6/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `QwenPERewriteT8` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `ReferenceMultiLatent` —— 1/7 个有
- `ResolutionSelector` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
