---
name: unknown_workflow_sampler_clip_unet_276
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8942
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux3 Klein 提示词增强文生图_2112106153021890562.json, 图片生成/文生图/Flux3 Klein 提示词增强文生图_2113652586107727873.json, 图片生成/文生图/Flux3&多图编辑-加速版_2111293209782603777.json, 图片生成/文生图/flux_klien3单图-快速图像编辑_2110999906369490946.json, 视频生成/图生视频/Flux3加速版多图编辑V1_2110847111846780929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_276

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux3 Klein 提示词增强文生图_2112106153021890562.json、图片生成/文生图/Flux3 Klein 提示词增强文生图_2113652586107727873.json、图片生成/文生图/Flux3&多图编辑-加速版_2111293209782603777.json、图片生成/文生图/flux_klien3单图-快速图像编辑_2110999906369490946.json、视频生成/图生视频/Flux3加速版多图编辑V1_2110847111846780929.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoadImage` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `ReferenceMultiLatent` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `TextGenerate` —— 2/5 个有
- `GetImageSize` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
