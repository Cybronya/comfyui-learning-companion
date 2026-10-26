---
name: unknown_workflow_sampler_clip_unet_195
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.959143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/家纺四件套扒花型_2031572811197714434.json, 图片生成/图生图/提亮光影111_2067431193964015617.json, 图片生成/图生图/效果图增强细节，软装色彩分析_2071601421786636290.json, 图片生成/图生图/效果图洗图_增强细节_真实感_2102679806793043970.json, 图片生成/图生图/效果图洗图_增强细节_真实感_2103373723498795010.json, 图片生成/图生图/效果图洗图_增强细节_真实感_零偏移_2062401252247564290.json, 图片生成/图生图/文字清除工作流333333333_2071422706821713921.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_195

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/家纺四件套扒花型_2031572811197714434.json、图片生成/图生图/提亮光影111_2067431193964015617.json、图片生成/图生图/效果图增强细节，软装色彩分析_2071601421786636290.json、图片生成/图生图/效果图洗图_增强细节_真实感_2102679806793043970.json、图片生成/图生图/效果图洗图_增强细节_真实感_2103373723498795010.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `LoraLoaderBypassModelOnly` —— 4/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageUpscaleWithModel` —— 2/7 个有
- `UpscaleModelLoader` —— 2/7 个有
- `ConstrainImage|pysssss` —— 1/7 个有
- `EmptyLatentImage` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Load Image From Url (mtb)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/7 个有
- `SaveImageJPG_GH` —— 1/7 个有
- `Text Multiline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
