---
name: unknown_workflow_video_sampler_unet_59
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.872857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, ManualSigmas, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json, 视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json, 视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json, 视频生成/图生视频/minimax_h3_r2v_video_edit_2092169538497503233.json, 视频生成/图生视频/参考故事版生成视频 minimax H3_2092780996881113090.json, 视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json, 视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json、视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json、视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json、视频生成/图生视频/minimax_h3_r2v_video_edit_2092169538497503233.json、视频生成/图生视频/参考故事版生成视频 minimax H3_2092780996881113090.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
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
- `LoadImage` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `MinimaxH3LatentUpscaler3D` —— 6/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `Label (rgthree)` —— 3/7 个有
- `MuyeTextEditOutput` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `Float to Int` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `ShellAgentPluginOutputText` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `LoadVideo` —— 1/7 个有
- `MiniMaxH3ImageToVideo` —— 1/7 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
