---
name: unknown_workflow_sampler_clip_unet_69
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.897917
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux 2-klein9b换脸换装组合_2064976052706963458.json, 图片生成/图生图/Flux2  Klein图像单图编辑9B版官方版_2012125328356941826.json, 图片生成/图生图/Flux2 Klein 一键转3D纸雕_2025543049413136385.json, 图片生成/图生图/Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026.json, 图片生成/图生图/Flux2 Klein 三图编辑9B版_2012176832983998465.json, 图片生成/图生图/Flux2 Klein 动漫转写实_2024871399084527618.json, 图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json, 图片生成/图生图/flux-2-klein换脸换装组合_2063802064890843138.json, 图片生成/图生图/产品智能场景摆放_Flux2 Klein_2014540954375561218.json, 图片生成/图生图/手部修复 修手换头换脸换装+ 最新完美修手+重绘修手-完美修手+自然真实+多图编辑加速版_2056901858727391234.json, 图片生成/图生图/换脸Flux2Klein全能编辑20版人物一致自然真实多图编辑加速版_2062017636703227905.json, 图片生成/图生图/换脸换装 人物一致+自然真实全能编辑2.0版_2078751895195312130.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux 2-klein9b换脸换装组合_2064976052706963458.json、图片生成/图生图/Flux2  Klein图像单图编辑9B版官方版_2012125328356941826.json、图片生成/图生图/Flux2 Klein 一键转3D纸雕_2025543049413136385.json、图片生成/图生图/Flux2 Klein 万物增强细节LoRA 林耀2.9_2020708657654145026.json、图片生成/图生图/Flux2 Klein 三图编辑9B版_2012176832983998465.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
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
- `CR Text` —— 8/12 个有
- `Image Comparer (rgthree)` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 7/12 个有
- `GetImageSize` —— 7/12 个有
- `MuyeTextEditOutput` —— 7/12 个有
- `EmptyFlux2LatentImage` —— 6/12 个有
- `ImageConcanate` —— 5/12 个有
- `JWFloat` —— 5/12 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 5/12 个有
- `RH_Nano_Banana2_Image2Image` —— 5/12 个有
- `ImageScaleBy` —— 3/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `GetNode` —— 2/12 个有
- `SeedVR2LoadDiTModel` —— 2/12 个有
- `SeedVR2LoadVAEModel` —— 2/12 个有
- `SeedVR2VideoUpscaler` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `RH_Translator` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
