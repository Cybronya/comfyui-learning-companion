---
name: unknown_workflow_video_upscale_latent_upscale_21
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.876154
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, ManualSigmas, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json, 视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json, 视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json, 视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json, 视频生成/图生视频/MiniMax FastH3 v2全能参考高清放大VSA加速生成_2099780057341456385.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成+2采放大_2099689978258345985.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成_2100766250199773186.json, 视频生成/图生视频/MiniMax-H3 ref2va单模型二采无编解码放大_2093541824198701058.json, 视频生成/图生视频/minimax h3_fi2va-dasiwa-zs05可选单图双采_2092267502540779521.json, 视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json, 视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json, 视频生成/文生视频/H3基础模式_10步+3步Latent Upscaler_2090818143013924865.json, 视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_21

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json、视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json、视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json、视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json、视频生成/图生视频/MiniMax FastH3 v2全能参考高清放大VSA加速生成_2099780057341456385.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 12/13 个有
- `ModelPreviewOverrideKJ` —— 11/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `MiniMaxH3ImageToVideo` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `MiniMaxH3ReferenceToVideo` —— 6/13 个有
- `SaveVideo` —— 6/13 个有
- `ImageResizeKJv2` —— 5/13 个有
- `Label (rgthree)` —— 4/13 个有
- `Fast Groups Muter (rgthree)` —— 3/13 个有
- `BlockSparseAttention` —— 2/13 个有
- `Float to Int` —— 2/13 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `PixaromaDuration` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `ShellAgentPluginOutputText` —— 2/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `LoadVideo` —— 1/13 个有
- `PixaromaSizes` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
