---
name: unknown_workflow_sampler_clip_unet_81
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.890385
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WH-AI-Studio换脸（flux2-klein）_2022508733837877249.json, 图片生成/图生图/一键换脸换头！加强版！Flux Klein BFS_2041772041380044802.json, 图片生成/图生图/万能图像修改编辑超强版-FAN REN_2020960397976674306.json, 图片生成/图生图/人物替换3.0FluxKlein影视替换加速高质量_2012789311053242369.json, 图片生成/图生图/图像编辑9B版-Flux2 Klein-v1_2013615530917240833.json, 图片生成/图生图/换头Flux2Klein多图编辑4B加速版Flux2Klein_2034479385473978369.json, 图片生成/图生图/换头Flux2Klein多图编辑4B加速版_2034605360421543938.json, 图片生成/图生图/换脸 - Flux2Klein多图编辑4B加速版_2048765588482301953.json, 图片生成/图生图/换脸 - Flux2Klein多图编辑4B加速版_2049322969406640130.json, 图片生成/图生图/换脸 - Flux2Klein多图编辑4B加速版_2049400548134232066.json, 图片生成/图生图/换脸 - Flux2Klein多图编辑4B加速版_2057344216329711618.json, 图片生成/图生图/无痕换头换脸 Klein BFS_2041786489603887105.json, 平台全量/Flux2-人物换装（自动遮罩）一键人物换服装｜精准锁脸 身形不变_2050819474974093314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio换脸（flux2-klein）_2022508733837877249.json、图片生成/图生图/一键换脸换头！加强版！Flux Klein BFS_2041772041380044802.json、图片生成/图生图/万能图像修改编辑超强版-FAN REN_2020960397976674306.json、图片生成/图生图/人物替换3.0FluxKlein影视替换加速高质量_2012789311053242369.json、图片生成/图生图/图像编辑9B版-Flux2 Klein-v1_2013615530917240833.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
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
- `CR Text` —— 10/13 个有
- `ImageConcanate` —— 10/13 个有
- `JWFloat` —— 8/13 个有
- `PreviewImage` —— 6/13 个有
- `EmptyFlux2LatentImage` —— 5/13 个有
- `GetImageSize` —— 5/13 个有
- `Image Comparer (rgthree)` —— 5/13 个有
- `Crop Face` —— 3/13 个有
- `GetNode` —— 3/13 个有
- `Load RetinaFace` —— 3/13 个有
- `SetNode` —— 3/13 个有
- `LayerMask: PersonMaskUltra V2` —— 2/13 个有
- `LayerUtility: PurgeVRAM V2` —— 2/13 个有
- `ImageAndMaskPreview` —— 1/13 个有
- `ImageConcatMulti` —— 1/13 个有
- `MaskColorize` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `TextInputBasic` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
