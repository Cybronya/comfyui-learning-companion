---
name: unknown_workflow_upscale_lora_sampler_121
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.802
common_nodes: [AILab_QwenVL, BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, DyPE_FLUX, EmptyImage, EmptyLatentImage, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewBridge, PreviewImage, SamplerCustom, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy imageSize, easy positive, easy promptConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/qwen-image-2512-手机壁纸生成-最纯粹的文生图-批量生成_2026156357417701377.json, 图片生成/文生图/z-image-造像-壁纸生成-批量生成-v2_1998251373164658690.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/qwen-image-2512-手机壁纸生成-最纯粹的文生图-批量生成_2026156357417701377.json、图片生成/文生图/z-image-造像-壁纸生成-批量生成-v2_1998251373164658690.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `DyPE_FLUX`
- `EmptyImage`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewBridge`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy positive`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `BasicGuider` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactMakeAnyList` —— 1/2 个有
- `JDCN_StringToList` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `Qwen2.5` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SamplerEulerAncestral` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy imageSizeBySide` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
