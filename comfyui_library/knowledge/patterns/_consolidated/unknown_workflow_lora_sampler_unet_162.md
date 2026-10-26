---
name: unknown_workflow_lora_sampler_unet_162
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8228
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜TaoMate 3步加速 lora_2099873466462855169.json, 视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json, 视频生成/文生视频/Minimax H3 加速双采 Self-Lift 工作流_2099332965401710594.json, 视频生成/文生视频/海螺H3最新融合模型+黑科技加速双采-self-lift工作流_2097523746214080514.json, 视频生成/文生视频/满血版minimax h3黑科技加速内置双采-self-lift工作流_2097892303456260098.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_162

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜TaoMate 3步加速 lora_2099873466462855169.json、视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json、视频生成/文生视频/Minimax H3 加速双采 Self-Lift 工作流_2099332965401710594.json、视频生成/文生视频/海螺H3最新融合模型+黑科技加速双采-self-lift工作流_2097523746214080514.json、视频生成/文生视频/满血版minimax h3黑科技加速内置双采-self-lift工作流_2097892303456260098.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 4/5 个有
- `LoadAudio` —— 4/5 个有
- `MiniMaxChunkFeedForward` —— 4/5 个有
- `MiniMaxLowVRAMAttention` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `AudioCrop` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LTXVSeparateAVLatent` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `MiniMaxH3AudioConditioningT8` —— 1/5 个有
- `RH_Astra` —— 1/5 个有
- `SaveVideoNode` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
