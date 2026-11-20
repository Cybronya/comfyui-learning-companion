---
name: unknown_workflow_sampler_clip_unet_158
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.940111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2klein去除主体_2103376169314906113.json, 图片生成/图生图/flux2klein去除卡片_2103408490587967490.json, 图片生成/图生图/flux2klein去除文字_2103396557008752641.json, 图片生成/图生图/flux2klein添加主体_2103385812510535682.json, 图片生成/图生图/一键人像转3D建模_2031914265522737154.json, 图片生成/图生图/一键去万物工作流Seg3+Klein_2031956746331230209.json, 图片生成/图生图/交换角色位置_2042497890186170370.json, 图片生成/图生图/仅更改尺寸，图案不变_2059163011654438913.json, 图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/flux2klein去除主体_2103376169314906113.json、图片生成/图生图/flux2klein去除卡片_2103408490587967490.json、图片生成/图生图/flux2klein去除文字_2103396557008752641.json、图片生成/图生图/flux2klein添加主体_2103385812510535682.json、图片生成/图生图/一键人像转3D建模_2031914265522737154.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `BasicGuider` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `FluxGuidance` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `Anything Everywhere3` —— 4/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `ImageToMask` —— 2/9 个有
- `PixaromaInpaintCrop` —— 2/9 个有
- `PixaromaUncrop` —— 2/9 个有
- `VRAMReserver` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `CFGGuider` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageResize+` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
