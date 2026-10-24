---
name: unknown_workflow_sampler_clip_unet_61
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.943
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_omnigen2_image_edit.json, 图片生成/图生图/AI脑洞狮--Flux-Klein图像编辑，实现人物换装、换场景、扩图等应用_2031388345238032386.json, 图片生成/图生图/Ai产品精修渲染放大V4.1_2043861761803165698.json, 图片生成/图生图/Ai产品精修渲染放大V4.1_2097148886946238466.json, 图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json, 图片生成/图生图/CG风格转绘极简工作流_2022333968351236098.json, 图片生成/图生图/F.2Klein9b产品渲染精修_2058016361133207554.json, 图片生成/图生图/FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778.json, 图片生成/图生图/Flux2 Klein-单图编辑：一致性保持_2014169468368330753.json, 图片生成/图生图/Flux2-Klein9b 万能提取服装 服装3D展示 精修褶皱_2032609919714725889.json, 图片生成/图生图/Flux2-Klein9b一键产品加背景 白底产品换背景换场景_2033110402749435906.json, 图片生成/图生图/万物迁移工作流_2036348251548426241.json, 图片生成/文生图/Flux2 Klein｜图像编辑（角色一致性，保留角色全身特征）+防色彩偏移_2046845762285346817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_61

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（comfyui-workflow-templates-json/image_omnigen2_image_edit.json、图片生成/图生图/AI脑洞狮--Flux-Klein图像编辑，实现人物换装、换场景、扩图等应用_2031388345238032386.json、图片生成/图生图/Ai产品精修渲染放大V4.1_2043861761803165698.json、图片生成/图生图/Ai产品精修渲染放大V4.1_2097148886946238466.json、图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `CFGGuider` —— 12/13 个有
- `EmptyFlux2LatentImage` —— 12/13 个有
- `Flux2Scheduler` —— 12/13 个有
- `GetImageSize` —— 12/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `ImageScaleToTotalPixels` —— 9/13 个有
- `Image Comparer (rgthree)` —— 7/13 个有
- `LoraLoaderModelOnly` —— 7/13 个有
- `ConstrainImage|pysssss` —— 4/13 个有
- `CR Prompt List` —— 2/13 个有
- `ColorMatch` —— 2/13 个有
- `Flux2KleinRefLatentController` —— 2/13 个有
- `Flux2KleinTextRefBalance` —— 2/13 个有
- `BasicScheduler` —— 1/13 个有
- `DualCFGGuider` —— 1/13 个有
- `EmptySD3LatentImage` —— 1/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `Flux2KleinColorAnchor` —— 1/13 个有
- `GetImageSize+` —— 1/13 个有
- `easy imageSize` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
