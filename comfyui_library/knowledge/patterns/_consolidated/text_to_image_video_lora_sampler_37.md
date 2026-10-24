---
name: text_to_image_video_lora_sampler_37
type: Text To Image
frequency: 16
level: strong
coverage: 0.784125
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MinimaxH3音乐数字人分段长视频版｜角色表演连贯不跳戏｜一致性稳如老狗_2104752849640058882.json, 数字人/数字人/MinimaxH3音乐数字人无限分段｜长视频角色一致性表演｜数字人唱歌不打断_2104748069731520513.json, 数字人/数字人/高阶双采加速不降质音频驱动数字人｜MiniMax H3新技术视频流_2111757289240743938.json, 视频生成/图生视频/MiniMax H3单图数字人SelfLift无限分段长视频工作流，数字人图生视频方案_2107539277377794049.json, 视频生成/图生视频/MiniMax H3音乐数字人无限分段长视频处理生成工具_2102121536076472321.json, 视频生成/图生视频/Minimax H3单图数字人selflift无限分段｜一张照片变身长视频主播_2107348289380241409.json, 视频生成/图生视频/Minimax-H3音乐数字人工作流｜无限分段长视频｜音频驱动口播_2101882039300612097.json, 视频生成/图生视频/Minimax-H3音乐数字人无限分段长视频｜音频驱动图生视频演唱_2101917400844300290.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频 数字人口播方案_2109432298180534273.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频 数字人口播方案_2109743708005556226.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频修复报错 数字人口播方案_2109394122141425666.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频修复报错 数字人口播方案_2109416523596132354.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段，长视频图生视频方案_2111270412171698177.json, 视频生成/图生视频/MinimaxH3音乐数字人长视频｜无限分段连播不断档_2111133304434028545.json, 视频生成/图生视频/MinimaxH3音乐数字人｜无限分段长视频直出｜唱歌视频一键到底_2102654919030427649.json, 视频生成/图生视频/高阶双采加速音频驱动数字人，图生视频不降质方案_2111240854835916802.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/MinimaxH3音乐数字人分段长视频版｜角色表演连贯不跳戏｜一致性稳如老狗_2104752849640058882.json、数字人/数字人/MinimaxH3音乐数字人无限分段｜长视频角色一致性表演｜数字人唱歌不打断_2104748069731520513.json、数字人/数字人/高阶双采加速不降质音频驱动数字人｜MiniMax H3新技术视频流_2111757289240743938.json、视频生成/图生视频/MiniMax H3单图数字人SelfLift无限分段长视频工作流，数字人图生视频方案_2107539277377794049.json、视频生成/图生视频/MiniMax H3音乐数字人无限分段长视频处理生成工具_2102121536076472321.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 16 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 14/16 个有
- `DF_Int_to_Float` —— 14/16 个有
- `GetNode` —— 14/16 个有
- `ImageResizeKJv2` —— 14/16 个有
- `Int` —— 14/16 个有
- `ModelPreviewOverrideKJ` —— 14/16 个有
- `PreviewAudio` —— 14/16 个有
- `PrimitiveInt` —— 14/16 个有
- `PrimitiveStringMultiline` —— 14/16 个有
- `SetNode` —— 14/16 个有
- `VHS_LoadAudioUpload` —— 14/16 个有
- `Compare` —— 12/16 个有
- `InversionDemoLazySwitch` —— 12/16 个有
- `PreviewImage` —— 12/16 个有
- `SaveImage` —— 8/16 个有
- `LoadAudio` —— 4/16 个有
- `CR Prompt Text` —— 2/16 个有
- `FlashVSRNode` —— 2/16 个有
- `Float` —— 2/16 个有
- `MelBandRoFormerModelLoader` —— 2/16 个有
- `MelBandRoFormerSampler` —— 2/16 个有
- `PreviewAny` —— 2/16 个有
- `ResolutionSelector` —— 2/16 个有
- `SelfLiftAvatarH3TST` —— 2/16 个有
- `TrimAudioDuration` —— 2/16 个有
- `easy showAnything` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
