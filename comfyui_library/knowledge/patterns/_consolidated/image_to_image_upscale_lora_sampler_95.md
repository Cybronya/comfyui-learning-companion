---
name: image_to_image_upscale_lora_sampler_95
type: Image To Image
frequency: 2
level: weak
coverage: 0.8325
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy float, easy getNode, easy setNode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【推荐】QwenEdit2511动漫真人转绘_2009931103217389570.json, 图片生成/图生图/真人转绘_动漫-QwenEdit2511&AIO-V18（最新优化版）_2034554167561293825.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【推荐】QwenEdit2511动漫真人转绘_2009931103217389570.json、图片生成/图生图/真人转绘_动漫-QwenEdit2511&AIO-V18（最新优化版）_2034554167561293825.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy float`
- `easy getNode`
- `easy setNode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
