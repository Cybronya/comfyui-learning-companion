---
name: unknown_workflow_sampler_clip_unet_215
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9005
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/即梦角色标准参考三视图_2026223411495706625.json, 图片生成/图生图/去ai-V2版本_2051151522649657345.json, 图片生成/图生图/去亮_2067431169767071746.json, 图片生成/图生图/发型迁移与更换_2051141221707468801.json, 图片生成/图生图/提亮光影111_2067431193964015617.json, 图片生成/文生图/产品抠图透明背景精修版+全节点注释_2090760561532424194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_215

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/即梦角色标准参考三视图_2026223411495706625.json、图片生成/图生图/去ai-V2版本_2051151522649657345.json、图片生成/图生图/去亮_2067431169767071746.json、图片生成/图生图/发型迁移与更换_2051141221707468801.json、图片生成/图生图/提亮光影111_2067431193964015617.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
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
- `EmptyFlux2LatentImage` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PreviewImage` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `JoinImageWithAlpha` —— 1/6 个有
- `LayerMask: BiRefNetUltra` —— 1/6 个有
- `SAM3Segment` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有
- `easy mathInt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1512 | - | 1 | 100% |
| 高度 | 1512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
