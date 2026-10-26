---
name: unknown_workflow_upscale_lora_sampler_68
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.672
common_nodes: [AILab_ImagePreview, AIO_Preprocessor, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, GetImageSizeAndCount, GetNode, Image Comparer (rgthree), ImageConcanate, ImageResizeKJv2, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, Krea2StyleReference, Krea2StyleTransfer, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImageEditPlus, UNETLoader_Any, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片编辑-Krea2-风格迁移_2093512185661186050.json, 图片生成/图生图/图片编辑-Krea2-风格迁移_2093610551673974785.json, 图片生成/文生图/图片编辑-Krea2-风格迁移_2075176160165711874.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片编辑-Krea2-风格迁移_2093512185661186050.json、图片生成/图生图/图片编辑-Krea2-风格迁移_2093610551673974785.json、图片生成/文生图/图片编辑-Krea2-风格迁移_2075176160165711874.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_ImagePreview`
- `AIO_Preprocessor`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageResizeKJv2`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `Krea2StyleReference`
- `Krea2StyleTransfer`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader_Any`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
