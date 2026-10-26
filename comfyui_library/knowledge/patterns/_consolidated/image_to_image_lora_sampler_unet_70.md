---
name: image_to_image_lora_sampler_unet_70
type: Image To Image
frequency: 8
level: strong
coverage: 0.72425
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-Edit 换衣换装服装展示_2062294033308938242.json, 图片生成/图生图/Qwen+Edit-2511图案提取_2032070399328002049.json, 图片生成/图生图/Qwen-Edit-2511-单图编辑版_2005473838425141249.json, 图片生成/图生图/Qwen-Edit-2511多图编辑版_2005543074220699649.json, 图片生成/图生图/qwen-edit-2511-单图编辑版_2008375703594602498.json, 图片生成/图生图/多图像提取整合（参照 Qwen Image Edit 2511）_2070080566082494465.json, 图片生成/图生图/🤗老许：Qwen-Edit-2511-全编辑丨四大常用工作流+两种放大工作流合集_2005940430791475202.json, 图片生成/文生图/Qwen-Edit 2511 单_多图编辑，人物换装，解决偏色和像素偏移，SeedVR2高清修复_2004097023886434305.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit 换衣换装服装展示_2062294033308938242.json、图片生成/图生图/Qwen+Edit-2511图案提取_2032070399328002049.json、图片生成/图生图/Qwen-Edit-2511-单图编辑版_2005473838425141249.json、图片生成/图生图/Qwen-Edit-2511多图编辑版_2005543074220699649.json、图片生成/图生图/qwen-edit-2511-单图编辑版_2008375703594602498.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `Image Comparer (rgthree)` —— 7/8 个有
- `CFGNorm` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `TextEncodeQwenImageEditPlus` —— 6/8 个有
- `LayerUtility: ImageReel` —— 5/8 个有
- `LayerUtility: ImageReelComposit` —— 5/8 个有
- `ReferenceLatent` —— 5/8 个有
- `ModelSamplingAuraFlow` —— 4/8 个有
- `SeedVR2LoadDiTModel` —— 4/8 个有
- `SeedVR2LoadVAEModel` —— 4/8 个有
- `SeedVR2VideoUpscaler` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `Int` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `DWPreprocessor` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `FluxKontextImageScale` —— 1/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `LayerColor: ColorAdapter` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy promptLine` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler_ancestral | - | 8 | 62% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 62%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（17/8 个样本）：Steps较低可能导致细节不足
