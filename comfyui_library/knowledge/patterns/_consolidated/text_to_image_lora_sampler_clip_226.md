---
name: text_to_image_lora_sampler_clip_226
type: Text To Image
frequency: 5
level: moderate
coverage: 0.974
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1956256254878470146.json, 图片生成/文生图/1957086467483734017.json, 图片生成/文生图/1976489433270755329.json, 图片生成/文生图/Qwen-千问文生图工作流+LORA（电商运营海报）_1993309631191728130.json, 图片生成/文生图/zimage文生图_2004814222078996481.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_226

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1956256254878470146.json、图片生成/文生图/1957086467483734017.json、图片生成/文生图/1976489433270755329.json、图片生成/文生图/Qwen-千问文生图工作流+LORA（电商运营海报）_1993309631191728130.json、图片生成/文生图/zimage文生图_2004814222078996481.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `QwenLoader` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `WanVideoPromptExtender` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 720 - 1080 | 5 | 81% |
| 高度 | 1280 | 1024 - 1920 | 5 | 79% |
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1080，5 个样本，取值集中（一致性 81%）
- 高度 中位数 1280，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
