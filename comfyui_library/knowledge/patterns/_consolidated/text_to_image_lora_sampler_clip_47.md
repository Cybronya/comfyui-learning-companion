---
name: text_to_image_lora_sampler_clip_47
type: Text To Image
frequency: 19
level: strong
coverage: 0.716474
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json, 视频生成/图生视频/Minimax H3单图生视频｜极速15秒直出1080P高清成片_2108394651400105985.json, 视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换｜1080高画质服装替换全注释_2089453564925136898.json, 视频生成/图生视频/MinimaxH3 Easy角色服装替换动作迁移｜1080高画质全节点注释视频生视频_2089719236200583170.json, 视频生成/图生视频/MinimaxH3视频生成工作台 支持图片参考多图创作_2098713051313819650.json, 视频生成/图生视频/MinimaxH3视频生成工作台｜支持@图片直接驱动_2098702232026963970.json, 视频生成/图生视频/图生视频｜视频生视频多合一优化版极简风格｜MinimaxH3工作流_2089005300677439489.json, 视频生成/图生视频/奇妙地图旅游多参版｜MinimaxH3 RH版图生视频_2090275673238757378.json, 视频生成/图生视频/极简版多合一工作流｜YZ金鱼 MinimaxH3图生视频直出_2091286836076441601.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3文生图生视频_2091611038503493634.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3视频生成_2091782867239129089.json, 视频生成/文生视频/MinimaxH3完美优化版｜文生图生视频高质量生成_2094586726764343297.json, 视频生成/文生视频/MinimaxH3极简多合一优化版｜文生视频视频生视频全搞定_2089379554887553025.json, 视频生成/文生视频/MinimaxH3极简版多合一｜文生视频视频生视频_2095251267785420802.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2090879047906717697.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2092393696179343362.json, 视频生成/文生视频/完美优化版｜MinimaxH3三模视频一键生成工作流_2094801305775726593.json, 视频生成/文生视频/文生视频视频生视频全搞定｜MinimaxH3极简多合一优化版工作流_2089009963904622593.json, 视频生成/文生视频/极简多合一｜Minimax H3全能参考文生图生视频工作流_2089473253059416065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json、视频生成/图生视频/Minimax H3单图生视频｜极速15秒直出1080P高清成片_2108394651400105985.json、视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换｜1080高画质服装替换全注释_2089453564925136898.json、视频生成/图生视频/MinimaxH3 Easy角色服装替换动作迁移｜1080高画质全节点注释视频生视频_2089719236200583170.json、视频生成/图生视频/MinimaxH3视频生成工作台 支持图片参考多图创作_2098713051313819650.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 18/19 个有
- `MiniMaxH3EasyLoader` —— 18/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/19 个有
- `VHS_VideoCombine` —— 17/19 个有
- `LoadAudio` —— 16/19 个有
- `LoadVideo` —— 16/19 个有
- `GetNode` —— 15/19 个有
- `LTXVConcatAVLatent` —— 15/19 个有
- `SetNode` —— 15/19 个有
- `ImageResizeKJv2` —— 12/19 个有
- `ResolutionSelector` —— 12/19 个有
- `VAEEncode` —— 12/19 个有
- `VAEEncodeAudio` —— 12/19 个有
- `easy cleanGpuUsed` —— 12/19 个有
- `LoadImage` —— 10/19 个有
- `Fast Groups Bypasser (rgthree)` —— 5/19 个有
- `LTXVSeparateAVLatent` —— 3/19 个有
- `MinimaxH3LatentUpscaler3D` —— 3/19 个有
- `SplitSigmas` —— 3/19 个有
- `CR Text` —— 2/19 个有
- `CreateVideo` —— 2/19 个有
- `Fast Groups Muter (rgthree)` —— 2/19 个有
- `Float` —— 2/19 个有
- `MiniMaxH3SigmaShift` —— 2/19 个有
- `MiniMaxH3TurboLoRA` —— 2/19 个有
- `ModelAttentionBackend` —— 2/19 个有
- `SaveImage` —— 2/19 个有
- `SaveVideo` —— 2/19 个有
- `Text` —— 2/19 个有
- `MiniMaxH3EasyModelAdapter` —— 1/19 个有
- `MiniMaxH3TurboSampler` —— 1/19 个有
- `ModelPreviewOverrideKJ` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `SpectrumApplyMiniMaxH3` —— 1/19 个有
- `workflow>声音` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足
