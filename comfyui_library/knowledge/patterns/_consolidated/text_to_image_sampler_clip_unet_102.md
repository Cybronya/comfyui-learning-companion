---
name: text_to_image_sampler_clip_unet_102
type: Text To Image
frequency: 7
level: strong
coverage: 0.974
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image+提示词扩写+8步快速lora_1956256254878470146.json, 图片生成/文生图/zimage文生图_2004814222078996481.json, 图片生成/文生图/写实 文生图_2068912035760529409.json, 图片生成/文生图/太猛了！Z-image文生图新王-支持中文！_1995051018658492417.json, 图片生成/文生图/徽派建筑klein_2063615144353165314.json, 图片生成/文生图/怀旧农村写实风格工作流_2000925300957605889.json, 图片生成/文生图/提示词扩写+z-image文生图___qwen-image文生图_2049685174404829186.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/qwen-image+提示词扩写+8步快速lora_1956256254878470146.json、图片生成/文生图/zimage文生图_2004814222078996481.json、图片生成/文生图/写实 文生图_2068912035760529409.json、图片生成/文生图/太猛了！Z-image文生图新王-支持中文！_1995051018658492417.json、图片生成/文生图/徽派建筑klein_2063615144353165314.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 5/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `QwenLoader` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `WanVideoPromptExtender` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.9 - 1 | 5 | 96% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 720 - 1920 | 7 | 65% |
| 高度 | 1280 | 1024 - 1920 | 7 | 74% |
| 采样步数 | 8 | 4 - 10 | 7 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.9 - 1，5 个样本，取值集中（一致性 96%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1920，7 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，7 个样本
- 采样步数 中位数 8，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
