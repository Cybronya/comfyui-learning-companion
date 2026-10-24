---
name: text_to_image_video_lora_sampler_36
type: Text To Image
frequency: 17
level: strong
coverage: 0.840882
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 All-in-One Accelerated V3 一体化加速视频工作流_2099231445800808450.json, 视频生成/文生视频/H3 All-in-One Accelerated V3一体化加速工作流_2099556074457231362.json, 视频生成/文生视频/H3八步二采视频｜文生图生视频生视频三模输出_2094567815121563650.json, 视频生成/文生视频/H3单采视频生成｜高质量文生图生视频工作流_2095961287233728513.json, 视频生成/文生视频/H3台词优化多合一极简版工作流 视频生成处理_2100665823122780162.json, 视频生成/文生视频/H3四步二采视频加速｜三模输出一键生成工作流_2094569314924974082.json, 视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json, 视频生成/文生视频/H3模型视频生成工作流，文生视频图生视频单采方案_2103235249256886274.json, 视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3｜文图视频一体化全搞定_2099405729106055169.json, 视频生成/文生视频/MiniMax H3全能插件音频设计视频生成处理工作流_2101366594571169793.json, 视频生成/文生视频/MiniMax H3全能插件｜音频设计加持视频创作_2101173506313637890.json, 视频生成/文生视频/MinimaxH3文生视频双采样加速版｜文生视频提速_2090442867549499394.json, 视频生成/文生视频/StarAI海螺MiniMaxH3智能提示词优化｜四步加速双采样高清放大文生视频_2090090942878535681.json, 视频生成/文生视频/h3 4步二采视频生成 文生视频加速高质量出片_2094239404528324609.json, 视频生成/文生视频/全能参考工作流｜H3文生图生视频多模态生成_2091594532889649153.json, 视频生成/文生视频/全能参考漫剧制作｜H3文生图生视频生视频_2091766009513467906.json, 视频生成/文生视频/智能提示词优化｜海螺minimaxH3加速双采样高清放大工作流_2089801693700648962.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/H3 All-in-One Accelerated V3 一体化加速视频工作流_2099231445800808450.json、视频生成/文生视频/H3 All-in-One Accelerated V3一体化加速工作流_2099556074457231362.json、视频生成/文生视频/H3八步二采视频｜文生图生视频生视频三模输出_2094567815121563650.json、视频生成/文生视频/H3单采视频生成｜高质量文生图生视频工作流_2095961287233728513.json、视频生成/文生视频/H3台词优化多合一极简版工作流 视频生成处理_2100665823122780162.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 15/17 个有
- `ModelPreviewOverrideKJ` —— 15/17 个有
- `ResolutionSelector` —— 13/17 个有
- `LTXVConcatAVLatent` —— 12/17 个有
- `LTXVSeparateAVLatent` —— 12/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/17 个有
- `CR Text` —— 11/17 个有
- `H3SigmaRefiner` —— 11/17 个有
- `MiniMaxH3SigmaShift` —— 11/17 个有
- `MiniMaxH3Unified` —— 11/17 个有
- `SplitSigmas` —— 10/17 个有
- `MiniMaxH3AVDecodeT8` —— 9/17 个有
- `MinimaxH3LatentUpscaler3D` —— 9/17 个有
- `VAEDecodeAudio` —— 8/17 个有
- `Fast Groups Bypasser (rgthree)` —— 7/17 个有
- `PrimitiveFloat` —— 6/17 个有
- `SaveImage` —— 6/17 个有
- `LoadImage` —— 5/17 个有
- `SolAttnMiniMax` —— 5/17 个有
- `ComfyMathExpression` —— 4/17 个有
- `GetNode` —— 4/17 个有
- `LoadVideo` —— 4/17 个有
- `MiniMaxH3Easy` —— 4/17 个有
- `MiniMaxH3EasyLoader` —— 4/17 个有
- `MiniMaxH3EasyOutput` —— 4/17 个有
- `MiniMaxH3ReferenceToVideo` —— 4/17 个有
- `PrimitiveStringMultiline` —— 4/17 个有
- `SetNode` —— 4/17 个有
- `ShowText|pysssss` —— 4/17 个有
- `MinimaxH3LatentUpscalerNode3D` —— 3/17 个有
- `ExtendIntermediateSigmas` —— 2/17 个有
- `H3LatentUpscaleByJingchen573` —— 2/17 个有
- `LoadAudio` —— 2/17 个有
- `MiniMaxH3EasyMediaLoader` —— 2/17 个有
- `PathchSageAttentionKJ` —— 2/17 个有
- `StariAI-MiniMaxH3-Skill` —— 2/17 个有
- `easy cleanGpuUsed` —— 2/17 个有
- `easy showAnything` —— 2/17 个有
- `Label (rgthree)` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
