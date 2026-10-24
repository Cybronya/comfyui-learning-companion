---
name: image_to_image_lora_sampler_clip_136
type: Image To Image
frequency: 2
level: weak
coverage: 0.9245
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSizeAndCount, ImageScaleDownToSize, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, Primitive integer [Crystools], SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698.json, 视频生成/图生视频/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_1988100609951821825.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698.json、视频生成/图生视频/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_1988100609951821825.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetImageSizeAndCount`
- `ImageScaleDownToSize`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `BetterFilmGrain` —— 1/2 个有
- `CR Simple Image Compare` —— 1/2 个有
- `DuckHideNode` —— 1/2 个有
- `EsesImageEffectBloom` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6.51 | - | 2 | 16% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | res_2s | - | 2 | 50% |
| 重绘幅度 | 0.1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 6.51，样本不足，未给区间，2 个样本，取值分散，一致性仅 16%
- 调度器 最常用 res_2s，2 个样本，一致性 50%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
