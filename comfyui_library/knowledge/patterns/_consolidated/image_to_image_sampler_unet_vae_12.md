---
name: image_to_image_sampler_unet_vae_12
type: Image To Image
frequency: 12
level: weak
coverage: 0.942333
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/上传图片 2K 高清放大（zimage turbo）_2057112481067261953.json, 图片生成/图生图/赛博玄幻·湘灵 女主｜图生图_2093230068645584897.json, 图片生成/图生图/赛博玄幻修仙者｜墨渊·图生图_2093285943129231361.json, 图片生成/图生图/赛博玄幻修仙者｜燕青·图生图_2093374930367901697.json, 图片生成/图生图/转现实场景qwen_2001592460314853378.json, 图片生成/图生图/👾怪獸-自动丰胸👾_2014653557068271618.json, 图片生成/文生图/Qwen Image Edit 2511-三图编辑-圣诞节快乐_2003966404120461313.json, 图片生成/文生图/Qwen-Image-Edit镜头控制_1990374981525803009.json, 图片生成/文生图/image_qwen_image_edit_2511-三图参考-换沙发+人物_2004738010233139201.json, 图片生成/文生图/image_qwen_image_edit_2511-单图参考-上色_2004744836605505538.json, 图片生成/文生图/image_qwen_image_edit_2511-单图参考-转写实_2005067891861061634.json, 图片生成/文生图/image_qwen_image_edit_2511-双图参考-沙发换材质_2004736076759662593.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_12

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/上传图片 2K 高清放大（zimage turbo）_2057112481067261953.json、图片生成/图生图/赛博玄幻·湘灵 女主｜图生图_2093230068645584897.json、图片生成/图生图/赛博玄幻修仙者｜墨渊·图生图_2093285943129231361.json、图片生成/图生图/赛博玄幻修仙者｜燕青·图生图_2093374930367901697.json、图片生成/图生图/转现实场景qwen_2001592460314853378.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `CFGNorm` —— 8/12 个有
- `TextEncodeQwenImageEditPlus` —— 8/12 个有
- `ImageScaleToTotalPixels` —— 7/12 个有
- `CLIPTextEncode` —— 5/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/12 个有
- `ImageScaleBy` —— 2/12 个有
- `ImageUpscaleWithModel` —— 2/12 个有
- `UpscaleModelLoader` —— 2/12 个有
- `ImageCompare` —— 1/12 个有
- `easy promptLine` —— 1/12 个有
- `easy seed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 22 | 12 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 12 | 29% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 67% |
| 重绘幅度 | 1 | 0.3 - 1 | 12 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 22，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，12 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，12 个样本
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
