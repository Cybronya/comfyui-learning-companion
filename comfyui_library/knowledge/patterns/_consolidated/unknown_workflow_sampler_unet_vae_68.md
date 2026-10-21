---
name: unknown_workflow_sampler_unet_vae_68
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8417
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json, 视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json, 视频生成/文生视频/H3-文生视频_2088176717721591810.json, 视频生成/文生视频/MINIMAX-H3-文生视频_2084191170879643650.json, 视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json, 视频生成/文生视频/MINIMAXH3-文生视频8月8日版本_2086533093908893698.json, 视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频-自动提示词_2084463867618488321.json, 视频生成/文生视频/MiniMax H3 lightx2v 4步加速文生视频工作流_2086325686846976002.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_68

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/GF01-MiniMax H3：文生视频_2084716666163908609.json、视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json、视频生成/文生视频/H3-文生视频_2088176717721591810.json、视频生成/文生视频/MINIMAX-H3-文生视频_2084191170879643650.json、视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `Text` —— 2/10 个有
- `孤海注释` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有
- `SpectrumApplyMiniMaxH3` —— 1/10 个有
- `SpectrumSDXL` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
