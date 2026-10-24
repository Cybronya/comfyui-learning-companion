---
name: unknown_workflow_video_sampler_unet_38
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6622
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json, 视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json, 视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2111011197268090882.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_base_2109449627366940674.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_multiframe_2109449722762190850.json, 视频生成/图生视频/开源版minimax_h3_i2v_fastH3 快速图生视频精品_2108072194780778497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json、视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json、视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `BlockSparseAttention` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `ModelAttentionBackend` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `GetNode` —— 7/10 个有
- `MiniMaxH3ImageToVideo` —— 7/10 个有
- `MiniMaxH3SigmaShift` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 3/10 个有
- `LoadAudio` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `ManualSigmas` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `MiniMaxH3MotionContext` —— 1/10 个有
- `MiniMaxH3MotionContextChain` —— 1/10 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/10 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/10 个有
- `MiniMaxH3MotionContextTrim` —— 1/10 个有
- `QwenH3PromptLocal` —— 1/10 个有
- `Text` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
