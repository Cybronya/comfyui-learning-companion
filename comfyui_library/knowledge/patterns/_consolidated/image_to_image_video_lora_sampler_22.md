---
name: image_to_image_video_lora_sampler_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.6985
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Prompt Text, FluxKontextMultiReferenceLatentMethod, GetNode, INTConstant, Image Comparer (rgthree), ImageConcatMulti, ImageLoader, ImageResizeKJv2, ImpactInt, Int, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, RIFE VFI, SaveImage, SetNode, ShowText|pysssss, SomethingToString, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy cleanGpuUsed, easy seed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2010239733770752001.json, 视频生成/图生视频/2013989533204877313.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2010239733770752001.json、视频生成/图生视频/2013989533204877313.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageLoader`
- `ImageResizeKJv2`
- `ImpactInt`
- `Int`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `RIFE VFI`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SomethingToString`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `easy seed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `easy promptList` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
