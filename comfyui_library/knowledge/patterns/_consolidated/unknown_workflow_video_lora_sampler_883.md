---
name: unknown_workflow_video_lora_sampler_883
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.459
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, Fast Groups Bypasser (rgthree), GetImagesFromBatchIndexed, GetNode, INTConstant, Image Comparer (rgthree), ImageBatchExtendWithOverlap, ImageResizeKJv2, JWStringConcat, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, Qwen3_VQA, ReActorFaceSwap, ReActorMaskHelper, SaveImage, SetNode, ShowText|pysssss, SomethingToString, Split String, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/2017490578111467522.json, 视频生成/图生视频/2046492277312327681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_883

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2017490578111467522.json、视频生成/图生视频/2046492277312327681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `JWStringConcat`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `ReActorFaceSwap`
- `ReActorMaskHelper`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SomethingToString`
- `Split String`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
