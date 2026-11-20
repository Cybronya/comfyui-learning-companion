---
name: unknown_workflow_video_sampler_clip_294
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ImageResizeKJ, KSamplerSelect, LTXVAdainLatent, LTXVBaseSampler, LTXVConditioning, LTXVFilmGrain, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, SplitSigmas, VAEDecode, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/最新LTXViedo-13B IV2 极速图生视频模型动态增强稳定高清放大-StarAI_1921808405055356929.json, 视频生成/文生视频/LTXV 0.97 13B（图生视频&首尾帧）_1922462563945107457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_294

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/最新LTXViedo-13B IV2 极速图生视频模型动态增强稳定高清放大-StarAI_1921808405055356929.json、视频生成/文生视频/LTXV 0.97 13B（图生视频&首尾帧）_1922462563945107457.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LTXVAdainLatent`
- `LTXVBaseSampler`
- `LTXVConditioning`
- `LTXVFilmGrain`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVTiledSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `SplitSigmas`
- `VAEDecode`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VideoCombine_Adv` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
