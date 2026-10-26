---
name: unknown_workflow_sampler_unet_vae_134
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.84975
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json, 图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json, 图片生成/文生图/Qwen-image2.1文生图3D国漫CG风格_2112960915317547010.json, 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json, 图片生成/文生图/Qwen_Image_2.1_文生图_6步加速无PE_2107979311847399426.json, 图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_134

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json、图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json、图片生成/文生图/Qwen-image2.1文生图3D国漫CG风格_2112960915317547010.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `QwenImage21Cache` —— 3/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `ModelAttentionBackend` —— 1/8 个有
- `ModelSamplingFlux` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 1024 - 2048 | 8 | 72% |
| 高度 | 1512 | 1024 - 2048 | 8 | 67% |
| 采样步数 | 17 | 6 - 40 | 8 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1088，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1512，观测区间 1024 - 2048，8 个样本
- 采样步数 中位数 17，观测区间 6 - 40，8 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
