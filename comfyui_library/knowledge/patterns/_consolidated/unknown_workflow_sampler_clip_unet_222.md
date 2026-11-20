---
name: unknown_workflow_sampler_clip_unet_222
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.977667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein9b超高清三视图_2034183674899472385.json, 图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json, 图片生成/图生图/klein 单图参考_2048402694292901891.json, 图片生成/图生图/klein 双图编辑_2048417433756639234.json, 图片生成/图生图/一键拍立得_2077678322762473473.json, 图片生成/图生图/一键生成婚纱照_2045753551078559745.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_222

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Klein9b超高清三视图_2034183674899472385.json、图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json、图片生成/图生图/klein 单图参考_2048402694292901891.json、图片生成/图生图/klein 双图编辑_2048417433756639234.json、图片生成/图生图/一键拍立得_2077678322762473473.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ConditioningZeroOut` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `EmptyFlux2LatentImage` —— 3/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `ImagePadForOutpaint` —— 2/6 个有
- `AILab_ImageStitch` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `LayerStyle: ColorOverlay` —— 1/6 个有
- `Multi Text Merge` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `ResolutionMaster` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `StringConstant` —— 1/6 个有
- `VRAMReserver` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
