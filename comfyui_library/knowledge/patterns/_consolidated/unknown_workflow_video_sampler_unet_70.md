---
name: unknown_workflow_video_sampler_unet_70
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.764333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/minimax_h3_i2v w4a8-超低显存-0810_2086689468593041410.json, 视频生成/文生视频/video_minimax_h3_t2v_2084181061847838721.json, 视频生成/文生视频/文生视频 可文字指定音频 minimax h3_2084283510747127809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/minimax_h3_i2v w4a8-超低显存-0810_2086689468593041410.json、视频生成/文生视频/video_minimax_h3_t2v_2084181061847838721.json、视频生成/文生视频/文生视频 可文字指定音频 minimax h3_2084283510747127809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
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
- `PreviewAny` —— 2/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SolAttnPatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
