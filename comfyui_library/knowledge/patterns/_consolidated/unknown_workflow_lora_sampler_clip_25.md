---
name: unknown_workflow_lora_sampler_clip_25
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.652071
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/矢量风格插画Flux+矢量Lora生图_1932014239752323074.json, 图片生成/文生图/简易贴纸制作工作流_1913052188661481473.json, 平台全量/10S生成室内设计图_1893206230348017666.json, 平台全量/Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050.json, 平台全量/Film Storyboard-电影故事板【Context LoRA】_1856225714939760641.json, 平台全量/Font Design-字体设计【Context LoRA】_1856277609574174722.json, 平台全量/Home Decoration-家居装饰【Context LoRA】_1856281624013836289.json, 平台全量/Portrait Illustration-肖像插图【Context LoRA】_1856600733977366529.json, 平台全量/Portrait Photography-人像摄影【Context LoRA】_1856534151095848961.json, 平台全量/Runninghub Oneshot Prompter_1872524884764192770.json, 平台全量/Sandstorm Visual Effect-沙尘暴视觉效果【Context LoRA】_1856603877087891458.json, 平台全量/Sparklers Visual Effect-烟花视觉效果【Context LoRA】_1856569778264477698.json, 平台全量/Visual Identity Design-视觉识别设计【Context LoRA】_1856562720681103362.json, 平台全量/ppt-templates【Context LoRA】_1856547498772074498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/矢量风格插画Flux+矢量Lora生图_1932014239752323074.json、图片生成/文生图/简易贴纸制作工作流_1913052188661481473.json、平台全量/10S生成室内设计图_1893206230348017666.json、平台全量/Couple Profile Design-双角色设计【Context LoRA】_1856611294731522050.json、平台全量/Film Storyboard-电影故事板【Context LoRA】_1856225714939760641.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 13/14 个有
- `FluxGuidance` —— 13/14 个有
- `JjkText` —— 13/14 个有
- `ShowText|pysssss` —— 12/14 个有
- `TextCombinerTwo` —— 12/14 个有
- `Label (rgthree)` —— 11/14 个有
- `ModelSamplingFlux` —— 11/14 个有
- `PreviewImage` —— 11/14 个有
- `TextCombinerSix` —— 11/14 个有
- `RH_Prompter` —— 5/14 个有
- `FluxResolutionNode` —— 2/14 个有
- `BlurFusionForegroundEstimation` —— 1/14 个有
- `EmptyLatentImage` —— 1/14 个有
- `GetMaskByBiRefNet` —— 1/14 个有
- `LoadRembgByBiRefNetModel` —— 1/14 个有
- `PatchModelAddDownscale` —— 1/14 个有
- `RH_OneShot_Prompter` —— 1/14 个有
- `RembgByBiRefNet` —— 1/14 个有
- `StringFunction|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.65 - 1 | 14 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.65 - 1，14 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
