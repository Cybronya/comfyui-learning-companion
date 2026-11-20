---
name: unknown_workflow_sampler_clip_unet_442
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9065
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, ImageConcanate, KSamplerSelect, LoadImage, ManualSigmas, PDIMAGE_LongerSize, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/单图编辑-FLUX3-Klein-int8加速版_2110936341600104450.json, 图片生成/图生图/单图编辑-FLUX3-Klein-int8加速版pe提示词优化版_2111502270784434177.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_442

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/单图编辑-FLUX3-Klein-int8加速版_2110936341600104450.json、图片生成/图生图/单图编辑-FLUX3-Klein-int8加速版pe提示词优化版_2111502270784434177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `ImageConcanate`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `PDIMAGE_LongerSize`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Flux3PELoader` —— 1/2 个有
- `Flux3PromptEnhance` —— 1/2 个有
- `GetLatentSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
