---
name: unknown_workflow_sampler_clip_unet_87
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.945091
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_omnigen2_image_edit.json, 图片生成/图生图/AI脑洞狮--Flux-Klein图像编辑，实现人物换装、换场景、扩图等应用_2031388345238032386.json, 图片生成/图生图/Ai产品精修渲染放大V4.1_2043861761803165698.json, 图片生成/图生图/Ai产品精修渲染放大V4.1_2097148886946238466.json, 图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json, 图片生成/图生图/CG风格转绘极简工作流_2022333968351236098.json, 图片生成/图生图/F.2Klein9b产品渲染精修_2058016361133207554.json, 图片生成/图生图/FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778.json, 图片生成/图生图/Flux2 Klein-单图编辑：一致性保持_2014169468368330753.json, 图片生成/图生图/Flux2-Klein9b 万能提取服装 服装3D展示 精修褶皱_2032609919714725889.json, 图片生成/图生图/klein高一致性高清修复_2030545132830859266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（comfyui-workflow-templates-json/image_omnigen2_image_edit.json、图片生成/图生图/AI脑洞狮--Flux-Klein图像编辑，实现人物换装、换场景、扩图等应用_2031388345238032386.json、图片生成/图生图/Ai产品精修渲染放大V4.1_2043861761803165698.json、图片生成/图生图/Ai产品精修渲染放大V4.1_2097148886946238466.json、图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
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
- `CFGGuider` —— 10/11 个有
- `EmptyFlux2LatentImage` —— 10/11 个有
- `Flux2Scheduler` —— 10/11 个有
- `GetImageSize` —— 10/11 个有
- `ConditioningZeroOut` —— 9/11 个有
- `Image Comparer (rgthree)` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `ConstrainImage|pysssss` —— 4/11 个有
- `CR Prompt List` —— 2/11 个有
- `ColorMatch` —— 2/11 个有
- `BasicScheduler` —— 1/11 个有
- `DualCFGGuider` —— 1/11 个有
- `EmptySD3LatentImage` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `Flux2KleinRefLatentController` —— 1/11 个有
- `Flux2KleinTextRefBalance` —— 1/11 个有
- `GetImageSize+` —— 1/11 个有
- `ImageSharpen` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
