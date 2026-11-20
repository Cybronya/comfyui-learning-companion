---
name: image_to_image_upscale_sampler_vae_2
type: Image To Image
frequency: 8
level: strong
coverage: 0.821
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像摄影-光线迁移_1998555472812736513.json, 图片生成/图生图/人物角色多视角生成_2043946548995825665.json, 图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2084973182859173890.json, 图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2085181731505790977.json, 图片生成/图生图/光线迁移Qwen-Edit-2509_2061993950671622146.json, 图片生成/图生图/光线迁移Qwen-Edit-2509_2064187409830596610.json, 图片生成/图生图/多图像提取整合（参照 Qwen Image Edit 2511）_2070080566082494465.json, 图片生成/图生图/白底转场景-叠高清放大-cr大雄_1998636955619483650.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人像摄影-光线迁移_1998555472812736513.json、图片生成/图生图/人物角色多视角生成_2043946548995825665.json、图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2084973182859173890.json、图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2085181731505790977.json、图片生成/图生图/光线迁移Qwen-Edit-2509_2061993950671622146.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `ImageScaleBy` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `easy seed` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImageBlend` —— 1/8 个有
- `Int` —— 1/8 个有
- `Mask Fill Holes` —— 1/8 个有
- `MaskToImage` —— 1/8 个有
- `PIP_图像联结` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 8 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（13/8 个样本）：Steps较低可能导致细节不足
