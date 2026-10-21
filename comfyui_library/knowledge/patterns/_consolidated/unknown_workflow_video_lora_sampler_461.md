---
name: unknown_workflow_video_lora_sampler_461
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7945
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PT_H3ConcatAVLatent, PixaromaGetNode, PixaromaLabel, PixaromaResolution, PixaromaSetNode, PreviewImage, RHHiddenNodes, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Switch any [Crystools], Text, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine, easy boolean, easy cleanGpuUsed, easy imageListToImageBatch, easy seed, easy showAnything]
problems: []
missing: [CR Text, CR Text Concatenate, LayerUtility: PurgeVRAM V2, Switch any [Crystools], Text Multiline, easy boolean, easy cleanGpuUsed, easy imageListToImageBatch, CR Prompt Text, easy promptLine, easy seed]
members: [图片生成/图生图/2088827135791296513.json, 视频生成/图生视频/Flux2_Klein_9B_电影级分镜_+_MiniMax_H3_影像生成工作流_2104386310512406530.json, 视频生成/图生视频/Flux2_Klein_9B_电影级分镜_+_MiniMax_H3_影像生成工作流_2104752656664317954.json, 视频生成/图生视频/MiniMax H3 +G -IMAGE-2.5 九宫格批量电影分镜视频工作流_2089027904285003777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_461

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2088827135791296513.json、视频生成/图生视频/Flux2_Klein_9B_电影级分镜_+_MiniMax_H3_影像生成工作流_2104386310512406530.json、视频生成/图生视频/Flux2_Klein_9B_电影级分镜_+_MiniMax_H3_影像生成工作流_2104752656664317954.json、视频生成/图生视频/MiniMax H3 +G -IMAGE-2.5 九宫格批量电影分镜视频工作流_2089027904285003777.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PT_H3ConcatAVLatent`
- `PixaromaGetNode`
- `PixaromaLabel`
- `PixaromaResolution`
- `PixaromaSetNode`
- `PreviewImage`
- `RHHiddenNodes`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Switch any [Crystools]`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy imageListToImageBatch`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `CR Text Concatenate` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `Float` —— 3/4 个有
- `Flux2Scheduler` —— 3/4 个有
- `ModelMemoryUsageFactorOverride` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `ProcessString` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `Images to RGB` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `RHSettingsNode` —— 1/4 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 1/4 个有
- `easy imageSplitGrid` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、LayerUtility: PurgeVRAM V2、Switch any [Crystools]、Text Multiline
