---
name: image_to_image_sampler_unet_vae_36
type: Image To Image
frequency: 7
level: weak
coverage: 0.929429
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen超强图像编辑_1958335255000322050.json, 图片生成/图生图/单图编辑_Qwen2511_2010642367375740929.json, 图片生成/图生图/单图编辑_qwen2511_2084533535242809346.json, 图片生成/图生图/双图编辑Qwen edit 2511 千问改图_2013884239669895170.json, 图片生成/图生图/双图编辑_2067958028665704449.json, 图片生成/图生图/图像编辑 Qwen Edit 2511_2003635995813789698.json, 图片生成/图生图/多镜头自由切换！Qwen-image edit 2511_2009557606741843969.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_36

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen超强图像编辑_1958335255000322050.json、图片生成/图生图/单图编辑_Qwen2511_2010642367375740929.json、图片生成/图生图/单图编辑_qwen2511_2084533535242809346.json、图片生成/图生图/双图编辑Qwen edit 2511 千问改图_2013884239669895170.json、图片生成/图生图/双图编辑_2067958028665704449.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
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
- `LoraLoaderModelOnly` —— 6/7 个有
- `TextEncodeQwenImageEditPlus` —— 6/7 个有
- `FluxKontextImageScale` —— 5/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/7 个有
- `LayerUtility: ImageReel` —— 4/7 个有
- `LayerUtility: ImageReelComposit` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `Textbox` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ImageAndMaskPreview` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `TextEncodeQwenImageEdit` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 7 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，7 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
