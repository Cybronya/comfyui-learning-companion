---
name: unknown_workflow_video_lora_sampler_556
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.52975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMAX参数优化版_2089184857632100354.json, 视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json, 视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json, 视频生成/视频生视频/双模型加强版二采重绘_MinimaxH3全能参考_RH兼容版_2106029678061510657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_556

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMAX参数优化版_2089184857632100354.json、视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json、视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json、视频生成/视频生视频/双模型加强版二采重绘_MinimaxH3全能参考_RH兼容版_2106029678061510657.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LoraLoaderBypassModelOnly` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `EasyCache` —— 1/4 个有
- `Float` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `ResizeShortestToNode` —— 1/4 个有
- `Text` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有
- `UniBlockSwap` —— 1/4 个有
- `UniBlockSwapTE` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
