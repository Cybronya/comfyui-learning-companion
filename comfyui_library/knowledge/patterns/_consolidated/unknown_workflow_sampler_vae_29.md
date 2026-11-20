---
name: unknown_workflow_sampler_vae_29
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.82825
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json, 视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json, 视频生成/文生视频/H3-文生视频_2088176717721591810.json, 视频生成/文生视频/MINIMAX-H3-文生视频_2084191170879643650.json, 视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json, 视频生成/文生视频/MINIMAXH3-文生视频8月8日版本_2086533093908893698.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频 加速版_2086019169908248577.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频_2089602856834912257.json, 视频生成/文生视频/MiniMax H3 T2V 文生视频_2097227552527052802.json, 视频生成/文生视频/MiniMax+H3+T2V+文生视频+加速版_2084297867275096065.json, 视频生成/文生视频/MiniMax+H3+T2V+文生视频低显存加速版（6~8GB）_2085705254150168577.json, 视频生成/文生视频/minimax_h3_turbo_lora_4步工作流_2085539352125464578.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_29

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json、视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json、视频生成/文生视频/H3-文生视频_2088176717721591810.json、视频生成/文生视频/MINIMAX-H3-文生视频_2084191170879643650.json、视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
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
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/12 个有
- `DiffusionModelLoaderKJ` —— 6/12 个有
- `Label (rgthree)` —— 6/12 个有
- `UNETLoader` —— 6/12 个有
- `PrimitiveStringMultiline` —— 5/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `LoadImage` —— 3/12 个有
- `PathchSageAttentionKJ` —— 3/12 个有
- `MiniMaxH3SigmaShift` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `SolAttnPatch` —— 2/12 个有
- `SpectrumApplyMiniMaxH3` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `ModelPreviewOverrideKJ` —— 1/12 个有
- `UniBlockSwap` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
