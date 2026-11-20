---
name: unknown_workflow_sampler_clip_unet_112
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9508
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux3 PE提示词强化加速版多图编辑V1_2111364159416922114.json, 图片生成/图生图/Flux3加速版多图编辑V1_2114191708626964481.json, 图片生成/图生图/Flux3加速版多图编辑_2111040326122164225.json, 图片生成/图生图/Flux3加速版多图编辑_2111060681888976898.json, 图片生成/图生图/Flux3图像编辑_2111273434834624514.json, 图片生成/图生图/Flux3图像编辑_2114630236741656578.json, 图片生成/图生图/多图编辑Flux3 PE提示词强化加速版_2111482509593763842.json, 图片生成/文生图/FLUX3 PE提示词强化加速版文生图v1_2111364151871365122.json, 图片生成/文生图/FLUX3+PE提示词强化加速版文生图_2111485679510319106.json, 图片生成/文生图/Flux3+PE提示词强化加速版多图编辑_2111485757222383618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_112

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux3 PE提示词强化加速版多图编辑V1_2111364159416922114.json、图片生成/图生图/Flux3加速版多图编辑V1_2114191708626964481.json、图片生成/图生图/Flux3加速版多图编辑_2111040326122164225.json、图片生成/图生图/Flux3加速版多图编辑_2111060681888976898.json、图片生成/图生图/Flux3图像编辑_2111273434834624514.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/10 个有
- `ReferenceMultiLatent` —— 8/10 个有
- `CR Prompt Text` —— 7/10 个有
- `Flux3PELoader` —— 5/10 个有
- `Flux3PromptEnhance` —— 5/10 个有
- `GetLatentSize` —— 5/10 个有
- `PrimitiveInt` —— 2/10 个有
- `QwenPERewriteT8` —— 2/10 个有
- `ResolutionSelector` —— 2/10 个有
- `PreviewImage` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
