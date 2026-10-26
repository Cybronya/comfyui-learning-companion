---
name: text_to_image_lora_sampler_clip_404
type: Text To Image
frequency: 5
level: strong
coverage: 0.8546
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1极简提示词文生图，日系胶片街拍人像写真随性抓拍_2112274524057198593.json, 图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json, 图片生成/文生图/Qwen Image 2.1自然街拍文生图｜日系胶片随手抓拍感｜极简提示词出真图_2112034888999333889.json, 图片生成/文生图/Qwen image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2102241527849373698.json, 图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_404

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1极简提示词文生图，日系胶片街拍人像写真随性抓拍_2112274524057198593.json、图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json、图片生成/文生图/Qwen Image 2.1自然街拍文生图｜日系胶片随手抓拍感｜极简提示词出真图_2112034888999333889.json、图片生成/文生图/Qwen image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2102241527849373698.json、图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `RHLLMChatNode` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Text` —— 3/5 个有
- `PreviewAny` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImpactInt` —— 1/5 个有

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
