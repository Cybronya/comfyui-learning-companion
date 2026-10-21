---
name: unknown_workflow_video_sampler_unet_45
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.882
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, ManualSigmas, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json, 视频生成/文生视频/minimax_h3_r2v_video_edit视频编辑_2094267455395950594.json, 视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json, 视频生成/文生视频/动漫短剧工作流（一键直出1080P竖屏短剧提示词未自动优化）_2093587306430160898.json, 视频生成/文生视频/（0825）二采放大1080P12秒-提示词未自动优化_2092123279141195777.json, 视频生成/文生视频/（0826）万象二采放大1080P横屏12秒-提示词未自动优化（增加动态lora）_2092578809114619905.json, 视频生成/文生视频/（0826）万象二采放大1080P竖屏12秒-提示词未自动优化（增加动态lora）_2092617053390856194.json, 视频生成/视频生视频/Minimax+H3+多参角色替换Lora，二采放大_2106244704005345281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_45

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json、视频生成/文生视频/minimax_h3_r2v_video_edit视频编辑_2094267455395950594.json、视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json、视频生成/文生视频/动漫短剧工作流（一键直出1080P竖屏短剧提示词未自动优化）_2093587306430160898.json、视频生成/文生视频/（0825）二采放大1080P12秒-提示词未自动优化_2092123279141195777.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3ReferenceToVideo` —— 7/8 个有
- `MinimaxH3LatentUpscaler3D` —— 7/8 个有
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `CreateVideo` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
