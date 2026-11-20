---
name: unknown_workflow_video_lora_sampler_671
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [平台全量/MinimaxH3 全自动长视频&数字人_2101528217386573826.json, 数字人/数字人/H3数字人对口型_2094236378186993665.json, 视频生成/图生视频/H3数字人对口型_2092500387885576193.json, 视频生成/图生视频/MinimaxH3 全自动长视频&数字人_2101599345828261889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_671

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/MinimaxH3 全自动长视频&数字人_2101528217386573826.json、数字人/数字人/H3数字人对口型_2094236378186993665.json、视频生成/图生视频/H3数字人对口型_2092500387885576193.json、视频生成/图生视频/MinimaxH3 全自动长视频&数字人_2101599345828261889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `Float` —— 2/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `MiniMaxH3AddGuide` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ShowAnything|Mie` —— 2/4 个有
- `SoundFlow_GetLength` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
