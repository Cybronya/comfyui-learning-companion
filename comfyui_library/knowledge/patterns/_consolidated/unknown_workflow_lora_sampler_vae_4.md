---
name: unknown_workflow_lora_sampler_vae_4
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.605
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/全能参考二次采样_MInimaxH3_2090972732266733570.json, 视频生成/文生视频/海螺H3 sigma强化+潜空间放大+高清人脸工作流_2089624110652551169.json, 视频生成/文生视频/海螺H3优化 小脸 打斗 浅空间_2091512771916681217.json, 视频生成/文生视频/海螺二采直出1080P视频H3 sigma强化+潜空间2倍放大（Remix融合模型去油腻）_2091655065831563265.json, 视频生成/文生视频/（0824）万象AI+海螺二采直出1080P（自动提示词）_2091672393700962305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/全能参考二次采样_MInimaxH3_2090972732266733570.json、视频生成/文生视频/海螺H3 sigma强化+潜空间放大+高清人脸工作流_2089624110652551169.json、视频生成/文生视频/海螺H3优化 小脸 打斗 浅空间_2091512771916681217.json、视频生成/文生视频/海螺二采直出1080P视频H3 sigma强化+潜空间2倍放大（Remix融合模型去油腻）_2091655065831563265.json、视频生成/文生视频/（0824）万象AI+海螺二采直出1080P（自动提示词）_2091672393700962305.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `MiniMaxH3SigmaShift` —— 4/5 个有
- `ModelAttentionBackend` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `SplitSigmas` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `MinimaxH3LatentUpscaler3D` —— 3/5 个有
- `LoadAudio` —— 2/5 个有
- `RHLLMChatNode` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `H3LatentUpscaleByJingchen573` —— 1/5 个有
- `MiniMaxH3HybridLoader` —— 1/5 个有
- `MiniMaxLowVRAMAttention` —— 1/5 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/5 个有
- `SolAttnMiniMax` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
