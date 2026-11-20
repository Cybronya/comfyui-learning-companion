---
name: unknown_workflow_lora_sampler_unet_109
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.932143
common_nodes: [CFGNorm, CLIPLoader, CR Latent Input Switch, CR Text, ConditioningZeroOut, EmptySD3LatentImage, KOOK_ImageCompression, KSampler (Efficient), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json, 图片生成/图生图/flux-2-klein-9b-fp8   EDIT   单修图 图像控制_2012434650270011394.json, 平台全量/一键 运行：qwen-image-edit-2511镜头、角度控制，图像编辑_2009853365051727873.json, 平台全量/一键运行：Qwen-Edit-2511   模糊图像高清无损放大_一键运行_2010194893418799105.json, 平台全量/一键运行：qwen 2511 edit  多图 编辑  图像编辑修改_2005082130424229889.json, 平台全量/一键运行：qwen 2511 edit 单图 偏移解决 修图 扩图 编辑_2004788042093260801.json, 视频生成/图生视频/FireRed-Image-Edit-1.1   单图编辑_2032730903151120385.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_109

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json、图片生成/图生图/flux-2-klein-9b-fp8   EDIT   单修图 图像控制_2012434650270011394.json、平台全量/一键 运行：qwen-image-edit-2511镜头、角度控制，图像编辑_2009853365051727873.json、平台全量/一键运行：Qwen-Edit-2511   模糊图像高清无损放大_一键运行_2010194893418799105.json、平台全量/一键运行：qwen 2511 edit  多图 编辑  图像编辑修改_2005082130424229889.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Latent Input Switch`
- `CR Text`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KOOK_ImageCompression`
- `KSampler (Efficient)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `KOOK_SaveJPGImage` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `CR Text Input Switch` —— 4/7 个有
- `PromptExpand` —— 4/7 个有
- `ImageConcanate` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `easy imageScaleDownToSize` —— 2/7 个有
- `CR Seed` —— 1/7 个有
- `QwenMultiangleCameraNode` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `StringFunction|pysssss` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有
- `easy imageScaleToNormPixels` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
