---
name: text_to_image_video_lora_sampler_17
type: Text To Image
frequency: 27
level: strong
coverage: 0.82363
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3音乐数字人 音频驱动对口型视频生成工具_2113772784173277185.json, 数字人/数字人/MiniMax H3音乐数字人 无限分段长视频音频驱动处理工具_2113013746007371778.json, 数字人/数字人/MinimaxH3音乐数字人分段长视频版｜角色表演连贯不跳戏｜一致性稳如老狗_2104752849640058882.json, 数字人/数字人/MinimaxH3音乐数字人无限分段｜长视频角色一致性表演｜数字人唱歌不打断_2104748069731520513.json, 数字人/数字人/Selflift数字人开口说话｜一张照片一段音频就开演_2111320781878808578.json, 数字人/数字人/慕斯AI MiniMaxH3数字人口播｜图生视频带货口播直出_2112859987381936129.json, 视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json, 视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H3 Selflift_2105763503423442946.json, 视频生成/图生视频/MiniMax H3 SelfLift数字人1080p图生视频处理工具_2101012772418052098.json, 视频生成/图生视频/MiniMax H3单图数字人SelfLift无限分段长视频工作流，数字人图生视频方案_2107539277377794049.json, 视频生成/图生视频/MiniMax H3音乐数字人无限分段长视频处理生成工具_2102121536076472321.json, 视频生成/图生视频/MiniMax H3高清数字人自动提示词图生视频处理工具_2101031617153290241.json, 视频生成/图生视频/Minimax H3 Selflift数字人三采｜角色一致画质再进阶_2103707327995138049.json, 视频生成/图生视频/Minimax H3 Selflift数字人｜口播带货数字人轻松做_2111136546035421186.json, 视频生成/图生视频/Minimax H3单图数字人selflift无限分段｜一张照片变身长视频主播_2107348289380241409.json, 视频生成/图生视频/Minimax-H3音乐数字人工作流｜无限分段长视频｜音频驱动口播_2101882039300612097.json, 视频生成/图生视频/Minimax-H3音乐数字人无限分段长视频｜音频驱动图生视频演唱_2101917400844300290.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频 数字人口播方案_2109432298180534273.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频 数字人口播方案_2109743708005556226.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频修复报错 数字人口播方案_2109394122141425666.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频修复报错 数字人口播方案_2109416523596132354.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段，长视频图生视频方案_2111270412171698177.json, 视频生成/图生视频/MinimaxH3音乐数字人长视频｜无限分段连播不断档_2111133304434028545.json, 视频生成/图生视频/MinimaxH3音乐数字人｜无限分段长视频直出｜唱歌视频一键到底_2102654919030427649.json, 视频生成/图生视频/minimaxh3 Selflift数字人1080p｜超自然对口型图生视频_2100775766433816577.json, 视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json, 视频生成/文生视频/AI音乐MV数字人新二采｜Minimax H3 Selflift联动出片_2100782399897554945.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/MiniMax H3音乐数字人 音频驱动对口型视频生成工具_2113772784173277185.json、数字人/数字人/MiniMax H3音乐数字人 无限分段长视频音频驱动处理工具_2113013746007371778.json、数字人/数字人/MinimaxH3音乐数字人分段长视频版｜角色表演连贯不跳戏｜一致性稳如老狗_2104752849640058882.json、数字人/数字人/MinimaxH3音乐数字人无限分段｜长视频角色一致性表演｜数字人唱歌不打断_2104748069731520513.json、数字人/数字人/Selflift数字人开口说话｜一张照片一段音频就开演_2111320781878808578.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 26/27 个有
- `SoundFlow_GetLength` —— 26/27 个有
- `ModelPreviewOverrideKJ` —— 21/27 个有
- `PrimitiveFloat` —— 18/27 个有
- `PrimitiveStringMultiline` —— 18/27 个有
- `AudioSeparation` —— 16/27 个有
- `DF_Int_to_Float` —— 16/27 个有
- `ImageResizeKJv2` —— 16/27 个有
- `PrimitiveInt` —— 16/27 个有
- `VHS_LoadAudioUpload` —— 16/27 个有
- `GetNode` —— 15/27 个有
- `SetNode` —— 15/27 个有
- `PreviewAudio` —— 14/27 个有
- `PreviewImage` —— 14/27 个有
- `SaveImage` —— 14/27 个有
- `Compare` —— 13/27 个有
- `Int` —— 13/27 个有
- `InversionDemoLazySwitch` —— 13/27 个有
- `LoadAudio` —— 13/27 个有
- `PreviewAny` —— 13/27 个有
- `ComfyNumberConvert` —— 11/27 个有
- `ResolutionSelector` —— 11/27 个有
- `TrimAudioDuration` —— 11/27 个有
- `QwenH3PromptLocal` —— 4/27 个有
- `FlashVSRNode` —— 2/27 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 2/27 个有
- `Text Multiline` —— 2/27 个有
- `Textbox` —— 2/27 个有
- `Fast Groups Bypasser (rgthree)` —— 1/27 个有
- `MiniMaxH3ImageToVideo` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（28/27 个样本）：Steps较低可能导致细节不足
