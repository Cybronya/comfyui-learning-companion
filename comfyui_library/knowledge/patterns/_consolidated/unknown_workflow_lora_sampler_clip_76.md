---
name: unknown_workflow_lora_sampler_clip_76
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.891125
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, FluxGuidance, JjkText, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Prompter, RH_Translator, RandomNoise, SamplerCustomAdvanced, TextCombinerTwo, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/极速文生图_1983350145905532929.json, 图片生成/文生图/极速文生图_1983456421763325954.json, 图片生成/文生图/极速文生图（测试）_1957340539244965890.json, 平台全量/服装设计1-文生手绘彩稿_1909863851737972737.json, 平台全量/服装设计10-文生男装模特_1912093849634963458.json, 平台全量/服装设计5-真实服装模特生成_1910158176543567873.json, 平台全量/服装设计6-文生面料_1910236838714404865.json, 平台全量/服装设计9-文生服装单品_1910619124739862529.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/极速文生图_1983350145905532929.json、图片生成/文生图/极速文生图_1983456421763325954.json、图片生成/文生图/极速文生图（测试）_1957340539244965890.json、平台全量/服装设计1-文生手绘彩稿_1909863851737972737.json、平台全量/服装设计10-文生男装模特_1912093849634963458.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxGuidance`
- `JjkText`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RH_Prompter`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextCombinerTwo`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 5/8 个有
- `FluxResolutionNode` —— 5/8 个有
- `ImageUpscaleWithModel` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `UpscaleModelLoader` —— 5/8 个有
- `Int` —— 4/8 个有
- `ImageScaleBy` —— 3/8 个有
- `ImpactSwitch` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `SaveImagePlus` —— 3/8 个有
- `LoadImage` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy textSwitch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 8 | 100% |
| 高度 | 512 | 512 - 512 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，8 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，8 个样本，取值集中（一致性 100%）
