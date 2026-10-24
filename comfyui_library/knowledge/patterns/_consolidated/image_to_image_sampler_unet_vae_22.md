---
name: image_to_image_sampler_unet_vae_22
type: Image To Image
frequency: 9
level: weak
coverage: 0.877111
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/01-06-01-QwenImage图生图V1（文字自动修复）_1986833915342221314.json, 图片生成/图生图/3d卡通可爱系风格-klein_2042859666035712002.json, 图片生成/图生图/F2K 白模建筑参考图渲染（指定风格参考图）_2058049321479794689.json, 图片生成/图生图/FireRed-Image-Edit 图像编辑（单图、双图、三图）_2025816421023879170.json, 图片生成/图生图/FireRed-Image-Edit-1.0 老照片修复重新上色_2026822786328563714.json, 图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json, 图片生成/图生图/Qwen-Edit-2509图像编辑_1981990949586903042.json, 图片生成/图生图/小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026.json, 图片生成/文生图/B妮B妳_Qwen Edit-2511_N_S_F_W_汇总_2019388996597583874.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_22

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/01-06-01-QwenImage图生图V1（文字自动修复）_1986833915342221314.json、图片生成/图生图/3d卡通可爱系风格-klein_2042859666035712002.json、图片生成/图生图/F2K 白模建筑参考图渲染（指定风格参考图）_2058049321479794689.json、图片生成/图生图/FireRed-Image-Edit 图像编辑（单图、双图、三图）_2025816421023879170.json、图片生成/图生图/FireRed-Image-Edit-1.0 老照片修复重新上色_2026822786328563714.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `CFGNorm` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `TextEncodeQwenImageEditPlus` —— 6/9 个有
- `EmptySD3LatentImage` —— 5/9 个有
- `ReferenceLatent` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `CLIPTextEncode` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `Seed Generator` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `Flux2KleinModelConfig_EditUtils` —— 1/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/9 个有
- `HAIGC_SaveImagesToZip` —— 1/9 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/9 个有
- `scale` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 30 | 9 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 72% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 0.3 - 1 | 9 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 30，9 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，9 个样本
- 高发问题（14/9 个样本）：Steps较低可能导致细节不足
