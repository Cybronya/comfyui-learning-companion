---
name: text_to_image_lora_sampler_clip_619
type: Text To Image
frequency: 2
level: weak
coverage: 0.9015
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimpleWithSwitch, CompressImages, ConditioningZeroOut, EmptyLatentImage, FlowMatchEulerDiscreteScheduler (Custom), FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, Image Filter Adjustments, JjkText, KSampler, KSamplerSelect, Krea2OstrisEditModelPatch, LoadImage, LoraLoader, LoraLoaderModelOnly, PrimitiveInt, ResizeImageMaskNode, SamplerCustom, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitSigmasDenoise, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy loraStack, easy loraStackApply, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2动漫转真人放大Z洗图｜图生图超真实写实风格_2091590712671428609.json, 图片生成/图生图/动漫转真人写实神作｜Krea2放大+Z洗图图生图_2091761742648004610.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_619

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2动漫转真人放大Z洗图｜图生图超真实写实风格_2091590712671428609.json、图片生成/图生图/动漫转真人写实神作｜Krea2放大+Z洗图图生图_2091761742648004610.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimpleWithSwitch`
- `CompressImages`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Filter Adjustments`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SplitSigmasDenoise`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy loraStack`
- `easy loraStackApply`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
