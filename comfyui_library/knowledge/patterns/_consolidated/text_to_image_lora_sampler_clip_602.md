---
name: text_to_image_lora_sampler_clip_602
type: Text To Image
frequency: 2
level: weak
coverage: 0.9405
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Beyond Reality Z-image人像写真换脸_2006760693088915457.json, 图片生成/图生图/角色壁纸-2511_2052886735515860993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_602

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Beyond Reality Z-image人像写真换脸_2006760693088915457.json、图片生成/图生图/角色壁纸-2511_2052886735515860993.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `FaceToMask` —— 1/2 个有
- `GetImage` —— 1/2 个有
- `ImageBlendResize` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `scale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1372 | - | 2 | 79% |
| 高度 | 1424 | - | 2 | 65% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 20% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1372，样本不足，未给区间，2 个样本
- 高度 中位数 1424，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值分散，一致性仅 20%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
