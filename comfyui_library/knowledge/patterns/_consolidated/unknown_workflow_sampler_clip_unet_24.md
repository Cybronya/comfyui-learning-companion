---
name: unknown_workflow_sampler_clip_unet_24
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.77312
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram 4 自审查生图_2062902826669535233.json, 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2065735487565946881.json, 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085242360778280962.json, 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714.json, 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2087796460128661505.json, 图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2087800722841759746.json, 图片生成/文生图/Ideogram 4_2064161496220917762.json, 图片生成/文生图/Ideogram 开源支持语言简洁文生图_2064255815862800385.json, 图片生成/文生图/Ideogram 强势开源_支持自然语言极简输入_2062741988264468482.json, 图片生成/文生图/Ideogram 强势开源_支持自然语言极简输入_2063812523903770625.json, 图片生成/文生图/Ideogram 强势开源_支持自然语言极简输入_2063818019272486913.json, 图片生成/文生图/Ideogram 强势开源_支持自然语言极简输入_2080566085367197698.json, 图片生成/文生图/Ideogram 强势开源_支持自然语言极简输入_2080569000928571394.json, 图片生成/文生图/Ideogram 强势开源文生图支持自然语言极简输入_2063901268447416321.json, 图片生成/文生图/Ideogram+Qwen35支持语言简洁文生图_2076442947637309441.json, 图片生成/文生图/Ideogram+_AI 版专业排版软件_的文生图方案_2067596044078247938.json, 图片生成/文生图/Ideogram4 精准定位文生图（平面设计_海报设计_角色场景设计）_2063567041306652673.json, 图片生成/文生图/Ideogram4-文生图_2063913322784841730.json, 图片生成/文生图/Ideogram4-美学大师-自动提示词-文生图-MJ风格_2063245808631377922.json, 图片生成/文生图/Ideogram4全自动文生图_2063089442067410946.json, 图片生成/文生图/Ideogram4全自动文生图_2063247772672937985.json, 图片生成/文生图/MJ最佳平替Ideogram4美学大师全自动文生图工作流 V1.0_2063172563454488577.json, 图片生成/文生图/【MJ最佳替代品】Ideogram4美学大师全自动文生图_2062820590976847873.json, 图片生成/文生图/【MJ最佳替代品】Ideogram4美学大师全自动文生图_2063183559854223361.json, 图片生成/文生图/心然·寻源-Ideogram4文生图（对标MJ）_2091164270091399170.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/Ideogram 4 自审查生图_2062902826669535233.json、图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2065735487565946881.json、图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085242360778280962.json、图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2085249483184627714.json、图片生成/文生图/Ideogram 4+Prompt Builder 中文提示词自动文生图_2087796460128661505.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 24/25 个有
- `PrimitiveStringMultiline` —— 24/25 个有
- `CustomCombo` —— 20/25 个有
- `ComfyMathExpression` —— 16/25 个有
- `llama_cpp_instruct_adv` —— 16/25 个有
- `llama_cpp_model_loader` —— 16/25 个有
- `llama_cpp_parameters` —— 16/25 个有
- `ResolutionSelector` —— 15/25 个有
- `JjkText` —— 10/25 个有
- `easy cleanGpuUsed` —— 8/25 个有
- `INTConstant` —— 7/25 个有
- `Image Comparer (rgthree)` —— 7/25 个有
- `ImageScaleToTotalPixels` —— 7/25 个有
- `PreviewImage` —— 7/25 个有
- `SeedVR2LoadDiTModel` —— 7/25 个有
- `SeedVR2LoadVAEModel` —— 7/25 个有
- `SeedVR2VideoUpscaler` —— 7/25 个有
- `easy saveText` —— 7/25 个有
- `RHLLMChatNode` —— 6/25 个有
- `easy showAnything` —— 6/25 个有
- `Fast Groups Bypasser (rgthree)` —— 2/25 个有
- `Ideogram4PromptBuilderKJ` —— 2/25 个有
- `ShowText|pysssss` —— 2/25 个有
- `DeepTranslatorTextNode` —— 1/25 个有
- `LoadImage` —— 1/25 个有
- `StringConcatenate` —— 1/25 个有
- `TextGenerate` —— 1/25 个有
- `UnloadAllModels` —— 1/25 个有
- `孤海注释` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
