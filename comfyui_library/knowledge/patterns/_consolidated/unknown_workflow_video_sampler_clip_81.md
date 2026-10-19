---
name: unknown_workflow_video_sampler_clip_81
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.942857
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSamplerSelect, LTXVBaseSampler, LTXVConditioning, LoadImage, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1947700858089783297.json, 视频生成/图生视频/1947702607479455746.json, 视频生成/图生视频/1921503421558620162.json, 视频生成/图生视频/1921491930432339969.json, 视频生成/图生视频/1921497557317402626.json, 视频生成/图生视频/1922465822680481794.json, 视频生成/图生视频/1920645310174138370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1947700858089783297.json、视频生成/图生视频/1947702607479455746.json、视频生成/图生视频/1921503421558620162.json、视频生成/图生视频/1921491930432339969.json、视频生成/图生视频/1921497557317402626.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSamplerSelect`
- `LTXVBaseSampler`
- `LTXVConditioning`
- `LoadImage`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 6/7 个有
- `LTXQ8Patch` —— 6/7 个有
- `LayerUtility: ImageAutoCrop V3` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `RH_Captioner` —— 6/7 个有
- `ImageConcanate` —— 5/7 个有
- `ImpactSwitch` —— 5/7 个有
- `JWImageResizeByLongerSide` —— 5/7 个有
- `Note Plus (mtb)` —— 5/7 个有
- `StringConstantMultiline` —— 5/7 个有
- `Text Concatenate` —— 5/7 个有
- `CR Prompt Text` —— 2/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `LTXVAdainLatent` —— 2/7 个有
- `LTXVFilmGrain` —— 2/7 个有
- `LTXVLatentUpsampler` —— 2/7 个有
- `LTXVLatentUpsamplerModelLoader` —— 2/7 个有
- `LTXVTiledSampler` —— 2/7 个有
- `SplitSigmas` —— 2/7 个有
- `VAEDecodeTiled` —— 2/7 个有
- `ImageBatch` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LTXVExtendSampler` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
