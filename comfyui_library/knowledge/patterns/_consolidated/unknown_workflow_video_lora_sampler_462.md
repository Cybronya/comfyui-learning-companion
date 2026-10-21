---
name: unknown_workflow_video_lora_sampler_462
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.79125
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, ConditioningZeroOut, ExtendIntermediateSigmas, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaGetNode, PixaromaLabel, PixaromaResolution, PixaromaSetNode, PrimitiveFloat, ResolutionSelector, SaveImage, SelfLiftAvatarH3Sampler, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy imageListToImageBatch, easy imageSplitGrid]
problems: []
missing: [CR Text, CR Text Concatenate, easy imageListToImageBatch, easy imageSplitGrid, CR Prompt Text]
members: [图片生成/图生图/2106077311387922433.json, 图片生成/文生图/全能图片G-IMAGE-2_5 4宫格4图 _ MiniMax H3 _一次4视_2106077311387922433.json, 视频生成/图生视频/Qwen Image 2.1 一键4图+Minimax H3 SelfLift 超高清4条视频生成_2105768139874201602.json, 视频生成/图生视频/全能图片G-IMAGE-2.5  + MiniMax H3 SelfLift  1次9图 9超高清视频生_2104630370133168129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_462

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2106077311387922433.json、图片生成/文生图/全能图片G-IMAGE-2_5 4宫格4图 _ MiniMax H3 _一次4视_2106077311387922433.json、视频生成/图生视频/Qwen Image 2.1 一键4图+Minimax H3 SelfLift 超高清4条视频生成_2105768139874201602.json、视频生成/图生视频/全能图片G-IMAGE-2.5  + MiniMax H3 SelfLift  1次9图 9超高清视频生_2104630370133168129.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `ExtendIntermediateSigmas`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaGetNode`
- `PixaromaLabel`
- `PixaromaResolution`
- `PixaromaSetNode`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveImage`
- `SelfLiftAvatarH3Sampler`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy imageListToImageBatch`
- `easy imageSplitGrid`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `CR Text Concatenate` —— 3/4 个有
- `PixaromaGroupSwitch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RHLLMChatNode` —— 3/4 个有
- `RHSettingsNode` —— 3/4 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageRGBA2RGB` —— 1/4 个有
- `Images to RGB` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `QwenImage21Cache` —— 1/4 个有
- `QwenPERewriteT8` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Switch any [Crystools]` —— 1/4 个有
- `TextEncodeQwenImage21` —— 1/4 个有
- `VRAM_Debug` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 40 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、easy imageListToImageBatch、easy imageSplitGrid、CR Prompt Text
