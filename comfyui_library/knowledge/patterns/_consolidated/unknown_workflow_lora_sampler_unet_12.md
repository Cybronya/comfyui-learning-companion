---
name: unknown_workflow_lora_sampler_unet_12
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.804636
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/黑科技加速双采-self-lift工作流-3图1音_2102289015847350274.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-4图1音_2102284106150273026.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-5图1音_2108825320408309761.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-6图1音_2108828857859141634.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2097505105535913985.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2097859473883881474.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2099386693676785665.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2109640374049402882.json, 视频生成/图生视频/黑科技加速双采-self-lift高动态_2102398843047469057.json, 视频生成/文生视频/1-Aiden-黑科技加速双采-self-lift工作流_2097588130751799297.json, 视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/黑科技加速双采-self-lift工作流-3图1音_2102289015847350274.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-4图1音_2102284106150273026.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-5图1音_2108825320408309761.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-6图1音_2108828857859141634.json、视频生成/图生视频/黑科技加速双采-self-lift工作流_2097505105535913985.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `VHS_VideoCombine` —— 10/11 个有
- `LoadImage` —— 7/11 个有
- `Int` —— 4/11 个有
- `SDVN Load Image Url` —— 4/11 个有
- `VHS_LoadAudio` —— 4/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `LoadAudio` —— 2/11 个有
- `LoraLoaderBypassModelOnly` —— 2/11 个有
- `QwenH3PromptLocal` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `JWInteger` —— 1/11 个有
- `RH_Astra` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `SaveVideoNode` —— 1/11 个有
- `Text` —— 1/11 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
