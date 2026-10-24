---
name: image_to_image_upscale_sampler_vae_2
type: Image To Image
frequency: 11
level: moderate
coverage: 0.835273
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像摄影-光线迁移_1998555472812736513.json, 图片生成/图生图/人物角色多视角生成_2043946548995825665.json, 图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2084973182859173890.json, 图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2085181731505790977.json, 图片生成/图生图/光线迁移Qwen-Edit-2509_2061993950671622146.json, 图片生成/图生图/光线迁移Qwen-Edit-2509_2064187409830596610.json, 图片生成/图生图/打光参考图一到图二+图片编辑+打光+氛围感+高清放大+全节点注释_2056218566550147074.json, 图片生成/图生图/模特融合生成-qwen2511场景图生成指定模特，合成完美融合_2011029108976787458.json, 图片生成/图生图/高清修复_增强细节Qwen 2511-Unblur-Anything_2011418046614740993.json, 图片生成/图生图/高清放大修复-2.0_8K_2087812199464132610.json, 图片生成/图生图/高清放大修复-2026年新版【真实细节】_2003273933614907393.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/人像摄影-光线迁移_1998555472812736513.json、图片生成/图生图/人物角色多视角生成_2043946548995825665.json、图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2084973182859173890.json、图片生成/图生图/光线迁移3_批量zip_Qwen-Edit-2509_2085181731505790977.json、图片生成/图生图/光线迁移Qwen-Edit-2509_2061993950671622146.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `LoraLoaderModelOnly` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `ImageScaleBy` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `ReferenceLatent` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `CLIPTextEncode` —— 3/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/11 个有
- `Anything Everywhere3` —— 2/11 个有
- `DownloadAndLoadFlorence2Model` —— 2/11 个有
- `Florence2Run` —— 2/11 个有
- `Latent Noise Injection` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `ShowText` —— 2/11 个有
- `easy imageSizeBySide` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `DualCLIPLoader` —— 1/11 个有
- `FluxGuidance` —— 1/11 个有
- `GrowMaskWithBlur` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `PIP_图像联结` —— 1/11 个有
- `SetLatentNoiseMask` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 11 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 0.42 - 1 | 11 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 0.42 - 1，11 个样本
- 高发问题（16/11 个样本）：Steps较低可能导致细节不足
