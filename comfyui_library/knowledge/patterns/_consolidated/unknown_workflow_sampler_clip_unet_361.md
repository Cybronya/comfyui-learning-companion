---
name: unknown_workflow_sampler_clip_unet_361
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.814333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/角色设计-克莱因_2026973403596464130.json, 图片生成/文生图/StyleSculpt_角色设计(游戏角色设计、动画设定本)_2021892139688398850.json, 图片生成/文生图/一键拍立得+全节点注释_2077751254561943553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_361

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/角色设计-克莱因_2026973403596464130.json、图片生成/文生图/StyleSculpt_角色设计(游戏角色设计、动画设定本)_2021892139688398850.json、图片生成/文生图/一键拍立得+全节点注释_2077751254561943553.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Prompt Text` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `JDCN_StringToList` —— 2/3 个有
- `JWStringConcat` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ImagePadForOutpaint` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
