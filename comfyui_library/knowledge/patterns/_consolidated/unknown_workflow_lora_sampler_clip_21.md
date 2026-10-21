---
name: unknown_workflow_lora_sampler_clip_21
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9051
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RH_OneShot_Prompter, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, SeargePromptText, ShowText|pysssss, String Replace (mtb), Trim Text _O, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MajicFlus 基础文生图_2071392066793459713.json, 图片生成/文生图/MajicFlus 基础文生图_2071498176409980929.json, 图片生成/文生图/MajicFlus 基础文生图_2071501043489394690.json, 图片生成/文生图/MajicFlus 基础文生图_2074740347225333762.json, 图片生成/文生图/MajicFlus 基础文生图_2075138903039893506.json, 图片生成/文生图/MajicFlus 文生图_极速版_2016027994061541378.json, 图片生成/文生图/MajicFlus 麦橘Flux模型 加速版 基础文生图_1884864959212568577.json, 图片生成/文生图/Shuttle Jaguar 4步快速出图_1883570549694808065.json, 图片生成/文生图/Text-to-Image-MajicFlus 麦橘Flux模型 基础文生图_2069321054610350082.json, 图片生成/文生图/基础文生图_2064962939718819841.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/MajicFlus 基础文生图_2071392066793459713.json、图片生成/文生图/MajicFlus 基础文生图_2071498176409980929.json、图片生成/文生图/MajicFlus 基础文生图_2071501043489394690.json、图片生成/文生图/MajicFlus 基础文生图_2074740347225333762.json、图片生成/文生图/MajicFlus 基础文生图_2075138903039893506.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
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
- `AddLabel` —— 9/10 个有
- `SDXLEmptyLatentSizePicker+` —— 9/10 个有
- `Label (rgthree)` —— 3/10 个有
- `ApplyFBCacheOnModel` —— 1/10 个有
- `EnhancedCompileModel` —— 1/10 个有
- `Int` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `ModelSamplingFlux` —— 1/10 个有
- `ReroutePrimitive|pysssss` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1080 - 1536 | 10 | 91% |
| 高度 | 2048 | 1920 - 2048 | 10 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1080 - 1536，10 个样本，取值集中（一致性 91%）
- 高度 中位数 2048，观测区间 1920 - 2048，10 个样本，取值集中（一致性 98%）
