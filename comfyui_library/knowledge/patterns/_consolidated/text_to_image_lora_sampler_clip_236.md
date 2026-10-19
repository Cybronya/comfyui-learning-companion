---
name: text_to_image_lora_sampler_clip_236
type: Text To Image
frequency: 3
level: strong
coverage: 0.881667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, Seed (rgthree), ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json, 图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json, 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_236

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json、图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json、图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenPERewriteT8` —— 2/3 个有
- `SaveImageAdvanced` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
