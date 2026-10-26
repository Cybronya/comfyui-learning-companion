---
name: unknown_workflow_sampler_clip_unet_78
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.906667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/即梦角色标准参考三视图_2026223411495706625.json, 图片生成/图生图/去ai-V2版本_2051151522649657345.json, 图片生成/图生图/去亮_2067431169767071746.json, 图片生成/图生图/双图编辑_2065803421642481665.json, 图片生成/图生图/双图编辑_2066850392478146562.json, 图片生成/图生图/双图编辑版+全能模型（FLUX2+Klein）_2012868598808715265.json, 图片生成/图生图/告别等待：FLUX.2 [klein] 开启“实时视觉合成”新时代_2012151475887149058.json, 图片生成/图生图/图片换背景工作流+全节点注释_2086268740781559809.json, 图片生成/图生图/幻影疾驰 • 视觉冲击CG造像师：定格震撼人心的游戏视觉大片_2013554944284037122.json, 图片生成/图生图/真人感换装_2105190551246172161.json, 图片生成/图生图/素描手绘风格迁移-Flux2 Klien_2065681291726643202.json, 图片生成/图生图/风格迁移-精准画风还原_Flux2 Klien_2066710064941060097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/即梦角色标准参考三视图_2026223411495706625.json、图片生成/图生图/去ai-V2版本_2051151522649657345.json、图片生成/图生图/去亮_2067431169767071746.json、图片生成/图生图/双图编辑_2065803421642481665.json、图片生成/图生图/双图编辑_2066850392478146562.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
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
- `EmptyFlux2LatentImage` —— 11/12 个有
- `GetImageSize` —— 11/12 个有
- `ImageScaleToTotalPixels` —— 9/12 个有
- `CR Text` —— 8/12 个有
- `PreviewImage` —— 7/12 个有
- `LayerUtility: ImageReel` —— 6/12 个有
- `LayerUtility: ImageReelComposit` —— 6/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `Image Comparer (rgthree)` —— 4/12 个有
- `ImageStitch` —— 4/12 个有
- `PrimitiveFloat` —— 4/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `easy imageConcat` —— 2/12 个有
- `AILab_QwenVL` —— 1/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `EmptyLatentImage` —— 1/12 个有
- `PlaySound|pysssss` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `TextCombinerTwo` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy mathInt` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1512 | - | 1 | 100% |
| 高度 | 1512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
