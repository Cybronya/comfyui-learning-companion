---
name: image_to_image_lora_sampler_unet_162
type: Image To Image
frequency: 3
level: strong
coverage: 0.848333
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, GenerateNoise, GetImageSize, Image Comparer (rgthree), KSampler, LGNoiseInjectionLatent, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511真0偏移真实画风方案_2003800935149281282.json, 图片生成/图生图/QW2511任意尺寸无偏移_2008215285597216770.json, 图片生成/图生图/qwen-2511-edit+噪声添加+图像缩放基础工作流_2005594224324210690.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_162

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2511真0偏移真实画风方案_2003800935149281282.json、图片生成/图生图/QW2511任意尺寸无偏移_2008215285597216770.json、图片生成/图生图/qwen-2511-edit+噪声添加+图像缩放基础工作流_2005594224324210690.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GenerateNoise`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LGNoiseInjectionLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `easy imagePixelPerfect` —— 2/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `PixelSnapping` —— 1/3 个有
- `PowerfulMaskCrop` —— 1/3 个有
- `PowerfulMaskRestore` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 7 | 3 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 7，3 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
