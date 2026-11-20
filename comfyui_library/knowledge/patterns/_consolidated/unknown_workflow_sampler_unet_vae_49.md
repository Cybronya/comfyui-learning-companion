---
name: unknown_workflow_sampler_unet_vae_49
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.806714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2张参考图_2110029532303552514.json, 视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json, 视频生成/图生视频/4步MiniMax-H3参考图生视频-LynnReal-Omni_2099804283427446785.json, 视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json, 视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json, 视频生成/图生视频/CG迷-MiniMax H3参考生视频工作流_2085601489535455234.json, 视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json, 视频生成/图生视频/LynnReal-Onmi 多参考+首尾帧满血4步加速音视频_2101265947867828226.json, 视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json, 视频生成/图生视频/MiniMax H3-全能参考-双图版_2089995459833192449.json, 视频生成/图生视频/MiniMax H3-全能参考-四图版_2094418452898476034.json, 视频生成/图生视频/MiniMax H3-全能参考一图版_2094433073793421313.json, 视频生成/图生视频/MinimaxH3 FastH3 Trim多参考+首尾帧满血8步加速音视频生成_2105942822275866626.json, 视频生成/图生视频/MinimaxH3_FastH3_Trim多参考+首尾帧满血8步加速音视频生成_2114189677254242305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_49

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2张参考图_2110029532303552514.json、视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json、视频生成/图生视频/4步MiniMax-H3参考图生视频-LynnReal-Omni_2099804283427446785.json、视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json、视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/14 个有
- `MiniMaxH3ReferenceToVideo` —— 13/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `ComfySwitchNode` —— 9/14 个有
- `PrimitiveBoolean` —— 9/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/14 个有
- `MiniMaxH3ImageToVideo` —— 4/14 个有
- `PrimitiveInt` —— 4/14 个有
- `AnySwitch` —— 3/14 个有
- `Fast Bypasser (rgthree)` —— 3/14 个有
- `MiniMaxChunkFeedForward` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `SDVN Any Show` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `H3AdaLNLoRAFix` —— 1/14 个有
- `LoadImageFromUrl` —— 1/14 个有
- `MiniMaxH3SigmaShift` —— 1/14 个有
- `MiniMaxLowVRAMAttention` —— 1/14 个有
- `ModelPreviewOverrideKJ` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `孤海注释` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
