---
name: text_to_image_lora_sampler_clip_18
type: Text To Image
frequency: 20
level: strong
coverage: 0.8717
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3多图参考成片V2六段式提示词IndexTTS声音克隆文生视频_2088269344596914177.json, 视频生成/文生视频/MiniMax H3开源版｜多图参考视频生成一键处理_2094756800972279809.json, 视频生成/文生视频/MiniMax H3文生图生视频｜260817001双模式视频生成_2089730940615614465.json, 视频生成/文生视频/MiniMax-4步加速工作流文生视频视频生视频图生视频_2085455891675049986.json, 视频生成/文生视频/Minimax参考生视频加速版｜高质量出片速度快人一步_2107652187882090498.json, 视频生成/文生视频/Minimax参考生视频高质量加速版工作流，文生视频视频运镜图生视频方案_2107891842988728321.json, 视频生成/文生视频/Minimax参考生视频高质量加速版｜视频运镜文生视频_2092068882994524162.json, 视频生成/文生视频/Minimax图生视频高质量加速版，文生视频图生视频高效创作工具_2105716933747367938.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜出片速度快 画质还在线的省心之选_2105487062328766465.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜快速视频生成_2094526253780000770.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜画质速度兼得_2097166149703262210.json, 视频生成/文生视频/Ref2VA剧本直出六段式自动生成校验9图参考成片｜H3原生音画同步文生图生视频_2088323034326331393.json, 视频生成/文生视频/六段式自动生成自动校验MiniMax H3 Ref2VA剧本直出9图参考成片原生音画同步_2088355373936893954.json, 视频生成/文生视频/分镜成片IndexTTS声音克隆配音｜MiniMax H3剧本角色图分镜一次出片工作流_2088217265090158594.json, 视频生成/文生视频/参考生视频高质量加速版｜Minimax运镜图生视频生成_2097045021672427522.json, 视频生成/文生视频/图生视频高质量加速版｜Minimax画面细节增强生成_2097028896674897921.json, 视频生成/文生视频/高质量加速版Minimax参考生视频文生视频图生视频运镜控制_2088379560130859010.json, 视频生成/文生视频/高质量加速版参考生视频｜Minimax文生图生视频运镜工作流_2087161521527934977.json, 视频生成/文生视频/高质量加速版参考生视频｜Minimax文生视频运镜图生视频工作流_2088351403445145601.json, 视频生成/文生视频/高质量加速版图生视频｜Minimax一键生成处理_2094746588890624001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3多图参考成片V2六段式提示词IndexTTS声音克隆文生视频_2088269344596914177.json、视频生成/文生视频/MiniMax H3开源版｜多图参考视频生成一键处理_2094756800972279809.json、视频生成/文生视频/MiniMax H3文生图生视频｜260817001双模式视频生成_2089730940615614465.json、视频生成/文生视频/MiniMax-4步加速工作流文生视频视频生视频图生视频_2085455891675049986.json、视频生成/文生视频/Minimax参考生视频加速版｜高质量出片速度快人一步_2107652187882090498.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 19/20 个有
- `VAEDecodeAudio` —— 18/20 个有
- `MiniMaxH3BlockCacheT8` —— 17/20 个有
- `PathchSageAttentionKJ` —— 14/20 个有
- `ImageResizeKJv2` —— 13/20 个有
- `MiniMaxH3ReferenceToVideo` —— 13/20 个有
- `PrimitiveInt` —— 13/20 个有
- `MiniMaxH3ImageToVideo` —— 7/20 个有
- `ResolutionSelector` —— 7/20 个有
- `SaveImage` —— 4/20 个有
- `LoadAudio` —— 3/20 个有
- `AudioCrop` —— 2/20 个有
- `IndexTTS2Run` —— 2/20 个有
- `MultiLinePromptIndex` —— 2/20 个有
- `RHLLMChatNode` —— 2/20 个有
- `SaveAudioMP3` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `ImageCrop+` —— 1/20 个有
- `ImageScaleToTotalPixels` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
