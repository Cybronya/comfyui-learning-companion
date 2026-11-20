---
name: unknown_workflow_video_sampler_clip_45
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.847455
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ImageResizeKJ, KSamplerSelect, LTXVAdainLatent, LTXVBaseSampler, LTXVConditioning, LTXVFilmGrain, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, LoadImage, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, SplitSigmas, VAEDecode, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705.json, 视频生成/图生视频/3图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921462278720520193.json, 视频生成/图生视频/4图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921473560848826369.json, 视频生成/图生视频/LTXV 0.9.7 13B 关键帧工作流_1921533815024467970.json, 视频生成/图生视频/ltxv-13b-i2v-base-fp8快速图生视频_1921753494003580929.json, 视频生成/图生视频/ltxv-13b-i2v-base图生视频+视频扩展_1921820658055987202.json, 视频生成/图生视频/图生视频-极速视频模型_1932368419218190337.json, 视频生成/图生视频/最新LTXV13B图生视频-极速视频模型_1920144851361533954.json, 视频生成/图生视频/最新LTXV13B多段分镜续写扩展_1920634402723008514.json, 视频生成/图生视频/最新LTXV13B首尾帧-多帧控制_1921825249476935682.json, 视频生成/图生视频/最新LTXV13B首尾帧控制(可多帧)_1920639676355379202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/2图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921088284032712705.json、视频生成/图生视频/3图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921462278720520193.json、视频生成/图生视频/4图首尾帧+空间or时间放大(LTXVideo 13B 0.9.7)_1921473560848826369.json、视频生成/图生视频/LTXV 0.9.7 13B 关键帧工作流_1921533815024467970.json、视频生成/图生视频/ltxv-13b-i2v-base-fp8快速图生视频_1921753494003580929.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ImageBatch` —— 9/11 个有
- `LTXVPromptEnhancer` —— 7/11 个有
- `LTXVPromptEnhancerLoader` —— 7/11 个有
- `Text Concatenate (JPS)` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `LayerUtility: PurgeVRAM` —— 6/11 个有
- `LTXVExtendSampler` —— 5/11 个有
- `Text Multiline` —— 5/11 个有
- `LTXQ8Patch` —— 4/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `JWInteger` —— 3/11 个有
- `LayerUtility: PurgeVRAM V2` —— 3/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `easy int` —— 3/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
