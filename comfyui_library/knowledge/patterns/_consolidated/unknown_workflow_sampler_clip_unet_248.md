---
name: unknown_workflow_sampler_clip_unet_248
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9076
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2klein去除主体_2103376169314906113.json, 图片生成/图生图/flux2klein去除卡片_2103408490587967490.json, 图片生成/图生图/flux2klein去除文字_2103396557008752641.json, 图片生成/图生图/flux2klein添加主体_2103385812510535682.json, 图片生成/图生图/仅更改尺寸，图案不变_2059163011654438913.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_248

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux2klein去除主体_2103376169314906113.json、图片生成/图生图/flux2klein去除卡片_2103408490587967490.json、图片生成/图生图/flux2klein去除文字_2103396557008752641.json、图片生成/图生图/flux2klein添加主体_2103385812510535682.json、图片生成/图生图/仅更改尺寸，图案不变_2059163011654438913.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
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
- `Anything Everywhere3` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ImageToMask` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `PixaromaInpaintCrop` —— 2/5 个有
- `PixaromaUncrop` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageResize+` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
