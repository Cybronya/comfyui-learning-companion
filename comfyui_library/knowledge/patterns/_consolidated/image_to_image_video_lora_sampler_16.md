---
name: image_to_image_video_lora_sampler_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.9005
common_nodes: [AddNode, CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DF_Get_image_size, Film Grain, GetImageSizeAndCount, ImageFromBatch, ImageScaleToTotalPixels, JWInteger, KSampler, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, PreviewImage, SDVN Any Show, SaveImage, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1988469039846572033.json, 视频生成/图生视频/1987350549395869697.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1988469039846572033.json、视频生成/图生视频/1987350549395869697.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AddNode`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DF_Get_image_size`
- `Film Grain`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewImage`
- `SDVN Any Show`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
