---
name: unknown_workflow_sampler_clip_unet_346
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96775
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/角色设计-克莱因_2026973403596464130.json, 图片生成/文生图/Flux2_Klein 多图编辑精简版_2012069622740164610.json, 图片生成/文生图/StyleSculpt_角色设计(游戏角色设计、动画设定本)_2021892139688398850.json, 平台全量/人物表情 动漫游戏角色设计  游戏角色设计 动画人物设定本 一键生成三视图_2025741207732756481.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_346

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/角色设计-克莱因_2026973403596464130.json、图片生成/文生图/Flux2_Klein 多图编辑精简版_2012069622740164610.json、图片生成/文生图/StyleSculpt_角色设计(游戏角色设计、动画设定本)_2021892139688398850.json、平台全量/人物表情 动漫游戏角色设计  游戏角色设计 动画人物设定本 一键生成三视图_2025741207732756481.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
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
- `CR Prompt Text` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `JDCN_StringToList` —— 3/4 个有
- `JWStringConcat` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ProcessString` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `BasicGuider` —— 1/4 个有
- `BasicScheduler` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
