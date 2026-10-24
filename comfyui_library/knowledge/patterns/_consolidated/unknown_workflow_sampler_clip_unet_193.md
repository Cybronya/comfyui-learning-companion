---
name: unknown_workflow_sampler_clip_unet_193
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.858571
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-Pruning版本更低显存质量一致_1968866874069065729.json, 图片生成/文生图/Z-image-base文生图8部加速版_2033075055076319234.json, 图片生成/文生图/Zimage base fp8一键出模特大片_2016314793744932866.json, 图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json, 图片生成/文生图/唯一讲述着专用Z-image造像_2000531408500162562.json, 图片生成/文生图/小说推文古风小说推文抖音超火_1991148887255920641.json, 图片生成/文生图/沙雕动漫超火古风人物加速_1966870624557731842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_193

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-Pruning版本更低显存质量一致_1968866874069065729.json、图片生成/文生图/Z-image-base文生图8部加速版_2033075055076319234.json、图片生成/文生图/Zimage base fp8一键出模特大片_2016314793744932866.json、图片生成/文生图/z base 文生图+豆包4.5训练的lora_2020451805334872066.json、图片生成/文生图/唯一讲述着专用Z-image造像_2000531408500162562.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `EmptySD3LatentImage` —— 4/7 个有
- `easy promptConcat` —— 4/7 个有
- `SDXLEmptyLatentSizePicker+` —— 3/7 个有
- `CR Prompt List` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `CR Upscale Image` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.72) | - | 3 | 67% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 9 | 4 - 30 | 7 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 36% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 832x1152 (0.72)，3 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，观测区间 4 - 30，7 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
