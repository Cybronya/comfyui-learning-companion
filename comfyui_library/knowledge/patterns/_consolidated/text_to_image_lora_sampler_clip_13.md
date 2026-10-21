---
name: text_to_image_lora_sampler_clip_13
type: Text To Image
frequency: 28
level: strong
coverage: 0.874286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/人物三视图生成｜MinimaxH3老金驿站高细节工作流_2090834916031426562.json, 视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json, 视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频多素材融合_2088699208495882241.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2092760928600285186.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2093795328280584193.json, 视频生成/图生视频/多图生视频+音频+视频接入｜MiniMax H3场景特效_2092205364438720514.json, 视频生成/图生视频/多图生视频音频视频接入｜MiniMax H3场景特效生成_2092018470065106945.json, 视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092388355215552514.json, 视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json, 视频生成/文生视频/MiniMax H3多图参考成片V2六段式提示词IndexTTS声音克隆文生视频_2088269344596914177.json, 视频生成/文生视频/MiniMax参考生视频高质量加速版处理工具_2101029961053327362.json, 视频生成/文生视频/Minimax参考生视频加速版｜高质量出片速度快人一步_2107652187882090498.json, 视频生成/文生视频/Minimax参考生视频高质量加速版工作流，文生视频视频运镜图生视频方案_2107891842988728321.json, 视频生成/文生视频/Minimax参考生视频高质量加速版｜视频运镜文生视频_2092068882994524162.json, 视频生成/文生视频/Minimax图生视频高质量加速版，文生视频图生视频高效创作工具_2105716933747367938.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜出片速度快 画质还在线的省心之选_2105487062328766465.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜快速视频生成_2094526253780000770.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜画质速度兼得_2097166149703262210.json, 视频生成/文生视频/分镜成片IndexTTS声音克隆配音｜MiniMax H3剧本角色图分镜一次出片工作流_2088217265090158594.json, 视频生成/文生视频/参考生视频高质量加速版｜Minimax运镜图生视频生成_2097045021672427522.json, 视频生成/文生视频/图生视频高质量加速版｜Minimax画面细节增强生成_2097028896674897921.json, 视频生成/文生视频/高质量加速版Minimax参考生视频文生视频图生视频运镜控制_2088379560130859010.json, 视频生成/文生视频/高质量加速版参考生视频｜Minimax文生图生视频运镜工作流_2087161521527934977.json, 视频生成/文生视频/高质量加速版参考生视频｜Minimax文生视频运镜图生视频工作流_2088351403445145601.json, 视频生成/文生视频/高质量加速版图生视频｜Minimax一键生成处理_2094746588890624001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/人物三视图生成｜MinimaxH3老金驿站高细节工作流_2090834916031426562.json、视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json、视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 27/28 个有
- `PrimitiveFloat` —— 27/28 个有
- `VAEDecodeAudio` —— 25/28 个有
- `MiniMaxH3ReferenceToVideo` —— 22/28 个有
- `MiniMaxH3BlockCacheT8` —— 17/28 个有
- `ImageResizeKJv2` —— 15/28 个有
- `PathchSageAttentionKJ` —— 15/28 个有
- `PrimitiveInt` —— 15/28 个有
- `ResolutionSelector` —— 13/28 个有
- `LoadAudio` —— 11/28 个有
- `MiniMaxH3ImageToVideo` —— 6/28 个有
- `SaveImage` —— 6/28 个有
- `AudioCrop` —— 3/28 个有
- `AILab_QwenVL` —— 2/28 个有
- `GetVideoComponents` —— 2/28 个有
- `IndexTTS2Run` —— 2/28 个有
- `LoadVideo` —— 2/28 个有
- `MultiLinePromptIndex` —— 2/28 个有
- `SaveAudioMP3` —— 2/28 个有
- `ImageFromBatch` —— 1/28 个有
- `ImageStitch` —— 1/28 个有
- `JoinStrings` —— 1/28 个有
- `MiniMaxChunkFeedForward` —— 1/28 个有
- `ModelAttentionBackend` —— 1/28 个有
- `ModelPatchTorchSettings` —— 1/28 个有
- `StringConcatenate` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
