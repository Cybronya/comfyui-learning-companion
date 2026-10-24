---
name: text_to_image_upscale_sampler_clip_36
type: Text To Image
frequency: 2
level: weak
coverage: 0.889
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, KSampler, LoadImage, ModelPatchLoader, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433.json, 图片生成/图生图/Z-image图生图+controlnet、反推、高清放大_1998246719987048450.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433.json、图片生成/图生图/Z-image图生图+controlnet、反推、高清放大_1998246719987048450.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `Qwen2.5VL` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `ZImageFunControlnet` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11.5 | - | 2 | 78% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1280 | - | 2 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 11.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
