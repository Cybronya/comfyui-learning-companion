---
name: unknown_workflow_sampler_clip_unet_41
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.930824
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 指定人物换服装（指定替换、单人换装、服装提取）_2040768619432382465.json, 图片生成/图生图/Flux2 Klein 替换人脸（蒙版指定替换）_2040732116815716354.json, 图片生成/图生图/Flux2 Klein 最强动漫转写实真人_2042405511412326401.json, 图片生成/图生图/Flux2 Klein 美甲迁移增强流_2025502923685367809.json, 图片生成/图生图/Flux2 Klein 美甲迁移增强流_2068736740612988929.json, 图片生成/图生图/Flux2 Klein-9B 多图编辑_2012089508413579266.json, 图片生成/图生图/Flux2 Klein-9B 多图编辑_2012133102637817858.json, 图片生成/图生图/Flux2 Klein-多图编辑-9B版本_2012129280318251010.json, 图片生成/图生图/Flux2 Klein-多图编辑-9B版本_2012144093203275777.json, 图片生成/图生图/Flux2 Klein_史上最强动漫转写实真人_2016180945006628865.json, 图片生成/图生图/Flux2 Klein_史上最强动漫转写实真人_2052278231113453570.json, 图片生成/图生图/Flux2-Klein-9B多图编辑 极速_2011999673732567042.json, 图片生成/图生图/Flux2-Klein-9B多图编辑 极速_2012006356626186241.json, 图片生成/图生图/Flux2-Klein-9B多图编辑+极速_2016797202454159362.json, 图片生成/图生图/Flux2-Klein-9B多图编辑_极速稳定版_2012803071105048578.json, 图片生成/图生图/Flux2-Klein-9B多图编辑基本工作流极速_2012433542348808194.json, 图片生成/图生图/Flux2-Klein-9B现实风格转换_2030135458734280705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 指定人物换服装（指定替换、单人换装、服装提取）_2040768619432382465.json、图片生成/图生图/Flux2 Klein 替换人脸（蒙版指定替换）_2040732116815716354.json、图片生成/图生图/Flux2 Klein 最强动漫转写实真人_2042405511412326401.json、图片生成/图生图/Flux2 Klein 美甲迁移增强流_2025502923685367809.json、图片生成/图生图/Flux2 Klein 美甲迁移增强流_2068736740612988929.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 17 个 workflow 都包含：
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
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 16/17 个有
- `ConditioningZeroOut` —— 16/17 个有
- `LayerUtility: PurgeVRAM` —— 9/17 个有
- `PreviewImage` —— 8/17 个有
- `Fast Groups Bypasser (rgthree)` —— 6/17 个有
- `LoraLoaderModelOnly` —— 6/17 个有
- `InpaintCropImproved` —— 2/17 个有
- `InpaintStitchImproved` —— 2/17 个有
- `DrawMaskOnImage` —— 1/17 个有
- `Fast Groups Muter (rgthree)` —— 1/17 个有
- `INPAINT_ExpandMask` —— 1/17 个有
- `Image Compare (mtb)` —— 1/17 个有
- `ImageStitch` —— 1/17 个有
- `Text Multiline` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
