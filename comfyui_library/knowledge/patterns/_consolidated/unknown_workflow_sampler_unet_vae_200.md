---
name: unknown_workflow_sampler_unet_vae_200
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.794143
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json, 图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json, 图片生成/文生图/Qwen Image 2.1智能文生图_2114865899411951618.json, 图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json, 视频生成/文生视频/Qwen_Image_2.1智能文生图_2116352088610525186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_200

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Viggle 4-Step 文生图工作流_2106002263507554306.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json、图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json、图片生成/文生图/Qwen Image 2.1智能文生图_2114865899411951618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `QwenImage21Cache` —— 4/7 个有
- `PreviewAny` —— 3/7 个有
- `TextGenerate` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `Display Int (rgthree)` —— 2/7 个有
- `GoohaiUniversalSlider` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ModelAttentionBackend` —— 2/7 个有
- `Text Prompt (JPS)` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `ModelSamplingFlux` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 7 | 70% |
| 高度 | 1024 | 1024 - 2048 | 7 | 65% |
| 采样步数 | 25 | 6 - 60 | 7 | 47% |
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
- 采样步数 中位数 25，观测区间 6 - 60，7 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
