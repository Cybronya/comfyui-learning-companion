---
name: text_to_image_lora_sampler_clip_63
type: Text To Image
frequency: 18
level: strong
coverage: 0.721778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json, 视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json, 视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json, 视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json, 视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json, 视频生成/图生视频/图生视频｜视频生视频多合一优化版极简风格｜MinimaxH3工作流_2089005300677439489.json, 视频生成/图生视频/奇妙地图旅游多参版｜MinimaxH3 RH版图生视频_2090275673238757378.json, 视频生成/图生视频/极简版MinimaxH3｜YZ金鱼图生视频一键生成_2094793540407742466.json, 视频生成/图生视频/极简版多合一工作流｜YZ金鱼 MinimaxH3图生视频直出_2091286836076441601.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3文生图生视频_2091611038503493634.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3视频生成_2091782867239129089.json, 视频生成/文生视频/MinimaxH3完美优化版｜文生图生视频高质量生成_2094586726764343297.json, 视频生成/文生视频/MinimaxH3极简多合一优化版｜文生视频视频生视频全搞定_2089379554887553025.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2090879047906717697.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2092393696179343362.json, 视频生成/文生视频/完美优化版｜MinimaxH3三模视频一键生成工作流_2094801305775726593.json, 视频生成/文生视频/文生视频视频生视频全搞定｜MinimaxH3极简多合一优化版工作流_2089009963904622593.json, 视频生成/文生视频/极简多合一｜Minimax H3全能参考文生图生视频工作流_2089473253059416065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json、视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json、视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json、视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json、视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 17/18 个有
- `孤海注释` —— 17/18 个有
- `LoadVideo` —— 16/18 个有
- `VHS_VideoCombine` —— 16/18 个有
- `ImageResizeKJv2` —— 14/18 个有
- `LoadAudio` —— 14/18 个有
- `GetNode` —— 13/18 个有
- `LTXVConcatAVLatent` —— 13/18 个有
- `ResolutionSelector` —— 13/18 个有
- `SetNode` —— 13/18 个有
- `VAEEncode` —— 13/18 个有
- `VAEEncodeAudio` —— 13/18 个有
- `easy cleanGpuUsed` —— 13/18 个有
- `LoadImage` —— 12/18 个有
- `Fast Groups Bypasser (rgthree)` —— 5/18 个有
- `CR Text` —— 3/18 个有
- `MiniMaxH3SigmaShift` —— 3/18 个有
- `BiRefNetRMBG` —— 2/18 个有
- `CreateVideo` —— 2/18 个有
- `Fast Groups Muter (rgthree)` —— 2/18 个有
- `Float` —— 2/18 个有
- `SaveVideo` —— 2/18 个有
- `LayerUtility: PurgeVRAM V2` —— 1/18 个有
- `MiniMaxH3TurboLoRA` —— 1/18 个有
- `MiniMaxH3TurboSampler` —— 1/18 个有
- `ModelAttentionBackend` —— 1/18 个有
- `Notif-PlaySound` —— 1/18 个有
- `PathchSageAttentionKJ` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有
- `ShellAgentPluginSaveAudios` —— 1/18 个有
- `Text` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
