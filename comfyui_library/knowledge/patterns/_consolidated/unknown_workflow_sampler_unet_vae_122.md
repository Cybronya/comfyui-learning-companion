---
name: unknown_workflow_sampler_unet_vae_122
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.86
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/02-02-01-QwenEdit-双图编辑-原生_2006652720903622658.json, 图片生成/图生图/10岁LoRA——Qwen-Image-Edit应用_1963222883298414594.json, 图片生成/图生图/70岁LoRA——Qwen-Image-Edit应用_1961782664925790210.json, 图片生成/图生图/Mad裂变资产-1_1989310590176948226.json, 图片生成/图生图/Qwen Edit 2509单图编辑_1993590123661115394.json, 图片生成/图生图/Qwen-Edit-2511人物角色三视图3D国漫CG风格（图生图）_2083446869669277698.json, 图片生成/图生图/qwen2511生活照秒变精结婚照登记照片婚纱_2057652286989619201.json, 图片生成/图生图/qwen2511生活照秒变精结婚照登记照片婚纱_2061052010992070658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_122

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/02-02-01-QwenEdit-双图编辑-原生_2006652720903622658.json、图片生成/图生图/10岁LoRA——Qwen-Image-Edit应用_1963222883298414594.json、图片生成/图生图/70岁LoRA——Qwen-Image-Edit应用_1961782664925790210.json、图片生成/图生图/Mad裂变资产-1_1989310590176948226.json、图片生成/图生图/Qwen Edit 2509单图编辑_1993590123661115394.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/8 个有
- `TextEncodeQwenImageEditPlus` —— 6/8 个有
- `PreviewImage` —— 4/8 个有
- `TextEncodeQwenImageEdit` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `ImageStitch` —— 2/8 个有
- `easy imageConcat` —— 2/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `GetImageSizeAndCount` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `ttN concat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1360 | 768 - 1920 | 8 | 71% |
| 高度 | 1024 | 720 - 1920 | 8 | 68% |
| 采样步数 | 6 | 4 - 8 | 8 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1360，观测区间 768 - 1920，8 个样本
- 高度 中位数 1024，观测区间 720 - 1920，8 个样本
- 采样步数 中位数 6，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（14/8 个样本）：Steps较低可能导致细节不足
