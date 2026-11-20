---
name: image_to_image_sampler_unet_vae_41
type: Image To Image
frequency: 4
level: strong
coverage: 0.89875
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json, 图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json, 图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json, 图片生成/图生图/千问编辑模型Plus姿势参考_1970434003935371266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【遇见AI】Qwen-image ControlNet union版_2050876851849052161.json、图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json、图片生成/图生图/【遇见AI】Qwen-image controlnet lora版diffsynth_2050876883620909058.json、图片生成/图生图/千问编辑模型Plus姿势参考_1970434003935371266.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
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
- `LoraLoader` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `ModelPatchLoader` —— 1/4 个有
- `QwenImageDiffsynthControlnet` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 4 | 57% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 4 | 69% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
