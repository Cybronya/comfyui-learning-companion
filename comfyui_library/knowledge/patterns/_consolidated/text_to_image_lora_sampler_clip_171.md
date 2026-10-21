---
name: text_to_image_lora_sampler_clip_171
type: Text To Image
frequency: 7
level: strong
coverage: 0.885286
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, EmptyLatentImage, ImpactInt, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, Seed (rgthree), String Literal, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图带优化处理生成工具_2102462790022819841.json, 图片生成/文生图/Qwen Image 2.1文生图带优化，开源最强图片模型文本到图像方案_2103623073571368962.json, 图片生成/文生图/Qwen-image2.1开源文生图｜提示词自动优化直出好图_2105261065113264129.json, 图片生成/文生图/Qwen-image2.1文生图开源王者｜优化提示词一步到位_2105264371466334209.json, 图片生成/文生图/开源最强Qwen-image2.1文生图｜自带提示词优化加持_2105257763684311042.json, 图片生成/文生图/开源最强图片模型Qwen image2.1文生图带优化 高质量画面直出_2105421946069536770.json, 图片生成/文生图/开源最强图片模型Qwen image2.1文生图带优化 高质量画面直出_2105423398204698625.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_171

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图带优化处理生成工具_2102462790022819841.json、图片生成/文生图/Qwen Image 2.1文生图带优化，开源最强图片模型文本到图像方案_2103623073571368962.json、图片生成/文生图/Qwen-image2.1开源文生图｜提示词自动优化直出好图_2105261065113264129.json、图片生成/文生图/Qwen-image2.1文生图开源王者｜优化提示词一步到位_2105264371466334209.json、图片生成/文生图/开源最强Qwen-image2.1文生图｜自带提示词优化加持_2105257763684311042.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `EmptyLatentImage`
- `ImpactInt`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Seed (rgthree)`
- `String Literal`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/7 个有

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
