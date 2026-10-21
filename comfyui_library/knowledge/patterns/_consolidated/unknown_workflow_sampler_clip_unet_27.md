---
name: unknown_workflow_sampler_clip_unet_27
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.900308
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_omnigen2_image_edit.json, 图片生成/文生图/1939949487580160001.json, 图片生成/文生图/1943503078144286722.json, 图片生成/文生图/Flux2-TurboV2加速_2007448172402057217.json, 图片生成/文生图/Flux2-Turbo加速生图_2005931616717467650.json, 图片生成/文生图/Flux2DEV多图编辑_1993501443036479490.json, 图片生成/文生图/Flux2DEV文生图_1993507322504953858.json, 图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json, 图片生成/文生图/flux2-ftp8 workflow_1993525727769411585.json, 图片生成/文生图/flux2_文生图+图片参考_1993696007951237121.json, 图片生成/文生图/image_flux2_1999252927225229314.json, 图片生成/文生图/动作编辑器应用系列之一__FLUX-2-klein-9b_文生图_2022474573257641985.json, 图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（comfyui-workflow-templates-json/image_omnigen2_image_edit.json、图片生成/文生图/1939949487580160001.json、图片生成/文生图/1943503078144286722.json、图片生成/文生图/Flux2-TurboV2加速_2007448172402057217.json、图片生成/文生图/Flux2-Turbo加速生图_2005931616717467650.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `ReferenceLatent` —— 11/13 个有
- `VAEEncode` —— 11/13 个有
- `BasicGuider` —— 10/13 个有
- `EmptyFlux2LatentImage` —— 10/13 个有
- `Flux2Scheduler` —— 10/13 个有
- `FluxGuidance` —— 10/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `EmptySD3LatentImage` —— 4/13 个有
- `BasicScheduler` —— 3/13 个有
- `DualCFGGuider` —— 3/13 个有
- `ImageConcanate` —— 3/13 个有
- `easy promptList` —— 3/13 个有
- `GetImageSize` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
