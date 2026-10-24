---
name: text_to_image_video_lora_sampler_48
type: Text To Image
frequency: 13
level: strong
coverage: 0.718538
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多合一极简工作流 MiniMax H3 短剧创作人物替换视频风格转换 Dasiwa可选_2094162754230898689.json, 数字人/数字人/MinimaxH3多合一极简版｜配套优化提示词直接用｜数字人角色表演一步到位_2104765994072891393.json, 视频生成/图生视频/FASHION walk动作迁移自用版｜视频生视频图生视频 时装走秀利器_2104028785950679042.json, 视频生成/图生视频/FASHION走秀动作迁移 时装步态视频生成质感在线_2104304709061402625.json, 视频生成/图生视频/H3极简版多合一工作流 轻量化图生视频处理_2100280029207949314.json, 视频生成/图生视频/Minimax H3开源版极简版多图多声音参考工作流 多模态输入_2109361043150565377.json, 视频生成/图生视频/MinimaxH3奇妙地图旅游多参版｜RH版本图生视频_2090452977030090754.json, 视频生成/图生视频/MinimaxH3极简多合一短剧｜图生视频超好用工作流_2089446695401771010.json, 视频生成/图生视频/MinimaxH3极简版多合一图生视频工作流_2088187341377728514.json, 视频生成/图生视频/MinimaxH3极简版多合一工作流 视频生成一站式方案_2109386311500128258.json, 视频生成/图生视频/MinimaxH3极简版多合一工作流 视频生成一站式方案_2109753123161075714.json, 视频生成/图生视频/MinimaxH3极简版工作流｜一键图生视频生成_2094547962402795522.json, 视频生成/图生视频/极简版MinimaxH3｜YZ金鱼图生视频一键生成_2094793540407742466.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/多合一极简工作流 MiniMax H3 短剧创作人物替换视频风格转换 Dasiwa可选_2094162754230898689.json、数字人/数字人/MinimaxH3多合一极简版｜配套优化提示词直接用｜数字人角色表演一步到位_2104765994072891393.json、视频生成/图生视频/FASHION walk动作迁移自用版｜视频生视频图生视频 时装走秀利器_2104028785950679042.json、视频生成/图生视频/FASHION走秀动作迁移 时装步态视频生成质感在线_2104304709061402625.json、视频生成/图生视频/H3极简版多合一工作流 轻量化图生视频处理_2100280029207949314.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 12/13 个有
- `GetNode` —— 11/13 个有
- `ImageResizeKJv2` —— 11/13 个有
- `LTXVConcatAVLatent` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/13 个有
- `SetNode` —— 11/13 个有
- `VAEEncode` —— 11/13 个有
- `VAEEncodeAudio` —— 11/13 个有
- `easy cleanGpuUsed` —— 11/13 个有
- `LoadVideo` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `LoadImage` —— 8/13 个有
- `Text` —— 6/13 个有
- `SaveImage` —— 5/13 个有
- `LTXVSeparateAVLatent` —— 2/13 个有
- `LayerUtility: PurgeVRAM V2` —— 2/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `MiniMaxLowVRAMAttention` —— 2/13 个有
- `MinimaxH3LatentUpscaler3D` —— 2/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `ModelPreviewOverrideKJ` —— 2/13 个有
- `Notif-PlaySound` —— 2/13 个有
- `PT_H3ConcatAVLatent` —— 2/13 个有
- `RIFE VFI` —— 2/13 个有
- `ShellAgentPluginSaveAudios` —— 2/13 个有
- `SplitSigmas` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `Float` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `MiniMaxH3EasyMediaLoader` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `TTResolutionSelector` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
