---
name: text_to_image_lora_sampler_clip_114
type: Text To Image
frequency: 13
level: strong
coverage: 0.880769
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图带优化处理生成工具_2102462790022819841.json, 图片生成/文生图/Qwen Image 2.1文生图带优化，开源最强图片模型文本到图像方案_2103623073571368962.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜官方模型直接调用｜出图质量有保障_2102230734147776513.json, 图片生成/文生图/Qwen image 2.1 turbo文生图 高质量画面稳定直出_2110355293870837762.json, 图片生成/文生图/Qwen image 2.1 turbo文生图｜画质优化LoRA加持_2112451573052952578.json, 图片生成/文生图/Qwen-image2.1开源文生图｜提示词自动优化直出好图_2105261065113264129.json, 图片生成/文生图/Qwen-image2.1文生图开源王者｜优化提示词一步到位_2105264371466334209.json, 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json, 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111954037758316546.json, 图片生成/文生图/开源最强Qwen-image2.1文生图｜自带提示词优化加持_2105257763684311042.json, 图片生成/文生图/开源最强图片模型Qwen image2.1文生图带优化 高质量画面直出_2105421946069536770.json, 图片生成/文生图/开源最强图片模型Qwen image2.1文生图带优化 高质量画面直出_2105423398204698625.json, 图片生成/文生图/（文生图）qwen image 2.1 rurbo，高清创意直出_2111591580015620098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图带优化处理生成工具_2102462790022819841.json、图片生成/文生图/Qwen Image 2.1文生图带优化，开源最强图片模型文本到图像方案_2103623073571368962.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜官方模型直接调用｜出图质量有保障_2102230734147776513.json、图片生成/文生图/Qwen image 2.1 turbo文生图 高质量画面稳定直出_2110355293870837762.json、图片生成/文生图/Qwen image 2.1 turbo文生图｜画质优化LoRA加持_2112451573052952578.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 7/13 个有
- `CR Text` —— 7/13 个有
- `ImpactInt` —— 7/13 个有
- `Seed (rgthree)` —— 7/13 个有
- `String Literal` —— 7/13 个有
- `ResolutionSelector` —— 6/13 个有
- `KSamplerSelect` —— 5/13 个有
- `ManualSigmas` —— 5/13 个有
- `PrimitiveStringMultiline` —— 5/13 个有
- `SamplerCustom` —— 5/13 个有
- `SaveImageAdvanced` —— 3/13 个有
- `Note Plus (mtb)` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
