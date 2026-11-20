---
name: unknown_workflow_video_lora_sampler_147
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.906643
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, H3SigmaRefiner, ImageFromBatch, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByShorterEdge, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/海螺H3_人物替换专用流v1.5_2113448330415140866.json, 图片生成/图生图/海螺H3_人物替换专用流v1.5_2114638887707561986.json, 图片生成/图生图/海螺H3_人物替换专用流v1.5_2115297585513717762.json, 平台全量/H3人物替换专用流v1.5_整理_2113195063688908801.json, 平台全量/MINIMAX-H3 动作迁移，人物替换_2087467565630185474.json, 平台全量/MINIMAX-H3 动作迁移，人物替换_2118984204234092545.json, 平台全量/minimaxH3 人物替换_2115322147085307905.json, 平台全量/海螺H3 人物替换专用流v2.5_2109427848829300738.json, 数字人/数字人/MiNimax超写实人物替换丨动作迁移_2115414771980922881.json, 视频生成/图生视频/H3 人物替换专用流（村头东 二狗子流）_2109969385438932994.json, 视频生成/图生视频/MiniMax H3 超级人物替换专用工作流V3.0_2115634910269624321.json, 视频生成/图生视频/MiniMax_H3_超级人物替换专用工作流V3.0_2116043600340537346.json, 视频生成/图生视频/海螺H3_人物替换专用流v1.5_2113771024394309634.json, 视频生成/图生视频/海螺H3_人物替换专用流v1.5_2113784739583848450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/海螺H3_人物替换专用流v1.5_2113448330415140866.json、图片生成/图生图/海螺H3_人物替换专用流v1.5_2114638887707561986.json、图片生成/图生图/海螺H3_人物替换专用流v1.5_2115297585513717762.json、平台全量/H3人物替换专用流v1.5_整理_2113195063688908801.json、平台全量/MINIMAX-H3 动作迁移，人物替换_2087467565630185474.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `H3SigmaRefiner`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByShorterEdge`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 13/14 个有
- `LTXVSeparateAVLatent` —— 13/14 个有
- `MinimaxH3LatentUpscaler3D` —— 13/14 个有
- `ModelAttentionBackend` —— 13/14 个有
- `ModelPreviewOverrideKJ` —— 13/14 个有
- `VAEDecodeAudio` —— 13/14 个有
- `Fast Groups Bypasser (rgthree)` —— 12/14 个有
- `VHS_VideoInfo` —— 12/14 个有
- `ImageExpandBatch+` —— 11/14 个有
- `MiniMaxH3AddGuide` —— 11/14 个有
- `TrimAudioDuration` —— 11/14 个有
- `VHS_LoadVideoFFmpeg` —— 11/14 个有
- `GetImageSize` —— 10/14 个有
- `ImageBatch` —— 10/14 个有
- `ImageBatchMulti` —— 10/14 个有
- `RepeatImageBatch` —— 10/14 个有
- `easy forLoopEnd` —— 10/14 个有
- `easy forLoopStart` —— 10/14 个有
- `AudioConcat` —— 9/14 个有
- `PreviewImage` —— 5/14 个有
- `EmptyImage` —— 4/14 个有
- `VHS_LoadVideo` —— 3/14 个有
- `easy showAnything` —— 2/14 个有
- `忽略多组孤海` —— 2/14 个有
- `LatentUpscaleModelLoader` —— 1/14 个有
- `MiniMaxH3LatentUpscaleWithModel` —— 1/14 个有
- `PathchSageAttentionKJ` —— 1/14 个有
- `VideoTemporalCrop` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
