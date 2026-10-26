---
name: text_to_image_controlnet_upscale_lora_14
type: Text To Image
frequency: 2
level: weak
coverage: 0.757
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, ImageScaleBy, ImageScaleToTotalPixels, JoinStrings, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetUnionControlNetType, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去AI感洗图 顶级洗图 去除AI感 超清放大 模拟真实图像_2051148406344699906.json, 图片生成/图生图/抄图像的风格：文生图_上传图 然后抄风格 洗图工作流 v2(配教程，新手更友好)_2033194120537186305.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/去AI感洗图 顶级洗图 去除AI感 超清放大 模拟真实图像_2051148406344699906.json、图片生成/图生图/抄图像的风格：文生图_上传图 然后抄风格 洗图工作流 v2(配教程，新手更友好)_2033194120537186305.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetUnionControlNetType`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `ColorCorrect` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RunningHub_ImageQwenI2L_Loader(Style)` —— 1/2 个有
- `RunningHub_ImageQwenI2L_LoraGenerator` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 0.85 | - | 2 | 82% |
| ControlNet 权重 | 0.9 | - | 2 | 89% |
| 宽度 | 924 | - | 2 | 83% |
| 高度 | 1500 | - | 2 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 宽度 中位数 924，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1500，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
