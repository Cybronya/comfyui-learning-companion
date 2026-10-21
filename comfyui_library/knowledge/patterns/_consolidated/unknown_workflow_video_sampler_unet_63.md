---
name: unknown_workflow_video_sampler_unet_63
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8498
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX多参官方加速工作流_2085378301211799553.json, 视频生成/图生视频/minimax H3酷炫街舞_2085366057304412161.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084127001375494145.json, 视频生成/文生视频/minimax_h3 多参考图生视频+sage加速_2084551631911342082.json, 音频生成/音频生成/minimax_h3 参考图生视频+sage加速_2085965890079776770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MINIMAX多参官方加速工作流_2085378301211799553.json、视频生成/图生视频/minimax H3酷炫街舞_2085366057304412161.json、视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084127001375494145.json、视频生成/文生视频/minimax_h3 多参考图生视频+sage加速_2084551631911342082.json、音频生成/音频生成/minimax_h3 参考图生视频+sage加速_2085965890079776770.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `Display Any (rgthree)` —— 2/5 个有
- `EasyCache` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `MiniMaxH3ImageToVideo` —— 1/5 个有
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
