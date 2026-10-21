---
name: unknown_workflow_video_upscale_latent_upscale_25
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.572077
common_nodes: [ApplyFaceProcessor, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, EasyCache, FaceProcessorLoader, GetNode, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PathchSageAttentionKJ, PreviewImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedVR2, SeedVR2BlockSwap, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy float]
problems: []
missing: []
members: [数字人/数字人/shuzirenzhufu_2102658561401778178.json, 数字人/数字人/shuzirenzhufu_2102695078782398465.json, 视频生成/图生视频/shenxianzhufu1_2098356668814938114.json, 视频生成/图生视频/shenxianzhufu999_2100041027850694658.json, 视频生成/图生视频/shenxianzhufu999_2101172093047103489.json, 视频生成/图生视频/shenxianzhufu999_2101449854881976322.json, 视频生成/图生视频/shenxianzhufu_2095428965656780801.json, 视频生成/图生视频/shenxianzhufu_2097255575225716737.json, 视频生成/图生视频/shuzirenzhufu_2095069867983593473.json, 视频生成/图生视频/shuzirenzhufu_2097241522621214721.json, 视频生成/文生视频/MiniMax H3 图生音视频_2093999974961991682.json, 视频生成/文生视频/MiniMax H3 数字人参考音视频_2093973895530504193.json, 视频生成/文生视频/MiniMax H3 视频参考版（编辑替换等）_2093940095719141378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_25

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/shuzirenzhufu_2102658561401778178.json、数字人/数字人/shuzirenzhufu_2102695078782398465.json、视频生成/图生视频/shenxianzhufu1_2098356668814938114.json、视频生成/图生视频/shenxianzhufu999_2100041027850694658.json、视频生成/图生视频/shenxianzhufu999_2101172093047103489.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 13 个 workflow 都包含：
- `ApplyFaceProcessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `EasyCache`
- `FaceProcessorLoader`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 12/13 个有
- `LoadAudio` —— 12/13 个有
- `PrimitiveString` —— 12/13 个有
- `SoundFlow_GetLength` —— 12/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 12/13 个有
- `AILab_QwenVL` —— 10/13 个有
- `ZML_MergeText` —— 10/13 个有
- `ImageScale` —— 8/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `JjkText` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `Int` —— 1/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/13 个有
- `MiniMaxH3SigmaShift` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
