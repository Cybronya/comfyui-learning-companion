---
name: text_to_image_video_lora_sampler_128
type: Text To Image
frequency: 5
level: strong
coverage: 0.8958
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowInt, CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptyLatentImage, Int, IntToString, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveBoolean, RHLLMChatNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, floatToInt _O, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3 MV制作｜开场间奏画面图生视频一键搞定_2089415390387589122.json, 视频生成/图生视频/Minimax H3唱歌跳舞换装｜数字人图生视频创意玩法_2089452113129725954.json, 视频生成/图生视频/Minimax H3数字人唱歌跳舞换装一体｜图生视频创意工作流_2089720756715483138.json, 视频生成/图生视频/唱歌跳舞换装数字人｜Minimax H3 图生视频_2089269821186863106.json, 视频生成/图生视频/数字人唱歌跳舞换装创意玩法 Minimax H3图生视频数字人应用方案_2093211398343057410.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 MV制作｜开场间奏画面图生视频一键搞定_2089415390387589122.json、视频生成/图生视频/Minimax H3唱歌跳舞换装｜数字人图生视频创意玩法_2089452113129725954.json、视频生成/图生视频/Minimax H3数字人唱歌跳舞换装一体｜图生视频创意工作流_2089720756715483138.json、视频生成/图生视频/唱歌跳舞换装数字人｜Minimax H3 图生视频_2089269821186863106.json、视频生成/图生视频/数字人唱歌跳舞换装创意玩法 Minimax H3图生视频数字人应用方案_2093211398343057410.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `Int`
- `IntToString`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RHLLMChatNode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `floatToInt _O`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 4/5 个有
- `Bjornulf_ShowFloat` —— 4/5 个有
- `CR Text Concatenate` —— 4/5 个有
- `MelBandRoFormerModelLoader` —— 4/5 个有
- `MelBandRoFormerSampler` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `PreviewAudio` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `RH_GetAudioDuration` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/5 个有
- `MultiTextConcatenate` —— 1/5 个有
- `VAEDecodeAudio` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `sanmi Float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
