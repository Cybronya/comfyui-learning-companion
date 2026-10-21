---
name: unknown_workflow_sampler_clip_unet_64
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.904778
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json, 图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json, 图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json, 图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json, 图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json, 图片生成/文生图/Flux.2+LoRA文生图_1995120190486667265.json, 图片生成/文生图/Flux.2-支持中文-文生图_1993529170808471553.json, 图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json, 图片生成/文生图/Flux2 单图编辑_1993603003697610753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json、图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json、图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json、图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json、图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `ReferenceLatent` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `CompressImages` —— 4/9 个有
- `Int Literal` —— 3/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `Int` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `SetNode` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
