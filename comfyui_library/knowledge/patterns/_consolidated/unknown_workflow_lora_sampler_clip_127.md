---
name: unknown_workflow_lora_sampler_clip_127
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.853
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RH_OneShot_Prompter, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, SeargePromptText, ShowText|pysssss, String Replace (mtb), Trim Text _O, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MajicFlus 麦橘Flux模型 加速版 基础文生图_1884864959212568577.json, 图片生成/文生图/Shuttle Jaguar 4步快速出图_1883570549694808065.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/MajicFlus 麦橘Flux模型 加速版 基础文生图_1884864959212568577.json、图片生成/文生图/Shuttle Jaguar 4步快速出图_1883570549694808065.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RH_OneShot_Prompter`
- `RH_Prompter`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeargePromptText`
- `ShowText|pysssss`
- `String Replace (mtb)`
- `Trim Text _O`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `ApplyFBCacheOnModel` —— 1/2 个有
- `EnhancedCompileModel` —— 1/2 个有
- `Int` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `ReroutePrimitive|pysssss` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1308 | - | 2 | 83% |
| 高度 | 1984 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1308，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1984，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
