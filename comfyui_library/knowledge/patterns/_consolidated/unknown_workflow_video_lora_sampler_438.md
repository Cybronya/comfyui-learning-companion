---
name: unknown_workflow_video_lora_sampler_438
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.487
common_nodes: [CLIPLoader, CLIPTextEncode, CR Seed, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, KSamplerAdvanced, Label (rgthree), LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, SetNode, TorchCompileModel, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_VideoCombine, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1968927593699450881.json, 视频生成/图生视频/1967394231394373634.json, 视频生成/图生视频/1966805388979056641.json, 视频生成/图生视频/1964217924158373889.json, 视频生成/文生视频/1966178940819771393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_438

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1968927593699450881.json、视频生成/图生视频/1967394231394373634.json、视频生成/图生视频/1966805388979056641.json、视频生成/图生视频/1964217924158373889.json、视频生成/文生视频/1966178940819771393.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SetNode`
- `TorchCompileModel`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerColor: BrightnessContrastV2` —— 4/5 个有
- `RIFE VFI` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `easy promptLine` —— 3/5 个有
- `ImpactInt` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `Text Concatenate` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `wanBlockSwap` —— 2/5 个有
- `CR Prompt List` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `FromListGet1String` —— 1/5 个有
- `ImageColorMatch+` —— 1/5 个有
- `LoadUpscalerTensorrtModel` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `UpscalerTensorrt` —— 1/5 个有
- `WanFirstLastFrameToVideo` —— 1/5 个有
- `string_util_StrSplit` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 4 | 5 | 25% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
