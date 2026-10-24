---
name: unknown_workflow_sampler_clip_unet_35
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.962684
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Klein 9b FP8 细节重绘超分辨率 极简工作流_2018990184506855426.json, 图片生成/图生图/Flux Klein 人物融入场景_2013179162063802369.json, 图片生成/图生图/Flux-2-Klein-4B（单图_多图编辑）_2012147672551006210.json, 图片生成/图生图/Flux-2-Klein-9B（单图编辑）_2012096588763635713.json, 图片生成/图生图/Flux-2-Klein-9B（多图编辑）_2012129810344054785.json, 图片生成/图生图/Flux-Klein｜换头+换脸二合一_2099320463754354690.json, 图片生成/图生图/Flux-Klein｜换头+换脸二合一_2099664438902222850.json, 图片生成/图生图/Flux2 Klein 单图编辑9B版_2012048543007121409.json, 图片生成/图生图/Flux2 Klein 双图编辑9B版_2012162140509052929.json, 图片生成/图生图/Flux2 Klein 双图编辑_2012443837314113537.json, 图片生成/图生图/Flux2 Klein 双图编辑_2070334381268488193.json, 图片生成/图生图/Flux2 Klein 图像编辑9B_单图编辑_2012093251225915394.json, 图片生成/图生图/Flux2 Klein 图像编辑9B版_2012021681962881026.json, 图片生成/图生图/Flux2 Klein 图像编辑9B版_2070062677459820545.json, 图片生成/图生图/Flux2 Klein 图像编辑_2013088463502974978.json, 图片生成/图生图/Flux2 Klein 图像编辑_2070063458003021826.json, 图片生成/图生图/Flux2-klein 双图编辑 指定画面比例_2013890699959209986.json, 图片生成/图生图/Flux2Klein 单图编辑 指定画面比例_2013884566422949890.json, 图片生成/图生图/Flux2_Klein 图像编辑9B版-官方版_2012026824955531265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Flux Klein 9b FP8 细节重绘超分辨率 极简工作流_2018990184506855426.json、图片生成/图生图/Flux Klein 人物融入场景_2013179162063802369.json、图片生成/图生图/Flux-2-Klein-4B（单图_多图编辑）_2012147672551006210.json、图片生成/图生图/Flux-2-Klein-9B（单图编辑）_2012096588763635713.json、图片生成/图生图/Flux-2-Klein-9B（多图编辑）_2012129810344054785.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `ConditioningZeroOut` —— 18/19 个有
- `GetImageSize` —— 18/19 个有
- `Flux2Scheduler` —— 17/19 个有
- `ImageScaleToTotalPixels` —— 17/19 个有
- `CR Text` —— 10/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/19 个有
- `BasicScheduler` —— 2/19 个有
- `EmptyUnitGenerator_UTK` —— 2/19 个有
- `ImageScale` —— 2/19 个有
- `ImageResize+` —— 1/19 个有
- `ImageScaleBy` —— 1/19 个有
- `ImageSharpen` —— 1/19 个有
- `LayerColor: AutoAdjustV2` —— 1/19 个有
- `LayerUtility: PurgeVRAM V2` —— 1/19 个有
- `Text Multiline` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
