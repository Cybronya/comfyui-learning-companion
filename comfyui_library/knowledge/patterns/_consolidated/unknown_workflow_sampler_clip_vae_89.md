---
name: unknown_workflow_sampler_clip_vae_89
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.703
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), KSampler (Efficient), LoadImage, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, PreviewImage, Prompts Everywhere, ReferenceLatent, SaveImage, Seed Everywhere, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Kontext Presets  官方预设提示词_1949648062012104705.json, 平台全量/一键运行：Flux_kontext 图像融合，电商专用_1949643121243627521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_89

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Kontext Presets  官方预设提示词_1949648062012104705.json、平台全量/一键运行：Flux_kontext 图像融合，电商专用_1949643121243627521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `PreviewImage`
- `Prompts Everywhere`
- `ReferenceLatent`
- `SaveImage`
- `Seed Everywhere`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BiRefNet_Hugo` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `JanusImageUnderstanding` —— 1/2 个有
- `JanusModelLoader` —— 1/2 个有
- `LoadKontextPresets` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
