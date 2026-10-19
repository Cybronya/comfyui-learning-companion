---
name: unknown_workflow_sampler_unet_vae_93
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.672429
common_nodes: [CLIPLoader, DF_Text_Box, GetNode, GoohaiRatioAndResolution, GoohaiRouteBlocker, Image Comparer (rgthree), KSampler, LoadImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, SetNode, ShowText|pysssss, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, 孤海注释, 忽略多组孤海]
problems: []
missing: [忽略多组孤海]
members: [图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json, 图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2105315513315450881.json, 图片生成/图生图/2103270694288183297.json, 图片生成/图生图/2105870849386573825.json, 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json, 图片生成/文生图/Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json, 图片生成/文生图/Qwen Image 2.1 文生、多图像编辑一体化_2105870849386573825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_93

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json、图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2105315513315450881.json、图片生成/图生图/2103270694288183297.json、图片生成/图生图/2105870849386573825.json、图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `DF_Text_Box`
- `GetNode`
- `GoohaiRatioAndResolution`
- `GoohaiRouteBlocker`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenImagePromptOptimizer`
- `RestoreQwenImage21GH`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `LoadImageGoohai` —— 4/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：忽略多组孤海
