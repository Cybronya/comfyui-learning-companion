---
name: text_to_image_lora_sampler_clip_34
type: Text To Image
frequency: 19
level: strong
coverage: 0.862263
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 All-in-One Accelerated V3 一体化加速视频工作流_2099231445800808450.json, 视频生成/文生视频/H3 All-in-One Accelerated V3一体化加速工作流_2099556074457231362.json, 视频生成/文生视频/H3八步二采视频｜文生图生视频生视频三模输出_2094567815121563650.json, 视频生成/文生视频/H3单采视频生成｜高质量文生图生视频工作流_2095961287233728513.json, 视频生成/文生视频/H3四步二采视频加速｜三模输出一键生成工作流_2094569314924974082.json, 视频生成/文生视频/H3模型视频生成工作流，文生视频图生视频单采方案_2103235249256886274.json, 视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3｜文图视频一体化全搞定_2099405729106055169.json, 视频生成/文生视频/MiniMax H3全能插件音频设计视频生成处理工作流_2101366594571169793.json, 视频生成/文生视频/MiniMax H3全能插件｜音频设计加持视频创作_2101173506313637890.json, 视频生成/文生视频/MiniMax H3多参Taomate 3步Lora二采视频生成处理工具_2101407475479179265.json, 视频生成/文生视频/MiniMax H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2106867673660485633.json, 视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json, 视频生成/文生视频/MinimaxH3文生视频双采样加速版｜文生视频提速_2090442867549499394.json, 视频生成/文生视频/h3 4步二采视频生成 文生视频加速高质量出片_2094239404528324609.json, 视频生成/文生视频/多参生视频潜空间放大二采｜Minimax H3高质量版_2095969486913495042.json, 视频生成/文生视频/多参生视频潜空间放大｜Minimax H3 二采画质更稳_2096260116558467073.json, 视频生成/文生视频/小脸不崩运动不糊｜H3高清优化版文生图生视频_2089773922295304193.json, 视频生成/文生视频/智能提示词优化｜海螺minimaxH3加速双采样高清放大工作流_2089801693700648962.json, 视频生成/文生视频/高清人脸｜海螺H3 sigma强化潜空间放大视频生成_2089812873718624257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/文生视频/H3 All-in-One Accelerated V3 一体化加速视频工作流_2099231445800808450.json、视频生成/文生视频/H3 All-in-One Accelerated V3一体化加速工作流_2099556074457231362.json、视频生成/文生视频/H3八步二采视频｜文生图生视频生视频三模输出_2094567815121563650.json、视频生成/文生视频/H3单采视频生成｜高质量文生图生视频工作流_2095961287233728513.json、视频生成/文生视频/H3四步二采视频加速｜三模输出一键生成工作流_2094569314924974082.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
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
- `BasicScheduler` —— 17/19 个有
- `MiniMaxH3SigmaShift` —— 15/19 个有
- `VHS_VideoCombine` —— 15/19 个有
- `LTXVConcatAVLatent` —— 14/19 个有
- `LTXVSeparateAVLatent` —— 14/19 个有
- `H3SigmaRefiner` —— 12/19 个有
- `SplitSigmas` —— 12/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/19 个有
- `MiniMaxH3Unified` —— 11/19 个有
- `CR Text` —— 10/19 个有
- `ComfyMathExpression` —— 10/19 个有
- `LoadImage` —— 10/19 个有
- `MiniMaxH3ReferenceToVideo` —— 10/19 个有
- `MinimaxH3LatentUpscaler3D` —— 10/19 个有
- `PrimitiveFloat` —— 10/19 个有
- `VAEDecodeAudio` —— 10/19 个有
- `MiniMaxH3AVDecodeT8` —— 9/19 个有
- `CreateVideo` —— 7/19 个有
- `SaveVideo` —— 7/19 个有
- `SaveImage` —— 6/19 个有
- `SolAttnMiniMax` —— 6/19 个有
- `ManualSigmas` —— 5/19 个有
- `Text` —— 5/19 个有
- `Fast Groups Bypasser (rgthree)` —— 4/19 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/19 个有
- `PrimitiveStringMultiline` —— 4/19 个有
- `GetNode` —— 3/19 个有
- `SetNode` —— 3/19 个有
- `ClownsharKSampler_Beta` —— 2/19 个有
- `ConditioningZeroOut` —— 2/19 个有
- `Label (rgthree)` —— 2/19 个有
- `SeedGenerator` —— 2/19 个有
- `ImageResizeKJv2` —— 1/19 个有
- `PathchSageAttentionKJ` —— 1/19 个有
- `ShowText|pysssss` —— 1/19 个有
- `StariAI-MiniMaxH3-Skill` —— 1/19 个有
- `VHS_LoadVideo` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足
