---
name: image_to_image_sampler_unet_vae_4
type: Image To Image
frequency: 17
level: weak
coverage: 0.910294
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/25.tonnie-Qwen洗图（带中文）_1998065820255289345.json, 图片生成/图生图/251207-03.Z_image_turbo图生图_1997679619232960513.json, 图片生成/图生图/87time QW 图生图_2054463234631061505.json, 图片生成/图生图/Krea2图生图重绘多张对比版本，一键无脑_2091851062343983106.json, 图片生成/图生图/Krea2图生图重绘多张对比，_2101865451822338049.json, 图片生成/图生图/LH-DMT版本-2.生图片类-023.Z_image_turbo图生图_2016484447947853825.json, 图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json, 图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json, 图片生成/图生图/Qwen 2512图生图工作流（摄影、电商洗图）_2022140446385901569.json, 图片生成/图生图/Qwen-Edit-指尖触摸虚拟角色_1983534381887365121.json, 图片生成/图生图/Qwen-Edit-毛绒绒饮料（冬季限定）_1980917424298049537.json, 图片生成/图生图/Qwen-Edit-海的那边是什么_1983545460763893761.json, 图片生成/图生图/Qwen-Edit-生成爆款手办_1964950491358744577.json, 图片生成/图生图/Qwen-Edit-科幻星空眼睛_1984170750527602690.json, 图片生成/图生图/一句话改变图片！图片编辑_1999431845727043586.json, 图片生成/图生图/动漫转真实 Qwen-edit+Zimage 双采样_2013604515278229505.json, 图片生成/图生图/通义千问2509双图编辑_1985768716262617090.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/25.tonnie-Qwen洗图（带中文）_1998065820255289345.json、图片生成/图生图/251207-03.Z_image_turbo图生图_1997679619232960513.json、图片生成/图生图/87time QW 图生图_2054463234631061505.json、图片生成/图生图/Krea2图生图重绘多张对比版本，一键无脑_2091851062343983106.json、图片生成/图生图/Krea2图生图重绘多张对比，_2101865451822338049.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/17 个有
- `ModelSamplingAuraFlow` —— 12/17 个有
- `CLIPTextEncode` —— 10/17 个有
- `ImageScaleToTotalPixels` —— 10/17 个有
- `CFGNorm` —— 9/17 个有
- `Image Comparer (rgthree)` —— 9/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/17 个有
- `TextEncodeQwenImageEdit` —— 7/17 个有
- `AILab_QwenVL` —— 3/17 个有
- `PreviewAny` —— 3/17 个有
- `easy cleanGpuUsed` —— 3/17 个有
- `CR Text` —— 2/17 个有
- `TextEncodeQwenImageEditPlus` —— 2/17 个有
- `Display Any (rgthree)` —— 1/17 个有
- `LayerUtility: ImageReel` —— 1/17 个有
- `LayerUtility: ImageReelComposit` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `RH_Captioner` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 20 | 17 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 17 | 50% |
| 采样算法 | euler | - | 17 | 88% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 0.7 | 0.23 - 1 | 17 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 20，17 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 88%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 0.7，观测区间 0.23 - 1，17 个样本
- 高发问题（20/17 个样本）：Steps较低可能导致细节不足
