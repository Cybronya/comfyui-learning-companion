---
name: unknown_workflow_upscale_lora_sampler_65
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.745
common_nodes: [AutoCropFaces, CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GGUFLoaderKJ, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAELoader, easy ifElse]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/脸部生成全身照Qwen Image Edit AIO 版_2075080327214755842.json, 图片生成/图生图/脸部生成全身照洗图版_2075078074802196482.json, 图片生成/图生图/高还原度换脸 Qwen Image Edit F2P lora_2075075662355980290.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/脸部生成全身照Qwen Image Edit AIO 版_2075080327214755842.json、图片生成/图生图/脸部生成全身照洗图版_2075078074802196482.json、图片生成/图生图/高还原度换脸 Qwen Image Edit F2P lora_2075075662355980290.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GGUFLoaderKJ`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAELoader`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `CFGNorm` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `Float` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageRemoveAlpha+` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `LayerMask: HumanPartsUltra` —— 1/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `VAEDecode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 0.7 - 1 | 3 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
