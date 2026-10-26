---
name: unknown_workflow_upscale_sampler_clip_20
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.889
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Image Comparer (rgthree), LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2klein 4K高清放大_2041033443819130881.json, 图片生成/图生图/flux2洗图+放大_2101535680026464257.json, 图片生成/图生图/klein9b白底生背景家具美式中古风格支持_2055473199701348354.json, 图片生成/图生图/klein9b白底自动匹配背景家具美式风_2059563878874439681.json, 图片生成/图生图/老孙AI 一键OK 老照片修复_2088443376889847809.json, 图片生成/图生图/老郑一键老照片修复_2088421738475515906.json, 图片生成/图生图/蒜香卡普klein9b白底生背景家具美式中古风格支持2048px_2051843695250554881.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/flux2klein 4K高清放大_2041033443819130881.json、图片生成/图生图/flux2洗图+放大_2101535680026464257.json、图片生成/图生图/klein9b白底生背景家具美式中古风格支持_2055473199701348354.json、图片生成/图生图/klein9b白底自动匹配背景家具美式风_2059563878874439681.json、图片生成/图生图/老孙AI 一键OK 老照片修复_2088443376889847809.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `Flux2Scheduler` —— 5/7 个有
- `KSamplerSelect` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `Float` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `PlaySound|pysssss` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `easy getNode` —— 3/7 个有
- `easy setNode` —— 3/7 个有
- `ImageScaleBy` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `ImageBlur` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有
- `easy imageColorMatch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
