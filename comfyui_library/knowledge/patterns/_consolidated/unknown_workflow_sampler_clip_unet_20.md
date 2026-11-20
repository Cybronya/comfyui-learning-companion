---
name: unknown_workflow_sampler_clip_unet_20
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.792308
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, KSamplerSelect, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4动漫文生图_2071282232492388353.json, 图片生成/文生图/Ideogram4文生图工作流_2085587398561456129.json, 图片生成/文生图/Ideogram4文生图自然语言LLM生成官方提示词版_2073724732792459266.json, 图片生成/文生图/Ideogram4极限写实版文生图V1_2070484938503319553.json, 图片生成/文生图/Ideogram4极限写实版文生图V1_2072129329676513281.json, 图片生成/文生图/Ideogram4极限写实版文生图_2070485307811782657.json, 图片生成/文生图/Ideogram4美学设计全自动文生图_2063531342176014337.json, 图片生成/文生图/Ideogram4（平替MJ）文生图美学大师_2067620647542542337.json, 图片生成/文生图/ideogram4_2063180809263206402.json, 图片生成/文生图/ideogram4工作流_2062533863087362049.json, 图片生成/文生图/ideogram4工作流_2062836963702562817.json, 图片生成/文生图/ideogram4工作流带提示词_2063538368042070017.json, 图片生成/文生图/ideogram4工作流带提示词_2063769707022479362.json, 图片生成/文生图/ideogram4工作流带提示词_2063772030377480194.json, 图片生成/文生图/ideogram4工作流带提示词_2063804440662073345.json, 图片生成/文生图/ideogram4工作流带提示词_2063810498231095297.json, 图片生成/文生图/ideogram4工作流带提示词_2063812502248583169.json, 图片生成/文生图/ideogram4工作流带提示词_2063813597683343362.json, 图片生成/文生图/ideogram4工作流带提示词_2063815460910616578.json, 图片生成/文生图/ideogram4工作流带提示词_2063816739921686529.json, 图片生成/文生图/ideogram4工作流带提示词_2063817989841047554.json, 图片生成/文生图/ideogram4工作流带提示词_2064174515973869569.json, 图片生成/文生图/ideogram4工作流带提示词_2064177318440034306.json, 图片生成/文生图/ideogram4工作流文生图工作流_2062820277763010562.json, 图片生成/文生图/ideogram4工作流文生图工作流_2062872647050022914.json, 图片生成/文生图/ldeogram4-文生图(极限写实版)_2070776801890234370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_20

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/Ideogram4动漫文生图_2071282232492388353.json、图片生成/文生图/Ideogram4文生图工作流_2085587398561456129.json、图片生成/文生图/Ideogram4文生图自然语言LLM生成官方提示词版_2073724732792459266.json、图片生成/文生图/Ideogram4极限写实版文生图V1_2070484938503319553.json、图片生成/文生图/Ideogram4极限写实版文生图V1_2072129329676513281.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 26 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 25/26 个有
- `StringReplace` —— 24/26 个有
- `PreviewAny` —— 23/26 个有
- `ComfyNumberConvert` —— 21/26 个有
- `JsonExtractString` —— 21/26 个有
- `CustomCombo` —— 20/26 个有
- `TextGenerate` —— 18/26 个有
- `StringConcatenate` —— 16/26 个有
- `Fast Groups Muter (rgthree)` —— 14/26 个有
- `LoraLoaderModelOnly` —— 5/26 个有
- `ModelSamplingAuraFlow` —— 5/26 个有
- `CR Prompt Text` —— 4/26 个有
- `Ideogram4PromptBuilderKJ` —— 4/26 个有
- `easy showAnything` —— 4/26 个有
- `RH_LLMAPI_Pro_Node` —— 3/26 个有
- `DuckHideNode` —— 2/26 个有
- `PreviewImage` —— 2/26 个有
- `RHLLMChatNode` —— 2/26 个有
- `easy imageChooser` —— 2/26 个有
- `ComfySwitchNode` —— 1/26 个有
- `Fast Groups Bypasser (rgthree)` —— 1/26 个有
- `LoadImage` —— 1/26 个有
- `PrimitiveBoolean` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
