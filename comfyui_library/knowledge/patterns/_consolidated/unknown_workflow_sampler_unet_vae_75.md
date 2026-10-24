---
name: unknown_workflow_sampler_unet_vae_75
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.76875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimaxh3 数字人_2089195997028249601.json, 视频生成/图生视频/video_minimax_h3_r2v_2084181079887536129.json, 视频生成/图生视频/video_minimax_h3_r2v_2084534320714313730.json, 视频生成/图生视频/video_minimax_h3_r2v_turbo 多参加速_2100758868111486978.json, 视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json, 视频生成/图生视频/【开源】minimax_h3 参考生视频加速版_2085966231420628993.json, 视频生成/图生视频/【开源】minimax_h3 图生视频加速版_2085932065148719105.json, 视频生成/图生视频/【开源】minimax_h3 音频参考生MV_2084184318896857090.json, 视频生成/文生视频/MINIMAX-H3-多参考生视频_2084144392893452289.json, 视频生成/文生视频/Minimax H3多参视频生成+全节点注释_2084873538615472129.json, 视频生成/文生视频/video_minimax_h3_r2v_fast_2094242970009694209.json, 视频生成/文生视频/音频裁剪驱动MiniMax H3数字人-单图版_2090380497007501314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_75

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/minimaxh3 数字人_2089195997028249601.json、视频生成/图生视频/video_minimax_h3_r2v_2084181079887536129.json、视频生成/图生视频/video_minimax_h3_r2v_2084534320714313730.json、视频生成/图生视频/video_minimax_h3_r2v_turbo 多参加速_2100758868111486978.json、视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 10/12 个有
- `PrimitiveStringMultiline` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `CreateVideo` —— 7/12 个有
- `PathchSageAttentionKJ` —— 7/12 个有
- `SaveVideo` —— 7/12 个有
- `LoadAudio` —— 6/12 个有
- `VHS_VideoCombine` —— 5/12 个有
- `EasyCache` —— 4/12 个有
- `TrimAudioDuration` —— 4/12 个有
- `SolAttnPatch` —— 3/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/12 个有
- `MiniMaxH3TurboLoRA` —— 2/12 个有
- `MiniMaxH3TurboSampler` —— 2/12 个有
- `Text` —— 2/12 个有
- `VHS_LoadVideo` —— 2/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/12 个有
- `AudioCrop` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `SoundFlow_GetLength` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
