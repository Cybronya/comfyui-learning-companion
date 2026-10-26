---
name: image_to_image_sampler_unet_vae_7
type: Image To Image
frequency: 15
level: weak
coverage: 0.893467
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/25.tonnie-Qwen洗图（带中文）_1998065820255289345.json, 图片生成/图生图/251207-03.Z_image_turbo图生图_1997679619232960513.json, 图片生成/图生图/87time QW 图生图_2054463234631061505.json, 图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963550771471273985.json, 图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963563706520260610.json, 图片生成/图生图/KIWI-qwen-edit-产品精修_1963557059360952321.json, 图片生成/图生图/KIWI-qwen-edit-衣服提取_1963567265559171074.json, 图片生成/图生图/Krea2图生图重绘多张对比版本，一键无脑_2091851062343983106.json, 图片生成/图生图/Krea2图生图重绘多张对比，_2101865451822338049.json, 图片生成/图生图/Qwen 2512图生图工作流（摄影、电商洗图）_2022140446385901569.json, 图片生成/图生图/qwen-edit-2509三图万物迁移_1993203591836008450.json, 图片生成/图生图/动漫转真实 Qwen-edit+Zimage 双采样_2013604515278229505.json, 图片生成/图生图/千问Edit2509图像编辑三图版_1972125442494885889.json, 图片生成/图生图/千问Edit2509图像编辑单图版_1972125938593034241.json, 图片生成/图生图/千问Edit2509图像编辑双图版_1972837097528860674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/25.tonnie-Qwen洗图（带中文）_1998065820255289345.json、图片生成/图生图/251207-03.Z_image_turbo图生图_1997679619232960513.json、图片生成/图生图/87time QW 图生图_2054463234631061505.json、图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963550771471273985.json、图片生成/图生图/KIWI-qwen-Edit图像转CG动漫_1963563706520260610.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/15 个有
- `ImageScaleToTotalPixels` —— 12/15 个有
- `ModelSamplingAuraFlow` —— 12/15 个有
- `CFGNorm` —— 10/15 个有
- `TextEncodeQwenImageEdit` —— 8/15 个有
- `CLIPTextEncode` —— 7/15 个有
- `ImageConcanate` —— 5/15 个有
- `TextEncodeQwenImageEditPlus` —— 5/15 个有
- `Display Any (rgthree)` —— 4/15 个有
- `Image Comparer (rgthree)` —— 4/15 个有
- `ImageConcatMulti` —— 4/15 个有
- `AILab_QwenVL` —— 3/15 个有
- `JjkText` —— 3/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `PreviewAny` —— 3/15 个有
- `PreviewImage` —— 3/15 个有
- `RH_LLMAPI_NODE` —— 3/15 个有
- `easy anythingIndexSwitch` —— 3/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `LayerUtility: ImageReel` —— 1/15 个有
- `LayerUtility: ImageReelComposit` —— 1/15 个有
- `RH_Captioner` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 20 | 15 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 15 | 50% |
| 采样算法 | euler | - | 15 | 87% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 15 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 20，15 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 87%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，15 个样本
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
