---
name: unknown_workflow_sampler_clip_unet_311
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.807
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Comfy挑战赛7（不可能的菜肴）-SRPO自动创意文生图V1（四图）_1974009583997947905.json, 图片生成/文生图/Flux1-TeaCache加速工作流_1929847965068988417.json, 图片生成/文生图/Flux_Dev文生图官方工作流_1930161942738976770.json, 图片生成/文生图/（生图篇）MagCache新王登基_1933213412669173762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_311

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Comfy挑战赛7（不可能的菜肴）-SRPO自动创意文生图V1（四图）_1974009583997947905.json、图片生成/文生图/Flux1-TeaCache加速工作流_1929847965068988417.json、图片生成/文生图/Flux_Dev文生图官方工作流_1930161942738976770.json、图片生成/文生图/（生图篇）MagCache新王登基_1933213412669173762.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `GoogleTranslator` —— 1/4 个有
- `MagCache` —— 1/4 个有
- `Note _O` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
