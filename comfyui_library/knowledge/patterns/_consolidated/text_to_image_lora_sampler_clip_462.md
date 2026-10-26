---
name: text_to_image_lora_sampler_clip_462
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, RHLLMChatNode, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/自动多视图设计表（人物_场景_道具_任意主体）_2089630532681428993.json, 图片生成/图生图/（风格Lora版）Anima 自动提示词文生图V1_2060735043315785730.json, 图片生成/文生图/AnimaBase-动漫抽卡神器-全自动提示词-文生图_2057408001748856833.json, 图片生成/文生图/（Lora版）Anima 自动提示词文生图V1_2059972222953017346.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_462

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/自动多视图设计表（人物_场景_道具_任意主体）_2089630532681428993.json、图片生成/图生图/（风格Lora版）Anima 自动提示词文生图V1_2060735043315785730.json、图片生成/文生图/AnimaBase-动漫抽卡神器-全自动提示词-文生图_2057408001748856833.json、图片生成/文生图/（Lora版）Anima 自动提示词文生图V1_2059972222953017346.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `RHLLMChatNode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `PreviewAny` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `Latent Switch (JPS)` —— 1/4 个有
- `Random Line` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 40 | 4 | 37% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 2488 | 1024 - 3056 | 4 | 62% |
| 高度 | 1080 | 768 - 1080 | 4 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 40，4 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 2488，观测区间 1024 - 3056，4 个样本
- 高度 中位数 1080，观测区间 768 - 1080，4 个样本，取值集中（一致性 87%）
