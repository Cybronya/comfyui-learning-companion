---
name: unknown_workflow_sampler_clip_vae_15
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.806
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Note Plus (mtb), SDXLEmptyLatentSizePicker+]
members: [图片生成/文生图/1904465680211611649.json, 图片生成/文生图/1909669429062631425.json, 图片生成/文生图/1909854047942209538.json, 图片生成/文生图/1909968900275273729.json, 图片生成/文生图/1910633207707172866.json, 图片生成/文生图/1917844166154321921.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1904465680211611649.json、图片生成/文生图/1909669429062631425.json、图片生成/文生图/1909854047942209538.json、图片生成/文生图/1909968900275273729.json、图片生成/文生图/1910633207707172866.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuFluxDiTLoader` —— 5/6 个有
- `NunchakuFluxLoraLoader` —— 5/6 个有
- `NunchakuTextEncoderLoader` —— 5/6 个有
- `DualCLIPLoader` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `SDXLEmptyLatentSizePicker+` —— 2/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `QuadrupleCLIPLoader` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 28 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | lcm | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)、SDXLEmptyLatentSizePicker+
