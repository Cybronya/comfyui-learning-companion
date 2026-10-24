---
name: image_to_image_sampler_unet_vae_42
type: Image To Image
frequency: 6
level: moderate
coverage: 0.899833
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json, 图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json, 图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json, 图片生成/图生图/千问编辑模型Plus三图版_1970743584494415874.json, 图片生成/图生图/千问编辑模型Plus双图_1970426505799081986.json, 图片生成/图生图/千问编辑模型Plus姿势参考_1970434003935371266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_42

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json、图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json、图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json、图片生成/图生图/千问编辑模型Plus三图版_1970743584494415874.json、图片生成/图生图/千问编辑模型Plus双图_1970426505799081986.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `ControlNetApplySD3` —— 1/6 个有
- `ControlNetLoader` —— 1/6 个有
- `ModelPatchLoader` —— 1/6 个有
- `QwenImageDiffsynthControlnet` —— 1/6 个有
- `ReferenceLatent` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 40 | 6 | 44% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 6 | 65% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 40，6 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
