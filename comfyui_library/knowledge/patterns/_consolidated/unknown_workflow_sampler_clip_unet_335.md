---
name: unknown_workflow_sampler_clip_unet_335
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.988667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, KSamplerSelect, LoadImage, RHHiddenNodes, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SimpleMathDual+, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2_Klein万物迁移_2012538636029403137.json, 图片生成/图生图/Flux2_Klein局部重绘_2012704330494779394.json, 图片生成/图生图/Flux2_Klein换头_2012518493354201089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_335

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2_Klein万物迁移_2012538636029403137.json、图片生成/图生图/Flux2_Klein局部重绘_2012704330494779394.json、图片生成/图生图/Flux2_Klein换头_2012518493354201089.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RHHiddenNodes`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMathDual+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Blank` —— 2/3 个有
- `LayerUtility: ImageBlend V2` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `Segment` —— 1/3 个有
- `TextBox` —— 1/3 个有
- `TextConcat` —— 1/3 个有
- `Textbox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | 640 - 640 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，观测区间 640 - 640，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
