---
name: unknown_workflow_sampler_clip_unet_206
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.798571
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ideogram4_2083390180580483074.json, 图片生成/文生图/ideogram4_光学眼镜模特(+提示词优化+KJ)_2072942885963657217.json, 图片生成/文生图/ideogram4摇卡_光学眼镜模特(+提示词优化)_2072938272011153409.json, 图片生成/文生图/设计师专用模型Ideogram4美学大师文生图_2064893847733362689.json, 图片生成/文生图/（贞贞-图图版）Ideogram4智能JSON格式简易版文生图（可选质量模式）V2_2067794610629472257.json, 图片生成/文生图/（贞贞版-新训练23500）Ideogram4智能JSON格式简易版文生图（可选质量模式）V2_2068037566401703938.json, 图片生成/文生图/（贞贞版）Ideogram4智能JSON格式简易版文生图（可选质量模式）V2_2067263113581391873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_206

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/ideogram4_2083390180580483074.json、图片生成/文生图/ideogram4_光学眼镜模特(+提示词优化+KJ)_2072942885963657217.json、图片生成/文生图/ideogram4摇卡_光学眼镜模特(+提示词优化)_2072938272011153409.json、图片生成/文生图/设计师专用模型Ideogram4美学大师文生图_2064893847733362689.json、图片生成/文生图/（贞贞-图图版）Ideogram4智能JSON格式简易版文生图（可选质量模式）V2_2067794610629472257.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `Ideogram4PromptBuilderKJ` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `RH_LLMAPI_Pro_Node` —— 4/7 个有
- `easy anythingIndexSwitch` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `CustomCombo` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `AspectRatio` —— 2/7 个有
- `CR Text` —— 2/7 个有
- `PreviewTextNode` —— 2/7 个有
- `RHLLMChatNode` —— 2/7 个有
- `GetNode` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
