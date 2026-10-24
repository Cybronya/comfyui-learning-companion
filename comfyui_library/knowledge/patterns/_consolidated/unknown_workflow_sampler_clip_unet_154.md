---
name: unknown_workflow_sampler_clip_unet_154
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.936
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/▶2_Flux2Klein-单图及多图编辑_2066881431275663361.json, 图片生成/图生图/【1月】高质量图像编辑 Flux2-Klein-9B_2012162088738758658.json, 图片生成/图生图/【flux2-klein】动漫人物转真人_2018492884374261761.json, 图片生成/图生图/【flux2-klein】手绘漫画风格_2018497479477567489.json, 图片生成/图生图/【推荐动漫转真人】Flux2 Klein_史上最强动漫转写实真人_2017575897674551298.json, 图片生成/图生图/【阡陌】FLUX-2-Klein 9B base版单图编辑工作流_2016508238623154177.json, 图片生成/图生图/一次出图100张 海量图生图 多角度 保持人物一致 Flux2 Klein 9B Klein  一图_2027279328433676290.json, 图片生成/图生图/告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/▶2_Flux2Klein-单图及多图编辑_2066881431275663361.json、图片生成/图生图/【1月】高质量图像编辑 Flux2-Klein-9B_2012162088738758658.json、图片生成/图生图/【flux2-klein】动漫人物转真人_2018492884374261761.json、图片生成/图生图/【flux2-klein】手绘漫画风格_2018497479477567489.json、图片生成/图生图/【推荐动漫转真人】Flux2 Klein_史上最强动漫转写实真人_2017575897674551298.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `CR Text` —— 3/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `easy imageConcat` —— 2/8 个有
- `CR Prompt List` —— 1/8 个有
- `ConditioningAddImageReference` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Load Lora` —— 1/8 个有
- `TextCombinerTwo` —— 1/8 个有
- `easy promptLine` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
