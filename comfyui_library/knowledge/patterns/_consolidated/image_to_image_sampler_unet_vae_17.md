---
name: image_to_image_sampler_unet_vae_17
type: Image To Image
frequency: 12
level: moderate
coverage: 0.893333
common_nodes: [CFGNorm, CLIPLoader, CR Text, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen_Edit批量文本编辑图像_1958106709317341185.json, 图片生成/图生图/千问Qwen_Edit编辑模型_1957784961989574657.json, 图片生成/图生图/千问edit指定穿搭模特生成_1959662036433186818.json, 图片生成/图生图/千问万物移除_1959884154957672449.json, 图片生成/图生图/千问图像编辑Plus自定义姿势_1971090740203921410.json, 图片生成/图生图/千问最新图像编辑Plus八步加速_1975583252884885506.json, 图片生成/图生图/千问最新编辑模型Plus_1970422090648199170.json, 图片生成/图生图/千问编辑Plus批量出图_1971075893584109569.json, 图片生成/图生图/千问编辑模型Plus三图版_1970743584494415874.json, 图片生成/图生图/千问编辑模型Plus双图_1970426505799081986.json, 图片生成/图生图/图片编辑姿势完美迁移_1970415639292747778.json, 图片生成/图生图/🥯千问新王炸！2509模型图片姿势完美迁移🥯_1970302455412125698.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_17

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/千问Qwen_Edit批量文本编辑图像_1958106709317341185.json、图片生成/图生图/千问Qwen_Edit编辑模型_1957784961989574657.json、图片生成/图生图/千问edit指定穿搭模特生成_1959662036433186818.json、图片生成/图生图/千问万物移除_1959884154957672449.json、图片生成/图生图/千问图像编辑Plus自定义姿势_1971090740203921410.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
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
- `TextEncodeQwenImageEditPlus` —— 8/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `TextEncodeQwenImageEdit` —— 6/12 个有
- `AIO_Preprocessor` —— 2/12 个有
- `CR Prompt List` —— 2/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `ImageConcanate` —— 2/12 个有
- `LoraLoader` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `CR Latent Batch Size` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `Note Plus (mtb)` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 12 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 54% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | beta57 | - | 12 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 beta57，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（7/12 个样本）：Steps较低可能导致细节不足
