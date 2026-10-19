---
name: unknown_workflow_video_lora_sampler_882
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8965
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ImageBatch, ImageFromBatch, ImageResizeKJv2, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PreviewAny, PreviewImage, RH_LLMAPI_NODE, RH_Nano_Banana2_Image2Image, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2011273091535605761.json, 视频生成/图生视频/2004870695077244929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_882

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2011273091535605761.json、视频生成/图生视频/2004870695077244929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `GetImagesFromBatchIndexed` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RegexReplace` —— 1/2 个有
- `ResizeAndPadImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
