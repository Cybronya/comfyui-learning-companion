---
name: unknown_workflow_video_sampler_clip_72
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.941875
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSamplerSelect, LTXVBaseSampler, LTXVConditioning, LoadImage, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/LTXV 13B高动态首尾帧优化版V1_1921482288666722305.json, 视频生成/图生视频/LTXV 0.98 平衡版图生视频双模式V1_1947700858089783297.json, 视频生成/图生视频/LTXV 0.98高动态首尾帧优化版V1_1947702607479455746.json, 视频生成/图生视频/LTXV 13B 图生视频潜空间放大（不炸显存）V1测试版_1921503421558620162.json, 视频生成/图生视频/LTXV 13B稳定优化版图生视频双模式V1_1921491930432339969.json, 视频生成/图生视频/Ltxv 13B Extend视频扩展优化稳定版（不炸显存）V2_1921497557317402626.json, 视频生成/图生视频/【LTXV 13B】图生视频稳定优化版_1922465822680481794.json, 视频生成/图生视频/图生视频+空间or时间放大(LTXVideo 13B 0.9.7)_1920645310174138370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/LTXV 13B高动态首尾帧优化版V1_1921482288666722305.json、视频生成/图生视频/LTXV 0.98 平衡版图生视频双模式V1_1947700858089783297.json、视频生成/图生视频/LTXV 0.98高动态首尾帧优化版V1_1947702607479455746.json、视频生成/图生视频/LTXV 13B 图生视频潜空间放大（不炸显存）V1测试版_1921503421558620162.json、视频生成/图生视频/LTXV 13B稳定优化版图生视频双模式V1_1921491930432339969.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
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
- `GetImageSizeAndCount` —— 7/8 个有
- `LayerUtility: ImageAutoCrop V3` —— 7/8 个有
- `ImageConcanate` —— 6/8 个有
- `JWImageResizeByLongerSide` —— 6/8 个有
- `LTXQ8Patch` —— 6/8 个有
- `LayerUtility: PurgeVRAM V2` —— 6/8 个有
- `Note Plus (mtb)` —— 6/8 个有
- `RH_Captioner` —— 6/8 个有
- `ImpactSwitch` —— 5/8 个有
- `StringConstantMultiline` —— 5/8 个有
- `Text Concatenate` —— 5/8 个有
- `CR Prompt Text` —— 3/8 个有
- `ImageBatch` —— 2/8 个有
- `ImageResizeKJ` —— 2/8 个有
- `LTXVAdainLatent` —— 2/8 个有
- `LTXVFilmGrain` —— 2/8 个有
- `LTXVLatentUpsampler` —— 2/8 个有
- `LTXVLatentUpsamplerModelLoader` —— 2/8 个有
- `LTXVTiledSampler` —— 2/8 个有
- `SplitSigmas` —— 2/8 个有
- `VAEDecodeTiled` —— 2/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `JWString` —— 1/8 个有
- `LTXVExtendSampler` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
