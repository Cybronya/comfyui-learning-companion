---
name: unknown_workflow_sampler_unet_vae_150
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.880429
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json, 图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json, 图片生成/文生图/Qwen_Image_2.1文生图_2108748004588085250.json, 图片生成/文生图/Qwen_Image_2.1文生图_2110292134430593026.json, 图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_150

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json、图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json、图片生成/文生图/Qwen_Image_2.1文生图_2108748004588085250.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `SaveImageAdvanced` —— 3/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `ModelSamplingFlux` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 7 | 69% |
| 高度 | 1024 | 1024 - 2048 | 7 | 69% |
| 采样步数 | 40 | 6 - 45 | 7 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，7 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，7 个样本
- 采样步数 中位数 40，观测区间 6 - 45，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
