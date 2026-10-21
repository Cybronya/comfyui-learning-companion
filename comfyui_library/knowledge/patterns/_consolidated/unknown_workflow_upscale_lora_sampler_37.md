---
name: unknown_workflow_upscale_lora_sampler_37
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPTextEncodeFlux, CR Aspect Ratio, CR Text, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageScaleToMegapixels, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, ModelSamplingSD3, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, OneButtonPrompt, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, Upscale Model Loader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Aspect Ratio, CR Text, CR Text Concatenate, Upscale Model Loader, Display Any (rgthree), ttN concat]
members: [图片生成/文生图/1958510775960813570.json, 图片生成/文生图/1959627535703289858.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1958510775960813570.json、图片生成/文生图/1959627535703289858.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Aspect Ratio`
- `CR Text`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageScaleToMegapixels`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `ModelSamplingSD3`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `OneButtonPrompt`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.05 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.05，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、CR Text、CR Text Concatenate、Upscale Model Loader、Display Any (rgthree)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
