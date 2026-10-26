---
name: image_to_image_sampler_vae_28
type: Image To Image
frequency: 3
level: strong
coverage: 0.730667
common_nodes: [CLIPLoader, CR Text, Image Comparer (rgthree), ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RHHiddenNodes, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Imgae_Edit优质定向唯美打光进阶工作流_2096870791186046978.json, 图片生成/图生图/Qwen_Imgae_Edit优质定向唯美打光进阶工作流_2097163277645209602.json, 图片生成/文生图/Qwen Edit 三图换装+图片编辑+全节点注释_2076371541939539970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen_Imgae_Edit优质定向唯美打光进阶工作流_2096870791186046978.json、图片生成/图生图/Qwen_Imgae_Edit优质定向唯美打光进阶工作流_2097163277645209602.json、图片生成/文生图/Qwen Edit 三图换装+图片编辑+全节点注释_2076371541939539970.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LayerColor: Brightness & Contrast` —— 2/3 个有
- `VRAM_Debug` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
