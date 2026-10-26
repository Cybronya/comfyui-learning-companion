---
name: image_to_image_lora_sampler_unet_90
type: Image To Image
frequency: 7
level: strong
coverage: 0.570429
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, GetNode, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwenedit_image_自由创作分镜_2041820186872909826.json, 图片生成/图生图/【AI】产品设计及模特上身（学员练习工作流）_2026934710932348930.json, 图片生成/图生图/【AI】图像编辑控制工作流(学员练习)_2011360098072928257.json, 图片生成/图生图/【AI】图像编辑控制工作流)_2085901700283592705.json, 图片生成/图生图/【AI】图像编辑控制工作流)_2085923884175548418.json, 图片生成/图生图/一键证件照生成_2086806567952932866.json, 图片生成/图生图/课程案例演示——图像编辑控制工作流教学_2074004701275840514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/qwenedit_image_自由创作分镜_2041820186872909826.json、图片生成/图生图/【AI】产品设计及模特上身（学员练习工作流）_2026934710932348930.json、图片生成/图生图/【AI】图像编辑控制工作流(学员练习)_2011360098072928257.json、图片生成/图生图/【AI】图像编辑控制工作流)_2085901700283592705.json、图片生成/图生图/【AI】图像编辑控制工作流)_2085923884175548418.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 6/7 个有
- `TextEncodeQwenImageEdit` —— 6/7 个有
- `TextInput_` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `ImageConcanate` —— 5/7 个有
- `AIO_Preprocessor` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `CR Prompt Text` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `EmptySD3LatentImage` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `RMBG` —— 1/7 个有
- `SaveGLB` —— 1/7 个有
- `Trellis2LoadModel` —— 1/7 个有
- `Trellis2MeshWithVoxelGenerator` —— 1/7 个有
- `Trellis2PostProcessAndUnWrapAndRasterizer` —— 1/7 个有
- `Trellis2SimplifyMesh` —— 1/7 个有
- `TrimeshToMESH` —— 1/7 个有
- `easy promptLine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
