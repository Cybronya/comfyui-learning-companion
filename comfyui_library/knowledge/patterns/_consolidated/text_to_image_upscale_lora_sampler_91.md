---
name: text_to_image_upscale_lora_sampler_91
type: Text To Image
frequency: 3
level: strong
coverage: 0.866667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Muter (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, PrimitiveStringMultiline, RH_LLMAPI_NODE, RH_RhartImageG2ImageToImage, SaveImage, UNETLoader, VAEDecode, VAELoader, WujiCleaner, WujiUpscaler, easy promptConcat, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1 image2.5二合一多参海报生成器文生多图生均可_2108657486508158978.json, 图片生成/图生图/Qwen image2.1与2.5二合一｜多参海报生成文生多图生均可_2111144922781929474.json, 图片生成/图生图/Qwen-Eidt-2511与image2二合一｜多参海报生成器文生多图生_2092002351044448258.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1 image2.5二合一多参海报生成器文生多图生均可_2108657486508158978.json、图片生成/图生图/Qwen image2.1与2.5二合一｜多参海报生成文生多图生均可_2111144922781929474.json、图片生成/图生图/Qwen-Eidt-2511与image2二合一｜多参海报生成器文生多图生_2092002351044448258.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `WujiUpscaler`
- `easy promptConcat`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 2/3 个有
- `WujiPromptEditor` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `PresetTextSelector` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `WujiStyleSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
