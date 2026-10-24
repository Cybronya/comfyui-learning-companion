---
name: unknown_workflow_video_sampler_unet_41
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8528
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3-对口型数字人_2086355727127498754.json, 视频生成/文生视频/MINIMAX-H3多参_2086757864504385537.json, 视频生成/文生视频/MiniMax H3-数字人_2086137653598179330.json, 视频生成/文生视频/MiniMax H3-数字人_2092346787918073857.json, 视频生成/文生视频/MiniMax_H3_数字人_双人版_2085223972794355714.json, 视频生成/文生视频/MinimaxH3数字人 音频驱动单人版_2095684640324538370.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2087735816637468673.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版_2090009910481342465.json, 视频生成/文生视频/音频裁剪驱动MiniMax H3数字人-双图版_2090485095252709377.json, 视频生成/文生视频/音频裁剪驱动MiniMax H3数字人-多图版_2090405026232619010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/H3-对口型数字人_2086355727127498754.json、视频生成/文生视频/MINIMAX-H3多参_2086757864504385537.json、视频生成/文生视频/MiniMax H3-数字人_2086137653598179330.json、视频生成/文生视频/MiniMax H3-数字人_2092346787918073857.json、视频生成/文生视频/MiniMax_H3_数字人_双人版_2085223972794355714.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 9/10 个有
- `AudioCrop` —— 8/10 个有
- `PathchSageAttentionKJ` —— 8/10 个有
- `SoundFlow_GetLength` —— 8/10 个有
- `AudioConcat` —— 3/10 个有
- `EmptyAudio` —— 3/10 个有
- `Label (rgthree)` —— 2/10 个有
- `AudioToFPS` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `VAEDecodeAudio` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
