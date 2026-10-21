---
name: text_to_image_video_lora_sampler_113
type: Text To Image
frequency: 6
level: strong
coverage: 0.7055
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedNode, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3角色替换参考到视频工作流，视频生视频图生视频处理方案_2107178414863118337.json, 视频生成/图生视频/MiniMax_H3角色替换参考到视频工作流，视频生视频图生视频处理方案_2109458240017879041.json, 视频生成/图生视频/MinimaxH3 R2V 2Stage VEDA加速视频生成工作流 视频生成加速_2109759397407846402.json, 视频生成/图生视频/Minimax_H3_Character_Swap角色替换｜参考到视频工作流_2106983200139599874.json, 视频生成/文生视频/H3面部精修图生视频工作流 人物面部细节优化_2099910439055482882.json, 视频生成/文生视频/图生视频｜MinimaxH3 R2V面部精修版，人像细节更自然_2099873159469158401.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3角色替换参考到视频工作流，视频生视频图生视频处理方案_2107178414863118337.json、视频生成/图生视频/MiniMax_H3角色替换参考到视频工作流，视频生视频图生视频处理方案_2109458240017879041.json、视频生成/图生视频/MinimaxH3 R2V 2Stage VEDA加速视频生成工作流 视频生成加速_2109759397407846402.json、视频生成/图生视频/Minimax_H3_Character_Swap角色替换｜参考到视频工作流_2106983200139599874.json、视频生成/文生视频/H3面部精修图生视频工作流 人物面部细节优化_2099910439055482882.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedNode`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `MMH3LatentUpscaleWithModelParams` —— 4/6 个有
- `MMH3SpatialSplitParams` —— 4/6 个有
- `MMH3TemporalSplitParams` —— 4/6 个有
- `MMH3UltimateUpscale` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `VAEDecodeTiled` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `easy clearCacheAll` —— 4/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `StringConcatenate` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `H3FaceStitch` —— 2/6 个有
- `H3FaceTrackCrop` —— 2/6 个有
- `H3InjectVideoLatent` —— 2/6 个有
- `H3PerFrameDenoise` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `VedaSparseAttention` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
