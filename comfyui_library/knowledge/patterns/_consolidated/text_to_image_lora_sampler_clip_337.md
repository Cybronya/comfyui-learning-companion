---
name: text_to_image_lora_sampler_clip_337
type: Text To Image
frequency: 5
level: strong
coverage: 0.8238
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, Flux3PELoader, Flux3PromptEnhance, ImageConcanate, ImpactConditionalBranch, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX3 PE提示词强化图像编辑单图版｜精修加速一步到位_2111795864938307585.json, 图片生成/图生图/Flux3 PE提示词强化加速版多图编辑｜批量修图不翻车_2111792576729796610.json, 图片生成/图生图/Flux3 PE提示词强化加速版，多图编辑图生图利器_2111972850059014145.json, 图片生成/文生图/flux3_klein_in 文生图图生图，功能二合一加速_2111968176782266369.json, 图片生成/文生图/flux3_klein_int8文生图图生图二合一｜int8加速低显存_2111774013038088193.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_337

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX3 PE提示词强化图像编辑单图版｜精修加速一步到位_2111795864938307585.json、图片生成/图生图/Flux3 PE提示词强化加速版多图编辑｜批量修图不翻车_2111792576729796610.json、图片生成/图生图/Flux3 PE提示词强化加速版，多图编辑图生图利器_2111972850059014145.json、图片生成/文生图/flux3_klein_in 文生图图生图，功能二合一加速_2111968176782266369.json、图片生成/文生图/flux3_klein_int8文生图图生图二合一｜int8加速低显存_2111774013038088193.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux3PELoader`
- `Flux3PromptEnhance`
- `ImageConcanate`
- `ImpactConditionalBranch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ReferenceMultiLatent` —— 4/5 个有
- `FastGroupsBypassSwitch` —— 3/5 个有
- `PDIMAGE_LongerSize` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `TextGenerateLTX2Prompt` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/5 个有
- `ReferenceLatent` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
