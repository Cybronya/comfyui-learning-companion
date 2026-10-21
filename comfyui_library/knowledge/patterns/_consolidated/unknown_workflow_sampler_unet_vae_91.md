---
name: unknown_workflow_sampler_unet_vae_91
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.696
common_nodes: [CLIPLoader, DF_Text_Box, GoohaiRatioAndResolution, GoohaiRouteBlocker, Image Comparer (rgthree), KSampler, LoadImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenImagePromptOptimizer, RestoreQwenImage21GH, SaveImage, ShowText|pysssss, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, 忽略多组孤海]
problems: []
missing: [忽略多组孤海]
members: [图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json, 图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2105315513315450881.json, 图片生成/图生图/2103270694288183297.json, 图片生成/图生图/2105870849386573825.json, 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2108120997114245121.json, 图片生成/文生图/Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json, 图片生成/文生图/Qwen Image 2.1 文生、多图像编辑一体化_2105870849386573825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json、图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2105315513315450881.json、图片生成/图生图/2103270694288183297.json、图片生成/图生图/2105870849386573825.json、图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `DF_Text_Box`
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
- `ShowText|pysssss`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `LoadImageGoohai` —— 5/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：忽略多组孤海
