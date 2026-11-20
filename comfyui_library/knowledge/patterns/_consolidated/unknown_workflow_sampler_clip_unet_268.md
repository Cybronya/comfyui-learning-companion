---
name: unknown_workflow_sampler_clip_unet_268
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9624
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/低精图洗图+服装替换_2085353987464847361.json, 图片生成/图生图/图案转刺绣风格_2043579107664994306.json, 图片生成/图生图/多图编辑组合_2078268396902379521.json, 图片生成/图生图/服装替换_2083162795322994690.json, 图片生成/文生图/Flux2 Klein 多图编辑&文生图 自由控制 平替全能图片 4B 极速 & 9B 质量_2012361850310107138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_268

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/低精图洗图+服装替换_2085353987464847361.json、图片生成/图生图/图案转刺绣风格_2043579107664994306.json、图片生成/图生图/多图编辑组合_2078268396902379521.json、图片生成/图生图/服装替换_2083162795322994690.json、图片生成/文生图/Flux2 Klein 多图编辑&文生图 自由控制 平替全能图片 4B 极速 & 9B 质量_2012361850310107138.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `AspectRatio` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `Qwen3VL_Chat` —— 1/5 个有
- `Seed_` —— 1/5 个有
- `ttN text` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
