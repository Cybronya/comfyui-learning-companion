---
name: unknown_workflow_sampler_clip_unet_167
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.862
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ideogram4_2083390180580483074.json, 图片生成/文生图/ideogram4_光学眼镜模特(+提示词优化+KJ)_2072942885963657217.json, 图片生成/文生图/ideogram4摇卡_光学眼镜模特(+提示词优化)_2072938272011153409.json, 图片生成/文生图/设计师专用模型Ideogram4美学大师文生图_2064893847733362689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/ideogram4_2083390180580483074.json、图片生成/文生图/ideogram4_光学眼镜模特(+提示词优化+KJ)_2072942885963657217.json、图片生成/文生图/ideogram4摇卡_光学眼镜模特(+提示词优化)_2072938272011153409.json、图片生成/文生图/设计师专用模型Ideogram4美学大师文生图_2064893847733362689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CustomCombo` —— 3/4 个有
- `AspectRatio` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewTextNode` —— 2/4 个有
- `RHLLMChatNode` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `Ideogram4PromptBuilderKJ` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
