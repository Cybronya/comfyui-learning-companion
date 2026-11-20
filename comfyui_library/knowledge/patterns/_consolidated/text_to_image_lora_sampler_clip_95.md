---
name: text_to_image_lora_sampler_clip_95
type: Text To Image
frequency: 14
level: strong
coverage: 0.907357
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3八步二采视频｜文生图生视频生视频三模输出_2094567815121563650.json, 视频生成/文生视频/H3单采视频生成｜高质量文生图生视频工作流_2095961287233728513.json, 视频生成/文生视频/H3四步二采视频加速｜三模输出一键生成工作流_2094569314924974082.json, 视频生成/文生视频/H3模型视频生成工作流，文生视频图生视频单采方案_2103235249256886274.json, 视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3｜文图视频一体化全搞定_2099405729106055169.json, 视频生成/文生视频/MiniMax H3全能插件音频设计视频生成处理工作流_2101366594571169793.json, 视频生成/文生视频/MiniMax H3全能插件｜音频设计加持视频创作_2101173506313637890.json, 视频生成/文生视频/MiniMax H3多参Taomate 3步Lora二采视频生成处理工具_2101407475479179265.json, 视频生成/文生视频/MiniMax H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2106867673660485633.json, 视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json, 视频生成/文生视频/MinimaxH3文生视频双采样加速版｜文生视频提速_2090442867549499394.json, 视频生成/文生视频/Ref2VA多参考全能生成｜MiniMax H3文生图生视频工作流_2093072782388187137.json, 视频生成/文生视频/Ref2VA多参考｜MiniMax H3全能视频生成直出_2090570005984407553.json, 视频生成/文生视频/多参考全能生成｜MiniMax H3 Ref2VA视频处理_2093230903848947714.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/H3八步二采视频｜文生图生视频生视频三模输出_2094567815121563650.json、视频生成/文生视频/H3单采视频生成｜高质量文生图生视频工作流_2095961287233728513.json、视频生成/文生视频/H3四步二采视频加速｜三模输出一键生成工作流_2094569314924974082.json、视频生成/文生视频/H3模型视频生成工作流，文生视频图生视频单采方案_2103235249256886274.json、视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3｜文图视频一体化全搞定_2099405729106055169.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 12/14 个有
- `MiniMaxH3SigmaShift` —— 12/14 个有
- `LTXVConcatAVLatent` —— 11/14 个有
- `LTXVSeparateAVLatent` —— 11/14 个有
- `ModelAttentionBackend` —— 11/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/14 个有
- `H3SigmaRefiner` —— 9/14 个有
- `MinimaxH3LatentUpscaler3D` —— 9/14 个有
- `SplitSigmas` —— 9/14 个有
- `VHS_VideoCombine` —— 9/14 个有
- `ComfyMathExpression` —— 8/14 个有
- `LoadImage` —— 8/14 个有
- `MiniMaxH3ReferenceToVideo` —— 8/14 个有
- `MiniMaxH3Unified` —— 8/14 个有
- `PrimitiveFloat` —— 8/14 个有
- `VAEDecodeAudio` —— 8/14 个有
- `CR Text` —— 6/14 个有
- `CreateVideo` —— 6/14 个有
- `MiniMaxH3AVDecodeT8` —— 6/14 个有
- `SaveVideo` —— 6/14 个有
- `PrimitiveStringMultiline` —— 5/14 个有
- `SaveImage` —— 4/14 个有
- `VHS_LoadVideo` —— 4/14 个有
- `AudioCrop` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `LoadAudio` —— 3/14 个有
- `ManualSigmas` —— 3/14 个有
- `SolAttnMiniMax` —— 3/14 个有
- `StringFunction|pysssss` —— 3/14 个有
- `Text` —— 3/14 个有
- `easy showAnything` —— 3/14 个有
- `ClownsharKSampler_Beta` —— 2/14 个有
- `ConditioningZeroOut` —— 2/14 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/14 个有
- `SeedGenerator` —— 2/14 个有
- `ImageResizeKJv2` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
