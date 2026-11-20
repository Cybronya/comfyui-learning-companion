---
name: unknown_workflow_video_lora_sampler_358
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.441143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3-多参生视频_2099054818437459969.json, 视频生成/图生视频/MiniMaxH3-多参生视频_2099773384988127233.json, 视频生成/图生视频/MiniMaxH3-多参生视频_2100033508268920833.json, 视频生成/图生视频/Minimax H3 N宫格视频_2098678084865183745.json, 视频生成/图生视频/【AI影视剧制作】MiniMaxH3-多参视频生成发布版_2109119782388846593.json, 视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json, 视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_358

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3-多参生视频_2099054818437459969.json、视频生成/图生视频/MiniMaxH3-多参生视频_2099773384988127233.json、视频生成/图生视频/MiniMaxH3-多参生视频_2100033508268920833.json、视频生成/图生视频/Minimax H3 N宫格视频_2098678084865183745.json、视频生成/图生视频/【AI影视剧制作】MiniMaxH3-多参视频生成发布版_2109119782388846593.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 6/7 个有
- `MiniMaxChunkFeedForward` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `JWFloat` —— 4/7 个有
- `MiniMaxH3AVLatentSeparateT8` —— 4/7 个有
- `MinimaxH3LatentUpscaler3D` —— 4/7 个有
- `PT_H3ConcatAVLatent` —— 4/7 个有
- `SplitSigmas` —— 4/7 个有
- `VHS_LoadAudioUpload` —— 4/7 个有
- `VRAM_Debug` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `LoadAudio` —— 3/7 个有
- `ModelPreviewOverrideKJ` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `ModelAttentionBackend` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `Float` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `MiniMaxH3AddGuide` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
