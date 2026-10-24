---
name: unknown_workflow_sampler_clip_unet_97
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9556
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX3 PE提示词强化加速版图像编辑_2111364166001971202.json, 图片生成/图生图/FLUX3+PE提示词强化加速版图像编辑_2111477045355180034.json, 图片生成/图生图/FLUX3加速版图像编辑_2110845040582025217.json, 图片生成/图生图/FLUX3加速版图像编辑_2111037244042727426.json, 图片生成/图生图/Flux3 PE提示词强化加速版多图编辑V1_2111364159416922114.json, 图片生成/图生图/单图编辑-FLUX3-Klein-int8加速版_2110936341600104450.json, 图片生成/图生图/单图编辑-FLUX3-Klein-int8加速版pe提示词优化版_2111502270784434177.json, 图片生成/图生图/多图编辑Flux3 PE提示词强化加速版_2111482509593763842.json, 图片生成/文生图/FLUX3 PE提示词强化加速版文生图v1_2111364151871365122.json, 图片生成/文生图/FLUX3+PE提示词强化加速版文生图_2111485679510319106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX3 PE提示词强化加速版图像编辑_2111364166001971202.json、图片生成/图生图/FLUX3+PE提示词强化加速版图像编辑_2111477045355180034.json、图片生成/图生图/FLUX3加速版图像编辑_2110845040582025217.json、图片生成/图生图/FLUX3加速版图像编辑_2111037244042727426.json、图片生成/图生图/Flux3 PE提示词强化加速版多图编辑V1_2111364159416922114.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：96%

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
- `Flux3PELoader` —— 7/10 个有
- `Flux3PromptEnhance` —— 7/10 个有
- `GetLatentSize` —— 7/10 个有
- `CR Prompt Text` —— 6/10 个有
- `PDIMAGE_LongerSize` —— 6/10 个有
- `ReferenceLatent` —— 6/10 个有
- `VAEEncode` —— 6/10 个有
- `孤海注释` —— 3/10 个有
- `ImageConcanate` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `ReferenceMultiLatent` —— 2/10 个有
- `Text` —— 2/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
