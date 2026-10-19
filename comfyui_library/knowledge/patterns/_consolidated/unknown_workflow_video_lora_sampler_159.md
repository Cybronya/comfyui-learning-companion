---
name: unknown_workflow_video_lora_sampler_159
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.515545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 音频驱动数字人超分V13_2096777449806843906.json, 视频生成/图生视频/Minimax H3数字人（多人对话，漫剧必备）_2092508231217278978.json, 视频生成/图生视频/Minimax H3数字人（多人对话，漫剧必备）_2101516388136480769.json, 视频生成/图生视频/MinimaxH3 一键MV（单人数字人） 不限时长_2092508260711624706.json, 视频生成/图生视频/MinimaxH3-数字人(单人加速版)_2084976133631729665.json, 视频生成/图生视频/MinimaxH3-满血int8单采八部加速Sigma版V4_2092900303573180418.json, 视频生成/图生视频/音频驱动测试_2111325696218976257.json, 视频生成/文生视频/H3模型测试_singularity_2098910282218299394.json, 视频生成/文生视频/Minimax H3 文生图生参考万能超分V13_2096777434057236482.json, 视频生成/文生视频/minimaxH3+访谈类数字人_2097651536854863873.json, 视频生成/文生视频/minimaxH3数字人工作流（音色参考）_2094688876832055298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_159

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 音频驱动数字人超分V13_2096777449806843906.json、视频生成/图生视频/Minimax H3数字人（多人对话，漫剧必备）_2092508231217278978.json、视频生成/图生视频/Minimax H3数字人（多人对话，漫剧必备）_2101516388136480769.json、视频生成/图生视频/MinimaxH3 一键MV（单人数字人） 不限时长_2092508260711624706.json、视频生成/图生视频/MinimaxH3-数字人(单人加速版)_2084976133631729665.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `ModelPreviewOverrideKJ` —— 6/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 6/11 个有
- `PrimitiveStringMultiline` —— 5/11 个有
- `SoundFlow_GetLength` —— 5/11 个有
- `VAEDecodeAudio` —— 5/11 个有
- `VHS_LoadVideo` —— 5/11 个有
- `AudioCrop` —— 4/11 个有
- `Text` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `PathchSageAttentionKJ` —— 3/11 个有
- `PurgeVRAM_UTK` —— 3/11 个有
- `RTXVideoSuperResolution` —— 3/11 个有
- `TrimAudioDuration` —— 2/11 个有
- `H3SigmaRefiner` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
