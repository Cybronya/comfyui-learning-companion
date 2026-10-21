---
name: unknown_workflow_video_sampler_clip_238
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.887
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ImageResizeKJ, KSamplerSelect, LTXVAdainLatent, LTXVConditioning, LTXVFilmGrain, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, LoadImage, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, SplitSigmas, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1921818761756622849.json, 视频生成/图生视频/1921808405055356929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_238

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1921818761756622849.json、视频生成/图生视频/1921808405055356929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LTXVAdainLatent`
- `LTXVConditioning`
- `LTXVFilmGrain`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVTiledSampler`
- `LoadImage`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `SplitSigmas`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `LTXVBaseSampler` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
