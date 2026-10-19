---
name: unknown_workflow_lora_sampler_unet_42
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8285
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json, 视频生成/文生视频/8步加速Mini Max H3图生视频_2084136196300697601.json, 视频生成/文生视频/Dasiwa+H3 taomate 3步加速 中远距离不崩脸_2101450830070247426.json, 视频生成/文生视频/🔪🔪阶段总结版！MiniMax H3全功能加速工作流拆解系列04集_2091383371724316673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json、视频生成/文生视频/8步加速Mini Max H3图生视频_2084136196300697601.json、视频生成/文生视频/Dasiwa+H3 taomate 3步加速 中远距离不崩脸_2101450830070247426.json、视频生成/文生视频/🔪🔪阶段总结版！MiniMax H3全功能加速工作流拆解系列04集_2091383371724316673.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `ModelPreviewOverrideKJ` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `QwenH3PromptLocal` —— 1/4 个有
- `SolAttnMiniMax` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
