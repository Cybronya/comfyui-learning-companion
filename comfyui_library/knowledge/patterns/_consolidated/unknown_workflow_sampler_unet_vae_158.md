---
name: unknown_workflow_sampler_unet_vae_158
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81725
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3口型同步_2086253656294383617.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2087735816637468673.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2090009910481342465.json, 视频生成/文生视频/音频裁剪驱动MiniMax H3数字人-单图版_2090380497007501314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3口型同步_2086253656294383617.json、视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2087735816637468673.json、视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2090009910481342465.json、视频生成/文生视频/音频裁剪驱动MiniMax H3数字人-单图版_2090380497007501314.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `SoundFlow_GetLength` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `PreviewAudio` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `GetAudioDurationFromAudio` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `SDVN Any Show` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
