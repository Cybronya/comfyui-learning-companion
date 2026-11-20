---
name: image_to_image_upscale_lora_sampler_74
type: Image To Image
frequency: 2
level: weak
coverage: 0.875
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, CLIPVisionEncode, ConditioningZeroOut, EmptyLatentHunyuan3Dv2, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Hunyuan3Dv2Conditioning, Image Comparer (rgthree), ImageOnlyCheckpointLoader, ImageResize+, ImageResizeKJv2, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveGLB, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeHunyuan3D, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, VoxelToMesh, easy cleanGpuUsed, easy imageRemBg, easy imageSizeBySide]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/006.Hunyuan模型创建003.指定角度模型产品互转_2035396565627572225.json, 图片生成/图生图/电商产品指定角度场景一致性【3D模型+任意角度】_2000045248841740289.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_74

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/006.Hunyuan模型创建003.指定角度模型产品互转_2035396565627572225.json、图片生成/图生图/电商产品指定角度场景一致性【3D模型+任意角度】_2000045248841740289.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `CLIPVisionEncode`
- `ConditioningZeroOut`
- `EmptyLatentHunyuan3Dv2`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Hunyuan3Dv2Conditioning`
- `Image Comparer (rgthree)`
- `ImageOnlyCheckpointLoader`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveGLB`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeHunyuan3D`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `VoxelToMesh`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.75 | - | 2 | 67% |
| 宽度 | 3000 | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 宽度 中位数 3000，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
