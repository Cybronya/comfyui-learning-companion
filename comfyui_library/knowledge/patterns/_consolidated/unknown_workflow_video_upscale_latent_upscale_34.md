---
name: unknown_workflow_video_upscale_latent_upscale_34
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5278
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/高清 替换（借鉴）_2108884315378642945.json, 视频生成/图生视频/H3 多参考双采｜5秒一致性版_2098723223021113346.json, 视频生成/图生视频/H3短剧生成新模型_2102294100425920514.json, 视频生成/图生视频/H3融合模型专属双采【16步高清PLUS 低显存危！】_2111450243706482690.json, 视频生成/图生视频/MiniMax H3-多参考生视频 快速高质量_2098739556991455233.json, 视频生成/图生视频/MiniMax H3-多参考生视频-720p_2094616194417516546.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2094397865706737666.json, 视频生成/图生视频/MiniMax H3-多参考生视频-自用_2099876679551377409.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-优化版_2099771867585409025.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-优化版_2100032660772057090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_34

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/高清 替换（借鉴）_2108884315378642945.json、视频生成/图生视频/H3 多参考双采｜5秒一致性版_2098723223021113346.json、视频生成/图生视频/H3短剧生成新模型_2102294100425920514.json、视频生成/图生视频/H3融合模型专属双采【16步高清PLUS 低显存危！】_2111450243706482690.json、视频生成/图生视频/MiniMax H3-多参考生视频 快速高质量_2098739556991455233.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 9/10 个有
- `easy float` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `Text` —— 8/10 个有
- `忽略多组孤海` —— 8/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `llama_cpp_instruct_adv` —— 4/10 个有
- `llama_cpp_model_loader` —— 4/10 个有
- `llama_cpp_parameters` —— 4/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `Lora Loader Stack (rgthree)` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `SolAttnMiniMax` —— 2/10 个有
- `BlockSparseAttention` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `ResizeImageMaskNode` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy loraStack` —— 1/10 个有
- `easy loraStackApply` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
