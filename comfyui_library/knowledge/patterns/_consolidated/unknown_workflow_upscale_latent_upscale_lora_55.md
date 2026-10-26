---
name: unknown_workflow_upscale_latent_upscale_lora_55
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.774
common_nodes: [CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json, 视频生成/图生视频/h3双采样高清流_2092571899955081218.json, 视频生成/图生视频/iniMax H3 六图可选图生视频｜混合模型 潜空间高清直出_2095018141456879618.json, 视频生成/文生视频/MiniMax-H3 极限复杂大动态与人脸去油腻工作流_2096278728602112001.json, 视频生成/文生视频/Minimax H3 双采样全能参考高清工作流｜超分放大｜4倍加速｜8倍加速_2092731840196079618.json, 视频生成/文生视频/Minimax H3 双采样全能参考｜真实电影感｜超分高清放大｜4倍加速｜8倍加速_2094320738051383298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_55

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json、视频生成/图生视频/h3双采样高清流_2092571899955081218.json、视频生成/图生视频/iniMax H3 六图可选图生视频｜混合模型 潜空间高清直出_2095018141456879618.json、视频生成/文生视频/MiniMax-H3 极限复杂大动态与人脸去油腻工作流_2096278728602112001.json、视频生成/文生视频/Minimax H3 双采样全能参考高清工作流｜超分放大｜4倍加速｜8倍加速_2092731840196079618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `BasicScheduler` —— 5/6 个有
- `MiniMaxLowVRAMAttention` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `H3SigmaRefiner` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `FlashVSRNode` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `Sleep` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `HAIGC_VideoLoader` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `VRAM_Debug` —— 2/6 个有
- `孤海注释` —— 2/6 个有
- `CFGGuider` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `ManualSigmas` —— 1/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `布尔孤海` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
