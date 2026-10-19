---
name: unknown_workflow_lora_sampler_unet_43
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.627
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMaxH3-SelfLift工作流V1_2103487158542749698.json, 视频生成/文生视频/self-lift双采工作流（全能参考）_2058746014022066178.json, 视频生成/文生视频/self-lift双采工作流（文生图生视频）_2097961269025402882.json, 视频生成/文生视频/海螺H3最新融合模型+黑科技加速双采-self-lift工作流_2097523746214080514.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMaxH3-SelfLift工作流V1_2103487158542749698.json、视频生成/文生视频/self-lift双采工作流（全能参考）_2058746014022066178.json、视频生成/文生视频/self-lift双采工作流（文生图生视频）_2097961269025402882.json、视频生成/文生视频/海螺H3最新融合模型+黑科技加速双采-self-lift工作流_2097523746214080514.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ModelPreviewOverrideKJ` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `CreateVideo` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `Float` —— 1/4 个有
- `LTXVSeparateAVLatent` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MiniMaxH3AudioConditioningT8` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
