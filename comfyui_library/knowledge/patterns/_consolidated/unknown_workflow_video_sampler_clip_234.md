---
name: unknown_workflow_video_sampler_clip_234
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVAdainLatent, LTXVConditioning, LTXVFilmGrain, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, RandomNoise, STGGuiderAdvanced, Set VAE Decoder Noise, VAEDecodeTiled, VAEEncode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/ltxv模型快速视频放大_1946193285667020801.json, 视频生成/图生视频/【老金驿站】LTXvideo-13b高清放大工作流_1921818761756622849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_234

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/ltxv模型快速视频放大_1946193285667020801.json、视频生成/图生视频/【老金驿站】LTXvideo-13b高清放大工作流_1921818761756622849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVAdainLatent`
- `LTXVConditioning`
- `LTXVFilmGrain`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVTiledSampler`
- `RandomNoise`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `VAEDecodeTiled`
- `VAEEncode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `FloatToSigmas` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `STGAdvancedPresets` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有
- `StringToFloatList` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
