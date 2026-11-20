---
name: text_to_image_lora_sampler_clip_416
type: Text To Image
frequency: 5
level: moderate
coverage: 0.913
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图_2112777126146568193.json, 图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json, 图片生成/文生图/ZIMAGE-杰洛特文生图_2044311451736739841.json, 图片生成/文生图/pipi-anima-普通采样器基础文生图工作流_2064683171064672258.json, 图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_416

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image文生图_2112777126146568193.json、图片生成/文生图/Z-image照片级超真实人物_2008470665782894594.json、图片生成/文生图/ZIMAGE-杰洛特文生图_2044311451736739841.json、图片生成/文生图/pipi-anima-普通采样器基础文生图工作流_2064683171064672258.json、图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 18% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 800 - 1920 | 5 | 68% |
| 高度 | 1536 | 1080 - 2160 | 5 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 800 - 1920，5 个样本
- 高度 中位数 1536，观测区间 1080 - 2160，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
