---
name: unknown_workflow_sampler_clip_unet_166
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.72675
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualModelGuider, Ideogram4Scheduler, KSamplerSelect, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4（无审查版）_2071111233360715777.json, 图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2094723434193448962.json, 图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2098917767268360194.json, 图片生成/文生图/Ideogram强势开源支持自然语言极简输入_2064195567823183874.json, 图片生成/文生图/Ideogram自然语文生图_2064911052713844737.json, 图片生成/文生图/[Ideogram 4 系列 01] Ideogram 4 第一课：官方 ComfyUI 工作流解析_2084558233645174785.json, 图片生成/文生图/[Ideogram 4 系列 02] Prompt Builder 解析_2084481304804024321.json, 图片生成/文生图/ideogram4_t2i文生图_2064543465328963586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_166

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Ideogram4（无审查版）_2071111233360715777.json、图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2094723434193448962.json、图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2098917767268360194.json、图片生成/文生图/Ideogram强势开源支持自然语言极简输入_2064195567823183874.json、图片生成/文生图/Ideogram自然语文生图_2064911052713844737.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualModelGuider`
- `Ideogram4Scheduler`
- `KSamplerSelect`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 7/8 个有
- `CustomCombo` —— 7/8 个有
- `JsonExtractString` —— 7/8 个有
- `StringReplace` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 6/8 个有
- `PrimitiveInt` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `ComfyMathExpression` —— 5/8 个有
- `PreviewAny` —— 5/8 个有
- `PreviewImage` —— 3/8 个有
- `llama_cpp_instruct_adv` —— 3/8 个有
- `llama_cpp_model_loader` —— 3/8 个有
- `llama_cpp_parameters` —— 3/8 个有
- `EmptyLatentImage` —— 2/8 个有
- `GetNode` —— 2/8 个有
- `Ideogram4PromptBuilderKJ` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `easy promptLine` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `InversionDemoLazySwitch` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `SimpleToggleNode` —— 1/8 个有
- `StringSplitSelect` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
