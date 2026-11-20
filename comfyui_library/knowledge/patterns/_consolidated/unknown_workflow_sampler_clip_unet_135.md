---
name: unknown_workflow_sampler_clip_unet_135
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9272
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生图海报1_2021770523801292801.json, 图片生成/图生图/多图编辑 Flux2-Klein-9b_2062081939934367746.json, 图片生成/图生图/多图编辑 Flux2-Klein_1979531857857515522.json, 图片生成/图生图/添加真实感细节 _ flux 2_1962490094668132354.json, 图片生成/图生图/真人转赛璐璐风格编辑_2068932411035045890.json, 图片生成/图生图/线稿_2016078729386139649.json, 图片生成/图生图/设计工作流——双图迁移_2013146117600448514.json, 图片生成/文生图/文生图+图生图_2039179127982399489.json, 图片生成/文生图/文生图+图生图_2044754006899171330.json, 平台全量/klein克莱因一键生成人物设定图+服装拆解_2017216065415159809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图生图海报1_2021770523801292801.json、图片生成/图生图/多图编辑 Flux2-Klein-9b_2062081939934367746.json、图片生成/图生图/多图编辑 Flux2-Klein_1979531857857515522.json、图片生成/图生图/添加真实感细节 _ flux 2_1962490094668132354.json、图片生成/图生图/真人转赛璐璐风格编辑_2068932411035045890.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `ImageScaleToTotalPixels` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `SaveImage` —— 7/10 个有
- `GetImageSize` —— 6/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `Text` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `CompressImages` —— 3/10 个有
- `DoubaoSizePreset` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `PlaySound|pysssss` —— 3/10 个有
- `SaveImagePlus` —— 3/10 个有
- `CR Text Concatenate` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `AILab_QwenVL_Advanced` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `LayerUtility: ImageReel` —— 1/10 个有
- `LayerUtility: ImageReelComposit` —— 1/10 个有
- `Qwen3_VQA_Plus` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
