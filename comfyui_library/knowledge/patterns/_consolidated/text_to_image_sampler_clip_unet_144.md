---
name: text_to_image_sampler_clip_unet_144
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8634
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image镜片·光学镜片场景生成_2044682719262674946.json, 图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json, 图片生成/文生图/Z-image最强真实人物细节多场景生成_2003710733722525697.json, 图片生成/文生图/qwen-image+提示词扩写+8步快速lora_1956256254878470146.json, 图片生成/文生图/提示词扩写+z-image文生图___qwen-image文生图_2049685174404829186.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_144

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image镜片·光学镜片场景生成_2044682719262674946.json、图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json、图片生成/文生图/Z-image最强真实人物细节多场景生成_2003710733722525697.json、图片生成/文生图/qwen-image+提示词扩写+8步快速lora_1956256254878470146.json、图片生成/文生图/提示词扩写+z-image文生图___qwen-image文生图_2049685174404829186.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoraLoader` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `easy promptList` —— 3/5 个有
- `AspectRatio` —— 2/5 个有
- `QwenLoader` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `WanVideoPromptExtender` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `HAIGC_SaveImagesToZip` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 5 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1104 | 720 - 1920 | 5 | 63% |
| 高度 | 1280 | 1080 - 1536 | 5 | 85% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 3 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，5 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1104，观测区间 720 - 1920，5 个样本
- 高度 中位数 1280，观测区间 1080 - 1536，5 个样本，取值集中（一致性 85%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
