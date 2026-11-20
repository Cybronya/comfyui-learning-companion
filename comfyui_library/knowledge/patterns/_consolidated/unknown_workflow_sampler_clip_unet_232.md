---
name: unknown_workflow_sampler_clip_unet_232
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8125
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Klein-t2i_2073767273445289985.json, 图片生成/文生图/Klein4B文生图(又快又好)_2036253514183221249.json, 图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json, 图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json, 图片生成/文生图/flux2.klein官方文生图工作流_2042509850478907393.json, 视频生成/文生视频/flux klein4B 工作流 浮云1.17_2012350472430034946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_232

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Klein-t2i_2073767273445289985.json、图片生成/文生图/Klein4B文生图(又快又好)_2036253514183221249.json、图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json、图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json、图片生成/文生图/flux2.klein官方文生图工作流_2042509850478907393.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 5/6 个有
- `AddLabel` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `easy ifElse` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
