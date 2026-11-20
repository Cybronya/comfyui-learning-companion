---
name: text_to_image_lora_sampler_clip_27
type: Text To Image
frequency: 24
level: strong
coverage: 0.853458
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3多图参考成片V2六段式提示词IndexTTS声音克隆文生视频_2088269344596914177.json, 视频生成/文生视频/MiniMax H3开源版｜多图参考视频生成一键处理_2094756800972279809.json, 视频生成/文生视频/MiniMax H3文生图生视频｜260817001双模式视频生成_2089730940615614465.json, 视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json, 视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json, 视频生成/文生视频/MiniMax H3文生视频纯净版｜从零开始生成完整短片_2107694082242990081.json, 视频生成/文生视频/MiniMaxH3文生视频 文本转视频高速生成处理工具_2113771189691830274.json, 视频生成/文生视频/MiniMaxH3文生视频工作流｜文字描述直接生成精彩视频_2113557011672686593.json, 视频生成/文生视频/Minimax参考生视频加速版｜高质量出片速度快人一步_2107652187882090498.json, 视频生成/文生视频/Minimax参考生视频高质量加速版工作流，文生视频视频运镜图生视频方案_2107891842988728321.json, 视频生成/文生视频/Minimax参考生视频高质量加速版｜视频运镜文生视频_2092068882994524162.json, 视频生成/文生视频/Minimax图生视频高质量加速版，文生视频图生视频高效创作工具_2105716933747367938.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜出片速度快 画质还在线的省心之选_2105487062328766465.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜快速视频生成_2094526253780000770.json, 视频生成/文生视频/Minimax图生视频高质量加速版｜画质速度兼得_2097166149703262210.json, 视频生成/文生视频/Minimax文生视频T2V工作流，加写实LoRA开关文生视频方案_2106872283892637697.json, 视频生成/文生视频/Minimax文生视频T2V工作流，文生视频官方文生视频处理工具_2107930345889943553.json, 视频生成/文生视频/分镜成片IndexTTS声音克隆配音｜MiniMax H3剧本角色图分镜一次出片工作流_2088217265090158594.json, 视频生成/文生视频/参考生视频高质量加速版｜Minimax运镜图生视频生成_2097045021672427522.json, 视频生成/文生视频/图生视频高质量加速版｜Minimax画面细节增强生成_2097028896674897921.json, 视频生成/文生视频/高质量加速版Minimax参考生视频文生视频图生视频运镜控制_2088379560130859010.json, 视频生成/文生视频/高质量加速版参考生视频｜Minimax文生图生视频运镜工作流_2087161521527934977.json, 视频生成/文生视频/高质量加速版参考生视频｜Minimax文生视频运镜图生视频工作流_2088351403445145601.json, 视频生成/文生视频/高质量加速版图生视频｜Minimax一键生成处理_2094746588890624001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3多图参考成片V2六段式提示词IndexTTS声音克隆文生视频_2088269344596914177.json、视频生成/文生视频/MiniMax H3开源版｜多图参考视频生成一键处理_2094756800972279809.json、视频生成/文生视频/MiniMax H3文生图生视频｜260817001双模式视频生成_2089730940615614465.json、视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json、视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 24 个 workflow 都包含：
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
- `VAEDecodeAudio` —— 22/24 个有
- `PrimitiveInt` —— 20/24 个有
- `LoadImage` —— 17/24 个有
- `PrimitiveStringMultiline` —— 16/24 个有
- `MiniMaxH3BlockCacheT8` —— 15/24 个有
- `MiniMaxH3ImageToVideo` —— 14/24 个有
- `ImageResizeKJv2` —— 13/24 个有
- `PathchSageAttentionKJ` —— 13/24 个有
- `ResolutionSelector` —— 11/24 个有
- `MiniMaxH3ReferenceToVideo` —— 10/24 个有
- `ComfySwitchNode` —— 7/24 个有
- `PrimitiveBoolean` —— 7/24 个有
- `SaveImage` —— 7/24 个有
- `LoadAudio` —— 4/24 个有
- `AudioCrop` —— 3/24 个有
- `GetNode` —— 2/24 个有
- `IndexTTS2Run` —— 2/24 个有
- `MultiLinePromptIndex` —— 2/24 个有
- `SaveAudioMP3` —— 2/24 个有
- `SetNode` —— 2/24 个有
- `CR Text` —— 1/24 个有
- `ImageCrop+` —— 1/24 个有
- `ImageScaleToTotalPixels` —— 1/24 个有
- `easy minimaxH3AudioLock` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：Steps较低可能导致细节不足
