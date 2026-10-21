---
name: unknown_workflow_upscale_latent_upscale_lora_32
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7038
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json, 视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json, 视频生成/图生视频/minimax h3_fi2va-dasiwa-zs05可选单图双采_2092267502540779521.json, 视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json, 视频生成/图生视频/同模双采 H3 动态修复_2096940486610219009.json, 视频生成/文生视频/(0823修复）海螺H3 sigma强化+潜空间放大+高清人脸工作流_2091505787058348034.json, 视频生成/文生视频/H3 高清优化版-小脸不崩-运动不模糊_2089690104179810306.json, 视频生成/文生视频/啊癫 minimaxh3极速版二采潜空间直接放大（去油版）_2093957991434379265.json, 视频生成/文生视频/收藏级！H3 加速+二采+打斗全能工作流拆解系列05集_2092970619469123586.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json、视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json、视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json、视频生成/图生视频/minimax h3_fi2va-dasiwa-zs05可选单图双采_2092267502540779521.json、视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：70%

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
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `ModelPreviewOverrideKJ` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `SplitSigmas` —— 9/10 个有
- `H3SigmaRefiner` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `SaveVideo` —— 4/10 个有
- `SolAttnMiniMax` —— 4/10 个有
- `Label (rgthree)` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `MiniMaxH3ImageToVideo` —— 2/10 个有
- `MiniMaxH3TurboLoRA` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `easy int` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
