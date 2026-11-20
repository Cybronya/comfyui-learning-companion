---
name: text_to_image_video_lora_sampler_51
type: Text To Image
frequency: 15
level: strong
coverage: 0.666
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LoadAudio, LoadVideo, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频｜视频生视频多合一优化版极简风格｜MinimaxH3工作流_2089005300677439489.json, 视频生成/图生视频/奇妙地图旅游多参版｜MinimaxH3 RH版图生视频_2090275673238757378.json, 视频生成/图生视频/极简版MinimaxH3｜YZ金鱼图生视频一键生成_2094793540407742466.json, 视频生成/图生视频/极简版多合一工作流｜YZ金鱼 MinimaxH3图生视频直出_2091286836076441601.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3文生图生视频_2091611038503493634.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3视频生成_2091782867239129089.json, 视频生成/文生视频/MinimaxH3完美优化版｜文生图生视频高质量生成_2094586726764343297.json, 视频生成/文生视频/MinimaxH3极简多合一优化版｜文生视频视频生视频全搞定_2089379554887553025.json, 视频生成/文生视频/MinimaxH3极简版多合一｜文生视频视频生视频_2095251267785420802.json, 视频生成/文生视频/全能参考工作流｜H3文生图生视频多模态生成_2091594532889649153.json, 视频生成/文生视频/全能参考漫剧制作｜H3文生图生视频生视频_2091766009513467906.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2090879047906717697.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2092393696179343362.json, 视频生成/文生视频/完美优化版｜MinimaxH3三模视频一键生成工作流_2094801305775726593.json, 视频生成/文生视频/文生视频视频生视频全搞定｜MinimaxH3极简多合一优化版工作流_2089009963904622593.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/图生视频｜视频生视频多合一优化版极简风格｜MinimaxH3工作流_2089005300677439489.json、视频生成/图生视频/奇妙地图旅游多参版｜MinimaxH3 RH版图生视频_2090275673238757378.json、视频生成/图生视频/极简版MinimaxH3｜YZ金鱼图生视频一键生成_2094793540407742466.json、视频生成/图生视频/极简版多合一工作流｜YZ金鱼 MinimaxH3图生视频直出_2091286836076441601.json、视频生成/文生视频/Easy极简工作台多参｜MiniMax H3文生图生视频_2091611038503493634.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 15 个 workflow 都包含：
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 14/15 个有
- `ImageResizeKJv2` —— 12/15 个有
- `ResolutionSelector` —— 12/15 个有
- `VAEEncode` —— 12/15 个有
- `VAEEncodeAudio` —— 12/15 个有
- `LoadImage` —— 10/15 个有
- `Fast Groups Bypasser (rgthree)` —— 6/15 个有
- `MiniMaxH3SigmaShift` —— 4/15 个有
- `LTXVSeparateAVLatent` —— 3/15 个有
- `MinimaxH3LatentUpscaler3D` —— 3/15 个有
- `ExtendIntermediateSigmas` —— 2/15 个有
- `Fast Groups Muter (rgthree)` —— 2/15 个有
- `Float` —— 2/15 个有
- `H3LatentUpscaleByJingchen573` —— 2/15 个有
- `PrimitiveFloat` —— 2/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `Text` —— 2/15 个有
- `easy showAnything` —— 2/15 个有
- `LayerUtility: PurgeVRAM V2` —— 1/15 个有
- `ModelPreviewOverrideKJ` —— 1/15 个有
- `Notif-PlaySound` —— 1/15 个有
- `RIFE VFI` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `ShellAgentPluginSaveAudios` —— 1/15 个有
- `SplitSigmas` —— 1/15 个有
- `workflow>声音` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
