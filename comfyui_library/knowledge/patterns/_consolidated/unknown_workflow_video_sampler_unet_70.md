---
name: unknown_workflow_video_sampler_unet_70
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.852833
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/图生视频/xinlingjitang_2095332464360251393.json, 视频生成/图生视频/海螺H3(minimax H3)数字人单人加速开源版_2084869370685247490.json, 视频生成/图生视频/海螺H3(minimax H3)数字人单人语音克隆加速开源版_2084910413048795137.json, 视频生成/图生视频/海螺H3(minimax H3)数字人双人语音克隆（可多人）加速开源版_2084897123694366722.json, 视频生成/文生视频/fengjing_2095750565702750210.json, 视频生成/文生视频/fengjing_2099671218269016065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/xinlingjitang_2095332464360251393.json、视频生成/图生视频/海螺H3(minimax H3)数字人单人加速开源版_2084869370685247490.json、视频生成/图生视频/海螺H3(minimax H3)数字人单人语音克隆加速开源版_2084910413048795137.json、视频生成/图生视频/海螺H3(minimax H3)数字人双人语音克隆（可多人）加速开源版_2084897123694366722.json、视频生成/文生视频/fengjing_2095750565702750210.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
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
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/6 个有
- `Label (rgthree)` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `PrimitiveString` —— 3/6 个有
- `ResolutionSelector` —— 3/6 个有
- `Text` —— 3/6 个有
- `ZML_MergeText` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `Qwen3TTSModelLoader` —— 2/6 个有
- `Qwen3TTSVoiceClone` —— 2/6 个有
- `SaveAudio` —— 2/6 个有
- `WhisperSTT` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `AudioConcat` —— 1/6 个有
- `EmptyAudio` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `MiniMaxH3BlockCacheT8` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
