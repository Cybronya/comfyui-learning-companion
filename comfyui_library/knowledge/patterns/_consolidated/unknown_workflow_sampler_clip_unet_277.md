---
name: unknown_workflow_sampler_clip_unet_277
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9404
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kontext 单图编辑火柴人_1970786088950374402.json, 图片生成/文生图/flux-海报_1914942831851466753.json, 图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json, 图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json, 图片生成/文生图/最新MagCache加速-Flux文生图_1933315314153365506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_277

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Kontext 单图编辑火柴人_1970786088950374402.json、图片生成/文生图/flux-海报_1914942831851466753.json、图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json、图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json、图片生成/文生图/最新MagCache加速-Flux文生图_1933315314153365506.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 4/5 个有
- `ModelSamplingFlux` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `RH_Translator` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `MagCache` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有
- `TextInputNode` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
