---
name: image_to_image_sampler_clip_unet_36
type: Image To Image
frequency: 9
level: weak
coverage: 0.884222
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2-Klein实现人物不同视角的白底照片【晨晨的AI应用包007】_2013884427834757122.json, 图片生成/图生图/Flux Klein 图生图工作流_2018899055077761025.json, 图片生成/图生图/Flux-Klein 真人转动漫_2033832402732191745.json, 图片生成/图生图/Flux2-Klein-单图编辑 （转真实lora）_2091149910098927618.json, 图片生成/图生图/Flux2-Klein-单图编辑_2087938968968060930.json, 图片生成/图生图/Flux2-Klein-多图编辑_2087940335677825026.json, 图片生成/图生图/Flux2-klein9B多角度分镜直出_2022298975256186881.json, 图片生成/图生图/flux-2-klein-9b超强老照片修复-高清放大_2038820603309854721.json, 图片生成/图生图/flux-2-klei洗图 去Ai感 高清修复 细节增强 告别塑料感_2098998012981899265.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein实现人物不同视角的白底照片【晨晨的AI应用包007】_2013884427834757122.json、图片生成/图生图/Flux Klein 图生图工作流_2018899055077761025.json、图片生成/图生图/Flux-Klein 真人转动漫_2033832402732191745.json、图片生成/图生图/Flux2-Klein-单图编辑 （转真实lora）_2091149910098927618.json、图片生成/图生图/Flux2-Klein-单图编辑_2087938968968060930.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `EmptyFlux2LatentImage` —— 6/9 个有
- `ConditioningZeroOut` —— 5/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `GetNode` —— 2/9 个有
- `ImageResize+` —— 2/9 个有
- `ImageScaleBy` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `Text` —— 2/9 个有
- `easy promptLine` —— 2/9 个有
- `Float` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `KSamplerAdvanced` —— 1/9 个有
- `ModelSamplingAuraFlow` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `Text Multiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 9 | 0% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，9 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
