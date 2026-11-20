---
name: image_to_image_controlnet_sampler_clip_11
type: Image To Image
frequency: 4
level: strong
coverage: 0.59125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, Image Comparer (rgthree), ImageAndMaskPreview, KSampler, LanPaint_MaskBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, ModelPatchLoader, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AA--Zimage-局部重绘+4K放大_2006950200786554882.json, 图片生成/图生图/局部重绘_2059477250227138562.json, 图片生成/图生图/局部重绘_2059506283165868033.json, 平台全量/Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AA--Zimage-局部重绘+4K放大_2006950200786554882.json、图片生成/图生图/局部重绘_2059477250227138562.json、图片生成/图生图/局部重绘_2059506283165868033.json、平台全量/Z-image-Tubro+Controlnet_自动提示词扩图-高清修复_2042864855950041090.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `KSampler`
- `LanPaint_MaskBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelPatchLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `ImageToMask` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `INTConstant` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 4 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
