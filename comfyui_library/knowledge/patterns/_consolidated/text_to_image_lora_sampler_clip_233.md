---
name: text_to_image_lora_sampler_clip_233
type: Text To Image
frequency: 5
level: strong
coverage: 0.8444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen 2.1洗图工作流，文生图反推提示词处理工具_2108319840565030913.json, 图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json, 图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json, 图片生成/文生图/Qwen Image 2.1文生图对比流｜不同提示词效果并排出图_2108037643018788866.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，文生图高质量文本到图像生成方案_2108446649474437121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_233

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen 2.1洗图工作流，文生图反推提示词处理工具_2108319840565030913.json、图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json、图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json、图片生成/文生图/Qwen Image 2.1文生图对比流｜不同提示词效果并排出图_2108037643018788866.json、图片生成/文生图/Qwen Image 2.1文生图工作流，文生图高质量文本到图像生成方案_2108446649474437121.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 4/5 个有
- `RegexExtract` —— 4/5 个有
- `SaveImageAdvanced` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `JsonExtractString` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `StringCompare` —— 3/5 个有
- `StringConcatenate` —— 2/5 个有
- `Text` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `RegexMatch` —— 1/5 个有
- `SeedGenerator` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
