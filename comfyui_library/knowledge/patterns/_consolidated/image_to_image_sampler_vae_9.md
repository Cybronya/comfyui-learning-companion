---
name: image_to_image_sampler_vae_9
type: Image To Image
frequency: 14
level: moderate
coverage: 0.883643
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/丰胸神器 一键变plump! - 千问Qwen2511_2005632117461708801.json, 图片生成/图生图/丰胸神器 一键变plump! - 千问Qwen2511_2030944455557124097.json, 图片生成/图生图/丰胸神器-胸部增大-雯雯的后宫_2075590081682960386.json, 图片生成/图生图/丰胸神器-胸部增强-胸部变大-一键变plump! Qwen2511_2077672131277705217.json, 图片生成/图生图/丰胸神器-胸部增强-胸部变大-一键变plump! Qwen2511_2077925230835748865.json, 图片生成/图生图/产品增加光影_2022309920766431234.json, 图片生成/图生图/产品摄影背景迁移 qwen_image_edit_2511_2015810728174821378.json, 图片生成/图生图/人像摄影-光线迁移_1998555472812736513.json, 图片生成/图生图/人物角色多视角生成_2043946548995825665.json, 图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2084973182859173890.json, 图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2085181731505790977.json, 图片生成/图生图/光线迁移Qwen-Edit-2509_2061993950671622146.json, 图片生成/图生图/光线迁移Qwen-Edit-2509_2064187409830596610.json, 图片生成/图生图/白底转场景-叠高清放大-cr大雄_1998636955619483650.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/丰胸神器 一键变plump! - 千问Qwen2511_2005632117461708801.json、图片生成/图生图/丰胸神器 一键变plump! - 千问Qwen2511_2030944455557124097.json、图片生成/图生图/丰胸神器-胸部增大-雯雯的后宫_2075590081682960386.json、图片生成/图生图/丰胸神器-胸部增强-胸部变大-一键变plump! Qwen2511_2077672131277705217.json、图片生成/图生图/丰胸神器-胸部增强-胸部变大-一键变plump! Qwen2511_2077925230835748865.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `SeedVR2LoadDiTModel` —— 12/14 个有
- `SeedVR2LoadVAEModel` —— 12/14 个有
- `SeedVR2VideoUpscaler` —— 12/14 个有
- `Fast Groups Muter (rgthree)` —— 5/14 个有
- `ImageScaleBy` —— 5/14 个有
- `PreviewImage` —— 4/14 个有
- `easy seed` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `ImageBlend` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `Mask Fill Holes` —— 1/14 个有
- `MaskToImage` —— 1/14 个有
- `PIP_图像联结` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有
- `easy imageSize` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 14 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 14 | 65% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，14 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
