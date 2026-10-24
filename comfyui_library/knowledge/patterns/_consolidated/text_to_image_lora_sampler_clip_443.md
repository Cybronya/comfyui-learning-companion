---
name: text_to_image_lora_sampler_clip_443
type: Text To Image
frequency: 4
level: strong
coverage: 0.86375
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, RHLLMChatNode, ResolutionSelector, SaveImage, Seed (rgthree), TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1极简提示词文生图，日系胶片街拍人像写真随性抓拍_2112274524057198593.json, 图片生成/文生图/Qwen Image 2.1自然街拍文生图｜日系胶片随手抓拍感｜极简提示词出真图_2112034888999333889.json, 图片生成/文生图/Qwen image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2102241527849373698.json, 图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_443

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1极简提示词文生图，日系胶片街拍人像写真随性抓拍_2112274524057198593.json、图片生成/文生图/Qwen Image 2.1自然街拍文生图｜日系胶片随手抓拍感｜极简提示词出真图_2112034888999333889.json、图片生成/文生图/Qwen image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2102241527849373698.json、图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `RHLLMChatNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `PreviewAny` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Text` —— 2/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
