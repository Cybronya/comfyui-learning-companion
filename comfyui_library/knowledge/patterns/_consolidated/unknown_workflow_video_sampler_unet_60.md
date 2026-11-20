---
name: unknown_workflow_video_sampler_unet_60
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8446
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3口型同步_2086253656294383617.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2087735816637468673.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2090009910481342465.json, 视频生成/文生视频/fengjing_2095750565702750210.json, 视频生成/文生视频/fengjing_2099671218269016065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3口型同步_2086253656294383617.json、视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2087735816637468673.json、视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2090009910481342465.json、视频生成/文生视频/fengjing_2095750565702750210.json、视频生成/文生视频/fengjing_2099671218269016065.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 4/5 个有
- `SoundFlow_GetLength` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `Int` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `PrimitiveString` —— 2/5 个有
- `Text` —— 2/5 个有
- `ZML_MergeText` —— 2/5 个有
- `DF_Int_to_Float` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `GetAudioDurationFromAudio` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiniMaxH3BlockCacheT8` —— 1/5 个有
- `SDVN Any Show` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
