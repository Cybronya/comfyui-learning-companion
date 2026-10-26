---
name: text_to_image_lora_sampler_clip_53
type: Text To Image
frequency: 17
level: strong
coverage: 0.905882
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/低显存专用MiniMax H3双采多参 图生视频影视处理工具_2113040884995547137.json, 视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json, 视频生成/图生视频/低显存友好方案｜时间分块前馈分块MiniMax H3双采参考生视频_2101157041715900417.json, 视频生成/图生视频/动态最强单采生成｜Dasiwa-MiniMax H3参考生视频_2095562835513405441.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速开源版｜MiniMax H3角色设计人物类特效图生视频_2088339977326383106.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速开源｜MiniMax H3人物类特效角色设计图生视频_2088325534035042306.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速版MiniMax H3开源版图生视频_2088371949490761729.json, 视频生成/图生视频/参考图生视频｜Dasiwa MinimaxH3一键生成_2092617206365515777.json, 视频生成/图生视频/参考生视频开源版｜Minimax-H3短剧漫剧角色表演_2094781908717756417.json, 视频生成/图生视频/唱歌MV数字人｜H3音频驱动多参视频生成对口型_2093102730167541762.json, 视频生成/图生视频/图生·首尾帧·多参一体化（H38步双时钟）极速导演台ENG_2087117508317900801.json, 视频生成/图生视频/时间分块前馈分块降显存｜MiniMax H3双采参考生视频_2101187630208737281.json, 视频生成/文生视频/MiniMax H3加速版参考生视频长视频直出单采处理工具_2101364588674637826.json, 视频生成/文生视频/MiniMax H3音频驱动数字人加速版长视频直出处理工具_2101009649368653826.json, 视频生成/文生视频/MiniMax H3音频驱动数字人加速版｜参考生视频长视频直出_2100769157192183810.json, 视频生成/文生视频/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2101416149702504449.json, 视频生成/文生视频/加速版单采参考生视频｜MiniMax H3长视频直出_2101171837278449665.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/低显存专用MiniMax H3双采多参 图生视频影视处理工具_2113040884995547137.json、视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json、视频生成/图生视频/低显存友好方案｜时间分块前馈分块MiniMax H3双采参考生视频_2101157041715900417.json、视频生成/图生视频/动态最强单采生成｜Dasiwa-MiniMax H3参考生视频_2095562835513405441.json、视频生成/图生视频/去油版数字人口播唱歌MV加速开源版｜MiniMax H3角色设计人物类特效图生视频_2088339977326383106.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 16/17 个有
- `VHS_VideoCombine` —— 14/17 个有
- `PrimitiveFloat` —— 13/17 个有
- `SolAttnMiniMax` —— 12/17 个有
- `LoadAudio` —— 9/17 个有
- `SaveImage` —— 6/17 个有
- `JWFloat` —— 4/17 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 4/17 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 4/17 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 4/17 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 4/17 个有
- `PreviewAny` —— 4/17 个有
- `easy cleanGpuUsed` —— 4/17 个有
- `CreateVideo` —— 3/17 个有
- `PreviewAudio` —— 3/17 个有
- `SaveVideo` —— 3/17 个有
- `TrimAudioDuration` —— 3/17 个有
- `DuckHideNode` —— 1/17 个有

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
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
