---
name: text_to_image_controlnet_sampler_clip_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.84975
common_nodes: [CLIPLoader, CLIPTextEncode, CR Seed, ConditioningZeroOut, EmptyLatentImage, GenerateNoise, KSampler, LGNoiseInjectionLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, ZImageFunControlnet, easy framesEditor, easy sam3ImageSegmentation, easy sam3ModelLoader]
problems: []
missing: []
members: [图片生成/图生图/Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026.json, 平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2078369803244490753.json, 平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096405023059173377.json, 平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026.json、平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2078369803244490753.json、平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096405023059173377.json、平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GenerateNoise`
- `KSampler`
- `LGNoiseInjectionLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy framesEditor`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_2s_ancestral | - | 4 | 100% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |
| LoRA 模型强度 | 2 | 2 - 2 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2s_ancestral，4 个样本，一致性 100%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
