---
name: unknown_workflow_sampler_unet_vae_116
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.726889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json, 视频生成/文生视频/minimax_h3_r2v_video_edit视频编辑_2094267455395950594.json, 视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json, 视频生成/文生视频/人物真实低动态H3+sigma强化+潜空间放大工作流 双采_2096114490512330753.json, 视频生成/文生视频/动漫短剧工作流（一键直出1080P竖屏短剧提示词未自动优化）_2093587306430160898.json, 视频生成/文生视频/啊癫 minimaxh3极速版二采潜空间直接放大（去油版）_2093957991434379265.json, 视频生成/文生视频/收藏级！H3 加速+二采+打斗全能工作流拆解系列05集_2092970619469123586.json, 视频生成/文生视频/海螺H3 sigma强化+潜空间放大+高清人脸工作流_2089624110652551169.json, 视频生成/文生视频/海螺H3优化 小脸 打斗 浅空间_2091512771916681217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_116

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json、视频生成/文生视频/minimax_h3_r2v_video_edit视频编辑_2094267455395950594.json、视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json、视频生成/文生视频/人物真实低动态H3+sigma强化+潜空间放大工作流 双采_2096114490512330753.json、视频生成/文生视频/动漫短剧工作流（一键直出1080P竖屏短剧提示词未自动优化）_2093587306430160898.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 8/9 个有
- `MinimaxH3LatentUpscaler3D` —— 7/9 个有
- `ModelPreviewOverrideKJ` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `GetNode` —— 5/9 个有
- `H3SigmaRefiner` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `VHS_VideoCombine` —— 5/9 个有
- `ManualSigmas` —— 4/9 个有
- `LoadAudio` —— 2/9 个有
- `SolAttnMiniMax` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `MiniMaxH3ImageToVideo` —— 1/9 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/9 个有
- `MiniMaxLowVRAMAttention` —— 1/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
