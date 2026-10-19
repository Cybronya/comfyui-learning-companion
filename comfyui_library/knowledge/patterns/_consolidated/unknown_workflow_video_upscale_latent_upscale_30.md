---
name: unknown_workflow_video_upscale_latent_upscale_30
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.924
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderBypassModelOnly, ManualSigmas, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LatentUpscaleBy32T8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PreviewAny, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/8.25Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092206996211724289.json, 数字人/数字人/8.25Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092231431488622593.json, 数字人/数字人/（0901）Minimax参考生视频V3_2094657495255048194.json, 视频生成/图生视频/8.25Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092676059840991233.json, 视频生成/图生视频/Minimax参考生视频V3_2091389333650628610.json, 视频生成/图生视频/Minimax参考生视频V3_2091443515422236674.json, 视频生成/图生视频/（0824）Minimax参考生视频V3_2091726026987626498.json, 视频生成/图生视频/（0828）Minimax参考生视频V3_2093315459616694273.json, 视频生成/图生视频/（0830）Minimax参考生视频V3_2094357571929989121.json, 视频生成/图生视频/（0913）Minimax参考生视频V3_2099142712363667458.json, 视频生成/文生视频/10.09新工作流_2108550820999553026.json, 视频生成/文生视频/（0930）Minimax参考生视频V3_2105122969159815169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_30

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/8.25Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092206996211724289.json、数字人/数字人/8.25Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092231431488622593.json、数字人/数字人/（0901）Minimax参考生视频V3_2094657495255048194.json、视频生成/图生视频/8.25Minimax H3+双采+加速+Lantent Upscaler参考生视频_2092676059840991233.json、视频生成/图生视频/Minimax参考生视频V3_2091389333650628610.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `ManualSigmas`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LatentUpscaleBy32T8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PreviewAny`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any To String (mtb)` —— 11/12 个有
- `JoinStringMulti` —— 11/12 个有
- `LoadAudio` —— 11/12 个有
- `StringConcatenate` —— 11/12 个有
- `BatchImagesNode` —— 10/12 个有
- `llama_cpp_instruct_adv` —— 10/12 个有
- `llama_cpp_model_loader` —— 10/12 个有
- `llama_cpp_parameters` —— 10/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `MiniMaxH3HybridLoader` —— 8/12 个有
- `ModelPreviewOverrideKJ` —— 8/12 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 3/12 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 3/12 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 3/12 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 3/12 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/12 个有
- `JjkText` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
