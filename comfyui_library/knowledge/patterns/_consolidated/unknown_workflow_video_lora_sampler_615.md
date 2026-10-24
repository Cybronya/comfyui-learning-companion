---
name: unknown_workflow_video_lora_sampler_615
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.472333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3短剧直出超级多合一工作流_2092982325507350530.json, 视频生成/文生视频/MiniMax H3 多参2采8步加速_2091443109673660417.json, 视频生成/文生视频/MiniMax H3短剧直出超级多合一工作流_2089404579107659777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_615

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3短剧直出超级多合一工作流_2092982325507350530.json、视频生成/文生视频/MiniMax H3 多参2采8步加速_2091443109673660417.json、视频生成/文生视频/MiniMax H3短剧直出超级多合一工作流_2089404579107659777.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `ComfySwitchNode` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `RegexExtract` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `YUAN_TXTConvertAny` —— 2/3 个有
- `YUAN_TXTJsonExtractor` —— 2/3 个有
- `YUAN_TXTParagraphSplitter` —— 2/3 个有
- `easy positive` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
