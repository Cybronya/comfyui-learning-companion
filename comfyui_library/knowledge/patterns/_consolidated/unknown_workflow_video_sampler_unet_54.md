---
name: unknown_workflow_video_sampler_unet_54
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8806
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX多参官方加速工作流_2085378301211799553.json, 视频生成/图生视频/minimax H3酷炫街舞_2085366057304412161.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084974167941804033.json, 视频生成/图生视频/单图Minimax H3_2084901814679461889.json, 视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MINIMAX多参官方加速工作流_2085378301211799553.json、视频生成/图生视频/minimax H3酷炫街舞_2085366057304412161.json、视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084974167941804033.json、视频生成/图生视频/单图Minimax H3_2084901814679461889.json、视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `Display Any (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `SolAttnMiniMax` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `MiniMaxH3ImageToVideo` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SimpleCalculatorKJ` —— 1/5 个有
- `StringReplace` —— 1/5 个有
- `TextGenerate` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
