---
name: unknown_workflow_video_upscale_latent_upscale_149
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [BasicGuider, BasicScheduler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyOutput, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, SplitSigmas, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 邪修音频驱动_2097635867723653122.json, 视频生成/文生视频/MinimaxH3工作流多合一极简版（配套优化提示词直接@使用）_2096935267025379329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_149

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/minimax H3 邪修音频驱动_2097635867723653122.json、视频生成/文生视频/MinimaxH3工作流多合一极简版（配套优化提示词直接@使用）_2096935267025379329.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyMediaLoader`
- `MiniMaxH3EasyOutput`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/2 个有
- `easy float` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
