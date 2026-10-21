---
name: unknown_workflow_sampler_clip_unet_89
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.926857
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2105994124833943553.json, 图片生成/图生图/2106023301272399873.json, 图片生成/文生图/Flux2_Klein 三图编辑_2012088869042262018.json, 图片生成/文生图/Flux2_Klein 多图编辑_2012086737983508482.json, 图片生成/文生图/Flux2_Klein 多图编辑精简版_2012069622740164610.json, 图片生成/文生图/danotebook-flux2-klein-9b_2062427994236481537.json, 图片生成/文生图/klein_文生图+图像编辑_2042538360702509058.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2105994124833943553.json、图片生成/图生图/2106023301272399873.json、图片生成/文生图/Flux2_Klein 三图编辑_2012088869042262018.json、图片生成/文生图/Flux2_Klein 多图编辑_2012086737983508482.json、图片生成/文生图/Flux2_Klein 多图编辑精简版_2012069622740164610.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/7 个有
- `BasicScheduler` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `ReferenceLatent` —— 5/7 个有
- `PrimitiveInt` —— 4/7 个有
- `CFGGuider` —— 3/7 个有
- `CR Text` —— 3/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `EmptyFlux2LatentImage` —— 3/7 个有
- `EmptyLatentImage` —— 3/7 个有
- `Flux2Scheduler` —— 3/7 个有
- `AILab_QwenVL` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有
- `StringCompare` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

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
