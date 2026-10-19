---
name: text_to_image_video_lora_sampler_14
type: Text To Image
frequency: 24
level: strong
coverage: 0.6625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadAudio, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/FASHION walk动作迁移自用版｜视频生视频图生视频 时装走秀利器_2104028785950679042.json, 视频生成/图生视频/FASHION走秀动作迁移 时装步态视频生成质感在线_2104304709061402625.json, 视频生成/图生视频/H3极简版多合一工作流 轻量化图生视频处理_2100280029207949314.json, 视频生成/图生视频/Minimax H3开源版极简版多图多声音参考工作流 多模态输入_2109361043150565377.json, 视频生成/图生视频/MinimaxH3奇妙地图旅游多参版｜RH版本图生视频_2090452977030090754.json, 视频生成/图生视频/MinimaxH3极简多合一短剧｜图生视频超好用工作流_2089446695401771010.json, 视频生成/图生视频/MinimaxH3极简版多合一图生视频工作流_2088187341377728514.json, 视频生成/图生视频/MinimaxH3极简版多合一工作流 视频生成一站式方案_2109386311500128258.json, 视频生成/图生视频/MinimaxH3极简版多合一工作流 视频生成一站式方案_2109753123161075714.json, 视频生成/图生视频/MinimaxH3极简版工作流｜一键图生视频生成_2094547962402795522.json, 视频生成/图生视频/MinimaxH3视频生成工作台 支持图片参考多图创作_2098713051313819650.json, 视频生成/图生视频/图生视频｜视频生视频多合一优化版极简风格｜MinimaxH3工作流_2089005300677439489.json, 视频生成/图生视频/奇妙地图旅游多参版｜MinimaxH3 RH版图生视频_2090275673238757378.json, 视频生成/图生视频/极简版MinimaxH3｜YZ金鱼图生视频一键生成_2094793540407742466.json, 视频生成/图生视频/极简版多合一工作流｜YZ金鱼 MinimaxH3图生视频直出_2091286836076441601.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3文生图生视频_2091611038503493634.json, 视频生成/文生视频/Easy极简工作台多参｜MiniMax H3视频生成_2091782867239129089.json, 视频生成/文生视频/MinimaxH3完美优化版｜文生图生视频高质量生成_2094586726764343297.json, 视频生成/文生视频/MinimaxH3极简多合一优化版｜文生视频视频生视频全搞定_2089379554887553025.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2090879047906717697.json, 视频生成/文生视频/全能参考漫剧工作流｜Minimax H3文生图生视频_2092393696179343362.json, 视频生成/文生视频/完美优化版｜MinimaxH3三模视频一键生成工作流_2094801305775726593.json, 视频生成/文生视频/文生视频视频生视频全搞定｜MinimaxH3极简多合一优化版工作流_2089009963904622593.json, 视频生成/文生视频/极简多合一｜Minimax H3全能参考文生图生视频工作流_2089473253059416065.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/FASHION walk动作迁移自用版｜视频生视频图生视频 时装走秀利器_2104028785950679042.json、视频生成/图生视频/FASHION走秀动作迁移 时装步态视频生成质感在线_2104304709061402625.json、视频生成/图生视频/H3极简版多合一工作流 轻量化图生视频处理_2100280029207949314.json、视频生成/图生视频/Minimax H3开源版极简版多图多声音参考工作流 多模态输入_2109361043150565377.json、视频生成/图生视频/MinimaxH3奇妙地图旅游多参版｜RH版本图生视频_2090452977030090754.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 23/24 个有
- `ImageResizeKJv2` —— 22/24 个有
- `LTXVConcatAVLatent` —— 22/24 个有
- `LoadVideo` —— 22/24 个有
- `ResolutionSelector` —— 22/24 个有
- `VAEEncode` —— 22/24 个有
- `VAEEncodeAudio` —— 22/24 个有
- `easy cleanGpuUsed` —— 22/24 个有
- `LoadImage` —— 17/24 个有
- `Text` —— 7/24 个有
- `SaveImage` —— 6/24 个有
- `Fast Groups Bypasser (rgthree)` —— 5/24 个有
- `Float` —— 3/24 个有
- `Fast Groups Muter (rgthree)` —— 2/24 个有
- `LTXVSeparateAVLatent` —— 2/24 个有
- `LayerUtility: PurgeVRAM V2` —— 2/24 个有
- `MiniMaxChunkFeedForward` —— 2/24 个有
- `MiniMaxH3SigmaShift` —— 2/24 个有
- `MiniMaxLowVRAMAttention` —— 2/24 个有
- `MinimaxH3LatentUpscaler3D` —— 2/24 个有
- `ModelAttentionBackend` —— 2/24 个有
- `Notif-PlaySound` —— 2/24 个有
- `PT_H3ConcatAVLatent` —— 2/24 个有
- `PrimitiveStringMultiline` —— 2/24 个有
- `RIFE VFI` —— 2/24 个有
- `ShellAgentPluginSaveAudios` —— 2/24 个有
- `SplitSigmas` —— 2/24 个有
- `EmptyImage` —— 1/24 个有
- `PreviewImage` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（26/24 个样本）：Steps较低可能导致细节不足
