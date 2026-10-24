---
name: image_to_image_controlnet_lora_sampler_13
type: Image To Image
frequency: 2
level: weak
coverage: 0.688
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ClownsharKSampler_Beta, ConditioningZeroOut, EmptySD3LatentImage, FaceAnalysisModels, FaceEmbedDistance, GrowMaskWithBlur, Image Comparer (rgthree), ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview, ModelPatchLoader, ModelSamplingAuraFlow, PreviewAny, PreviewImage, PrimitiveInt, SAM3_Detect, SaveImage, SetLatentNoiseMask, TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913.json, 图片生成/文生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913.json、图片生成/文生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ClownsharKSampler_Beta`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `SAM3_Detect`
- `SaveImage`
- `SetLatentNoiseMask`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | -1 | - | 1 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
