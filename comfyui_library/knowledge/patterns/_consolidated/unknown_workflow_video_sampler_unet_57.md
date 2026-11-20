---
name: unknown_workflow_video_sampler_unet_57
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.579143
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/智能分镜—— 人类对H-3的开发不足1%_2117859365519712258.json, 视频生成/图生视频/fastH3_ref2va_2116818505256493057.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2111011197268090882.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194.json, 视频生成/图生视频/开源版minimax_h3_i2v_fastH3_快速图生视频_2113910481533628418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_57

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/智能分镜—— 人类对H-3的开发不足1%_2117859365519712258.json、视频生成/图生视频/fastH3_ref2va_2116818505256493057.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2111011197268090882.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `MiniMaxH3ImageToVideo` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `MiniMaxH3MotionContext` —— 1/7 个有
- `MiniMaxH3MotionContextChain` —— 1/7 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/7 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/7 个有
- `MiniMaxH3MotionContextTrim` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `RHLLMChatNode` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
