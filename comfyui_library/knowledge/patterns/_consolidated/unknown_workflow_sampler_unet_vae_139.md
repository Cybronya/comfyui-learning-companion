---
name: unknown_workflow_sampler_unet_vae_139
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.4975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3_高动态_Singularity-(新)分段采样进阶工作流_2104944269617352706.json, 视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json, 视频生成/图生视频/fast_h3_omni_base_2114521289464569857.json, 视频生成/图生视频/h3潜空间放大工作流老八_2089878151064276994.json, 视频生成/图生视频/minimaxH3海螺智能提示词优化加速双采样高清放大工作流_2093339172751888385.json, 视频生成/文生视频/(0823修复）海螺H3 sigma强化+潜空间放大+高清人脸工作流_2091505787058348034.json, 视频生成/文生视频/H3 高清优化版-小脸不崩-运动不模糊_2089690104179810306.json, 视频生成/文生视频/minimaxH3海螺智能提示词优化加速双采样高清放大工作流-StarAI_2087299228723933186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_139

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3_高动态_Singularity-(新)分段采样进阶工作流_2104944269617352706.json、视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json、视频生成/图生视频/fast_h3_omni_base_2114521289464569857.json、视频生成/图生视频/h3潜空间放大工作流老八_2089878151064276994.json、视频生成/图生视频/minimaxH3海螺智能提示词优化加速双采样高清放大工作流_2093339172751888385.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `LTXVConcatAVLatent` —— 7/8 个有
- `LTXVSeparateAVLatent` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 7/8 个有
- `ModelAttentionBackend` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `SplitSigmas` —— 7/8 个有
- `H3SigmaRefiner` —— 6/8 个有
- `MinimaxH3LatentUpscaler3D` —— 6/8 个有
- `ModelPreviewOverrideKJ` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `Label (rgthree)` —— 5/8 个有
- `SolAttnMiniMax` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `CreateVideo` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `StariAI-MiniMaxH3-Skill` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `DisableNoise` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
