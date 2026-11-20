---
name: image_to_image_upscale_lora_sampler_55
type: Image To Image
frequency: 4
level: strong
coverage: 0.933
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/参考图像打光 艺术照打光  Qwen-Edit-2509 + SeedVR2图片高清放大 重新打光_2041348969401425921.json, 图片生成/图生图/多角度+放大+qwen_2511_multiangle_2009943128391819266.json, 平台全量/参考图像打光 _ Qwen-Edit-2509_1890370127920013313.json, 平台全量/参考图像打光 艺术照打光  Qwen-Edit-2509 + SeedVR2图片高清放大 重新打光_2002586863250599937.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/参考图像打光 艺术照打光  Qwen-Edit-2509 + SeedVR2图片高清放大 重新打光_2041348969401425921.json、图片生成/图生图/多角度+放大+qwen_2511_multiangle_2009943128391819266.json、平台全量/参考图像打光 _ Qwen-Edit-2509_1890370127920013313.json、平台全量/参考图像打光 艺术照打光  Qwen-Edit-2509 + SeedVR2图片高清放大 重新打光_2002586863250599937.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ConstrainImage|pysssss` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `RepeatLatentBatch` —— 3/4 个有
- `CreateVideo` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `ReActorFaceSwap` —— 1/4 个有
- `VideoFrameExtractor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
