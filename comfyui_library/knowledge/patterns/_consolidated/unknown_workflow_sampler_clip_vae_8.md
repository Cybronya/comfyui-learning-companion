---
name: unknown_workflow_sampler_clip_vae_8
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.817786
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxResolutionNode, ImageResize+, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 开源模型+ Nunchaku FLUX 加速工作流_1939912219494621186.json, 图片生成/图生图/Kontext+双图-万能改图_z_2014654807981694978.json, 图片生成/图生图/Kontext-一键换姿势（人物保真）_1951246872604274689.json, 图片生成/图生图/kontext Dev 模特产品替换_1938883953208315906.json, 图片生成/图生图/【IP形象一致性】Nun-Kontext-Dev（人物篇）_1941401692749643778.json, 图片生成/图生图/【万物合影】Nun-Kontext-Dev_1942272809550942209.json, 图片生成/图生图/【产品一致性】Nun-Kontext-Dev（静物篇）_1942155136640905218.json, 图片生成/图生图/【单图编辑】Flux-Kontext-Dev（基础流）_1938510905971769345.json, 图片生成/图生图/【图像去水印】Flux-Kontext-Dev_1943231517701128194.json, 图片生成/图生图/【灵魂画手风格】Nun-Kontext-Dev（加速版）_1939972321711157249.json, 图片生成/图生图/【超全风格转绘】Nun-Kontext-Dev（加更）_1940331067989753857.json, 图片生成/图生图/一键去水印工作流_1948188735107137537.json, 图片生成/图生图/照相馆专用-老照片高清修复上色工作流_1948187584666185729.json, 图片生成/文生图/【灵魂画手风格】抖音火爆视频专用（加速版）_2024382098097836034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Kontext 开源模型+ Nunchaku FLUX 加速工作流_1939912219494621186.json、图片生成/图生图/Kontext+双图-万能改图_z_2014654807981694978.json、图片生成/图生图/Kontext-一键换姿势（人物保真）_1951246872604274689.json、图片生成/图生图/kontext Dev 模特产品替换_1938883953208315906.json、图片生成/图生图/【IP形象一致性】Nun-Kontext-Dev（人物篇）_1941401692749643778.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxResolutionNode`
- `ImageResize+`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 13/14 个有
- `MathExpression|pysssss` —— 12/14 个有
- `PreviewImage` —— 12/14 个有
- `Anything Everywhere` —— 11/14 个有
- `CM_IntToBool` —— 11/14 个有
- `CR Text` —— 11/14 个有
- `ImpactConditionalBranch` —— 11/14 个有
- `Int` —— 11/14 个有
- `easy cleanGpuUsed` —— 11/14 个有
- `Image Comparer (rgthree)` —— 10/14 个有
- `NunchakuFluxDiTLoader` —— 10/14 个有
- `RH_Translator` —— 10/14 个有
- `easy showAnything` —— 10/14 个有
- `RHHiddenNodes` —— 6/14 个有
- `UNETLoader` —— 4/14 个有
- `CR Text Concatenate` —— 2/14 个有
- `ImageConcanate` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `RMBG` —— 2/14 个有
- `ShowText|pysssss` —— 2/14 个有
- `ttN concat` —— 2/14 个有
- `FluxKontextImageScale` —— 1/14 个有
- `GetNode` —— 1/14 个有
- `ImageStitch` —— 1/14 个有
- `ImpactSwitch` —— 1/14 个有
- `SetNode` —— 1/14 个有
- `easy imageRemBg` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 14 | 66% |
| 高度 | 512 | 512 - 1280 | 14 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，14 个样本
- 高度 中位数 512，观测区间 512 - 1280，14 个样本
