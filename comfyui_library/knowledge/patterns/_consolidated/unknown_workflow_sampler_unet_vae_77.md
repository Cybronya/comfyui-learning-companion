---
name: unknown_workflow_sampler_unet_vae_77
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.8295
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/mini_max文生视频_2084531376707166209.json, 视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json, 视频生成/文生视频/minimaxH3开源版文生视频(8step加速)_2090102856362840065.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json, 视频生成/文生视频/minimax_h3 4steps加速_2085757759953399809.json, 视频生成/文生视频/minimax_h3_lightx2v正式版 文生、图生、首尾帧加速_2085755880041181185.json, 视频生成/文生视频/minimax_h3_文生视频4步加速_2084135777386192898.json, 视频生成/文生视频/minimax_h3_文生视频_8步加速_2084159928788410370.json, 视频生成/文生视频/【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970.json, 视频生成/文生视频/【遇见AI】Minimax H3官方提示词skill效果测试_2088103932554993666.json, 视频生成/文生视频/一键工作流_2088139639545749506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_77

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/mini_max文生视频_2084531376707166209.json、视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json、视频生成/文生视频/minimaxH3开源版文生视频(8step加速)_2090102856362840065.json、视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json、视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json…）

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
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/12 个有
- `PathchSageAttentionKJ` —— 6/12 个有
- `LoadImage` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `ModelAttentionBackend` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `CLIPTextEncode` —— 1/12 个有
- `EasyCache` —— 1/12 个有
- `ModelPatchTorchSettings` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `SetReserveVRAM` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
