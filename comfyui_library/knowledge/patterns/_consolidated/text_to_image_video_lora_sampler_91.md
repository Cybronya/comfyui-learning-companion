---
name: text_to_image_video_lora_sampler_91
type: Text To Image
frequency: 8
level: strong
coverage: 0.885625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/单图电商广告生成｜产品展示图生图一键完整广告_2093128655328342018.json, 图片生成/图生图/开源模型自动提示词｜全行业广告图生图制作_2091165245799751681.json, 图片生成/图生图/往前行走角色展示 MMH3 动漫资产lora训练集_2094259527184113665.json, 视频生成/图生视频/Minimax H3 MV制作｜开场间奏画面图生视频一键搞定_2089415390387589122.json, 视频生成/图生视频/Minimax H3唱歌跳舞换装｜数字人图生视频创意玩法_2089452113129725954.json, 视频生成/图生视频/Minimax H3数字人唱歌跳舞换装一体｜图生视频创意工作流_2089720756715483138.json, 视频生成/图生视频/唱歌跳舞换装数字人｜Minimax H3 图生视频_2089269821186863106.json, 视频生成/图生视频/数字人唱歌跳舞换装创意玩法 Minimax H3图生视频数字人应用方案_2093211398343057410.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/单图电商广告生成｜产品展示图生图一键完整广告_2093128655328342018.json、图片生成/图生图/开源模型自动提示词｜全行业广告图生图制作_2091165245799751681.json、图片生成/图生图/往前行走角色展示 MMH3 动漫资产lora训练集_2094259527184113665.json、视频生成/图生视频/Minimax H3 MV制作｜开场间奏画面图生视频一键搞定_2089415390387589122.json、视频生成/图生视频/Minimax H3唱歌跳舞换装｜数字人图生视频创意玩法_2089452113129725954.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 7/8 个有
- `CR Text Replace` —— 6/8 个有
- `Int` —— 6/8 个有
- `IntToString` —— 6/8 个有
- `RHLLMChatNode` —— 6/8 个有
- `floatToInt _O` —— 6/8 个有
- `Bjornulf_ShowInt` —— 5/8 个有
- `CR Text Concatenate` —— 5/8 个有
- `LazySwitch1way` —— 5/8 个有
- `ModelAttentionBackend` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `PreviewAny` —— 5/8 个有
- `PrimitiveBoolean` —— 5/8 个有
- `ShowAnything|Mie` —— 5/8 个有
- `AudioCrop` —— 4/8 个有
- `Bjornulf_ShowFloat` —— 4/8 个有
- `MelBandRoFormerModelLoader` —— 4/8 个有
- `MelBandRoFormerSampler` —— 4/8 个有
- `PreviewAudio` —— 4/8 个有
- `PrimitiveFloat` —— 4/8 个有
- `RH_GetAudioDuration` —— 4/8 个有
- `RH_Translator` —— 4/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `ImageBatchMultiV2` —— 3/8 个有
- `MultiTextConcatenate` —— 3/8 个有
- `VAEDecodeAudio` —— 3/8 个有
- `llama_cpp_instruct_adv` —— 3/8 个有
- `llama_cpp_model_loader` —— 3/8 个有
- `llama_cpp_parameters` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `easy int` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `JWFloat` —— 1/8 个有
- `sanmi Float` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
