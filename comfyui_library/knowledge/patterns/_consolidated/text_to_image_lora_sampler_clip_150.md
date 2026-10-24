---
name: text_to_image_lora_sampler_clip_150
type: Text To Image
frequency: 11
level: strong
coverage: 0.869
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json, 视频生成/文生视频/H3六步文生视频短片预检版｜六步走完从想法到成片_2099146163709628418.json, 视频生成/文生视频/H3文生视频加速版 官方Turbo加速出片_2099594371384561665.json, 视频生成/文生视频/H3高动态打斗场景武术动作二采修复 提示词增强工作流_2099919995085086722.json, 视频生成/文生视频/LightX2V Turbo加速｜MiniMax H3文生图生视频生视频工作流_2087187099337445378.json, 视频生成/文生视频/MiniMax H3 Easy Hybrid全能参考极简多合一工作流，文生视频图生视频方案_2105737236565282818.json, 视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json, 视频生成/文生视频/MiniMax H3 FL2VA文生首尾帧全能视频｜文生视频视频生视频图生视频_2090423722896347138.json, 视频生成/文生视频/低动态真实感人物视频｜H3 sigma强化潜空间双采_2096336928575680513.json, 视频生成/文生视频/多参数视频生成768p｜Minimax H3加速LoRA两步_2095964673219846146.json, 视频生成/文生视频/多合一生视频V3.0｜Minimax H3文生首尾图参二采高清放大_2090209607414276097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json、视频生成/文生视频/H3六步文生视频短片预检版｜六步走完从想法到成片_2099146163709628418.json、视频生成/文生视频/H3文生视频加速版 官方Turbo加速出片_2099594371384561665.json、视频生成/文生视频/H3高动态打斗场景武术动作二采修复 提示词增强工作流_2099919995085086722.json、视频生成/文生视频/LightX2V Turbo加速｜MiniMax H3文生图生视频生视频工作流_2087187099337445378.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `ComfyMathExpression` —— 7/11 个有
- `PrimitiveFloat` —— 7/11 个有
- `ResolutionSelector` —— 7/11 个有
- `LoadImage` —— 6/11 个有
- `MiniMaxH3SigmaShift` —— 6/11 个有
- `PathchSageAttentionKJ` —— 5/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `LTXVConcatAVLatent` —— 4/11 个有
- `LTXVSeparateAVLatent` —— 4/11 个有
- `MiniMaxH3Easy` —— 4/11 个有
- `MiniMaxH3EasyLoader` —— 4/11 个有
- `MiniMaxH3EasyOutput` —— 4/11 个有
- `MiniMaxH3ImageToVideo` —— 4/11 个有
- `MiniMaxH3ReferenceToVideo` —— 4/11 个有
- `SaveImage` —— 4/11 个有
- `SplitSigmas` —— 4/11 个有
- `H3SigmaRefiner` —— 3/11 个有
- `ModelAttentionBackend` —— 3/11 个有
- `MiniMaxH3EasyMediaLoader` —— 2/11 个有
- `MinimaxH3LatentUpscaler3D` —— 2/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `DisableNoise` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `GetVideoComponents` —— 1/11 个有
- `LoadVideo` —— 1/11 个有
- `MiniMaxH3HybridLoader` —— 1/11 个有
- `Seed (rgthree)` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `忽略多组孤海` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
