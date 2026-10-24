---
name: image_to_image_sampler_unet_vae_21
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8814
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen_Edit批量文本编辑图像_1958106709317341185.json, 图片生成/图生图/千问Qwen_Edit编辑模型_1957784961989574657.json, 图片生成/图生图/千问edit指定穿搭模特生成_1959662036433186818.json, 图片生成/图生图/千问万物移除_1959884154957672449.json, 图片生成/图生图/千问图像编辑Plus自定义姿势_1971090740203921410.json, 图片生成/图生图/千问最新图像编辑Plus八步加速_1975583252884885506.json, 图片生成/图生图/千问最新编辑模型Plus_1970422090648199170.json, 图片生成/图生图/千问编辑Plus批量出图_1971075893584109569.json, 图片生成/图生图/千问编辑put it here万物溶图_1965372671791874050.json, 图片生成/图生图/溶图打光-透视纠正_1980932243189317633.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_21

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/千问Qwen_Edit批量文本编辑图像_1958106709317341185.json、图片生成/图生图/千问Qwen_Edit编辑模型_1957784961989574657.json、图片生成/图生图/千问edit指定穿搭模特生成_1959662036433186818.json、图片生成/图生图/千问万物移除_1959884154957672449.json、图片生成/图生图/千问图像编辑Plus自定义姿势_1971090740203921410.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 9/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `TextEncodeQwenImageEdit` —— 5/10 个有
- `TextEncodeQwenImageEditPlus` —— 5/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `CR Prompt List` —— 2/10 个有
- `FastCanvas` —— 2/10 个有
- `FastCanvasTool` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `CR Latent Batch Size` —— 1/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `LayerUtility: CropByMask V2` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `MaskToImage` —— 1/10 个有
- `RMBG` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 10 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 10 | 57% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（6/10 个样本）：Steps较低可能导致细节不足
