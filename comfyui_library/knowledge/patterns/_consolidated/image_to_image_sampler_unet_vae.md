---
name: image_to_image_sampler_unet_vae
type: Image To Image
frequency: 6
level: moderate
coverage: 0.908667
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Seed]
members: [图片生成/文生图/1979253121035702273.json, 图片生成/文生图/Qwen Edit 2511单图编辑_2073294347310821377.json, 图片生成/文生图/Qwen Edit 2511双图编辑_2073294666874843138.json, 图片生成/文生图/workflow_2073294866825695233.json, 图片生成/文生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2079820923355615233.json, 图片生成/文生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2079833773604171778.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1979253121035702273.json、图片生成/文生图/Qwen Edit 2511单图编辑_2073294347310821377.json、图片生成/文生图/Qwen Edit 2511双图编辑_2073294666874843138.json、图片生成/文生图/workflow_2073294866825695233.json、图片生成/文生图/图像编辑四合一 Qwen-Image-Edit-2511完美改图_2079820923355615233.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `DWPreprocessor` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `InpaintModelConditioning` —— 2/6 个有
- `Mask Fill Holes` —— 2/6 个有
- `SDXLEmptyLatentSizePicker+` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CR Seed` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 6 | 57% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 6 | 65% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 768x1280 (0.6) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 最常用 768x1280 (0.6)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（9/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Seed
