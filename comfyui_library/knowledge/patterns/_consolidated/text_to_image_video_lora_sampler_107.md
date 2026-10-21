---
name: text_to_image_video_lora_sampler_107
type: Text To Image
frequency: 7
level: strong
coverage: 0.648143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LoadAudio, LoadVideo, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/全能参考工作流｜H3文生图生视频多模态生成_2091594532889649153.json, 视频生成/文生视频/全能参考漫剧制作｜H3文生图生视频生视频_2091766009513467906.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2090879047906717697.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2092393696179343362.json, 视频生成/文生视频/完美优化版｜MinimaxH3三模视频一键生成工作流_2094801305775726593.json, 视频生成/文生视频/文生视频视频生视频全搞定｜MinimaxH3极简多合一优化版工作流_2089009963904622593.json, 视频生成/文生视频/极简多合一｜Minimax H3全能参考文生图生视频工作流_2089473253059416065.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/全能参考工作流｜H3文生图生视频多模态生成_2091594532889649153.json、视频生成/文生视频/全能参考漫剧制作｜H3文生图生视频生视频_2091766009513467906.json、视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2090879047906717697.json、视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2092393696179343362.json、视频生成/文生视频/完美优化版｜MinimaxH3三模视频一键生成工作流_2094801305775726593.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `VAEEncode` —— 5/7 个有
- `VAEEncodeAudio` —— 5/7 个有
- `MiniMaxH3SigmaShift` —— 4/7 个有
- `ExtendIntermediateSigmas` —— 2/7 个有
- `Float` —— 2/7 个有
- `H3LatentUpscaleByJingchen573` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `MinimaxH3LatentUpscaler3D` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
