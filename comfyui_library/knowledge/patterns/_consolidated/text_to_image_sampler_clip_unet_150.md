---
name: text_to_image_sampler_clip_unet_150
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9316
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image+提示词扩写+8步快速lora_1956256254878470146.json, 图片生成/文生图/zimage文生图_2004814222078996481.json, 图片生成/文生图/失败作图工作流_2077959412047765506.json, 图片生成/文生图/官流Qwen-lmage-FP8中文版_1953112797149392898.json, 图片生成/文生图/提示词扩写+z-image文生图___qwen-image文生图_2049685174404829186.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/qwen-image+提示词扩写+8步快速lora_1956256254878470146.json、图片生成/文生图/zimage文生图_2004814222078996481.json、图片生成/文生图/失败作图工作流_2077959412047765506.json、图片生成/文生图/官流Qwen-lmage-FP8中文版_1953112797149392898.json、图片生成/文生图/提示词扩写+z-image文生图___qwen-image文生图_2049685174404829186.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `LoraLoader` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `QwenLoader` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `WanVideoPromptExtender` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `Textbox` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 720 - 1920 | 5 | 61% |
| 高度 | 1368 | 1080 - 1920 | 5 | 80% |
| 采样步数 | 8 | 8 - 20 | 5 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1920，5 个样本
- 高度 中位数 1368，观测区间 1080 - 1920，5 个样本，取值集中（一致性 80%）
- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
