---
name: text_to_image_video_lora_sampler_38
type: Text To Image
frequency: 15
level: strong
coverage: 0.770067
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json, 视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json, 视频生成/图生视频/H3音频驱动数字人单人版｜口播视频高质量生成_2094900079206424577.json, 视频生成/图生视频/MiniMax-H3音频数字人来了｜单人出镜最高15秒，口播带货省事_2099401548009918466.json, 视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json, 视频生成/图生视频/单人版音频驱动数字人｜H3图生视频对口型生成_2095092471347900417.json, 视频生成/图生视频/单人音频驱动数字人（最高15秒）MiniMax-H3_2087437541388673025.json, 视频生成/图生视频/数字人对口型生成｜H3视频生视频图生视频直出_2092730251368558593.json, 视频生成/图生视频/数字人说话唱歌MV｜MiniMaxH3开源版音频驱动对口型加速生成_2090848011483172865.json, 视频生成/图生视频/音频驱动对口型MV｜MiniMaxH3开源数字人加速版_2095079699335700481.json, 视频生成/图生视频/音频驱动数字人MV｜MiniMaxH3开源版 说话唱歌对口型加速生成_2105524576473141249.json, 视频生成/图生视频/音频驱动数字人对口型｜MiniMaxH3开源版说话唱歌MV生成加速_2090840855216222210.json, 视频生成/图生视频/音频驱动数字人｜MiniMaxH3说话唱歌对口型MV加速版_2090544996637302786.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json、视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json、视频生成/图生视频/H3音频驱动数字人单人版｜口播视频高质量生成_2094900079206424577.json、视频生成/图生视频/MiniMax-H3音频数字人来了｜单人出镜最高15秒，口播带货省事_2099401548009918466.json、视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 13/15 个有
- `ComfyMathExpression` —— 13/15 个有
- `PrimitiveFloat` —— 13/15 个有
- `PathchSageAttentionKJ` —— 12/15 个有
- `PreviewAudio` —— 11/15 个有
- `PrimitiveStringMultiline` —— 11/15 个有
- `GetNode` —— 10/15 个有
- `SetNode` —— 10/15 个有
- `Any To String (mtb)` —— 8/15 个有
- `ImageResizeKJv2` —— 8/15 个有
- `PreviewImage` —— 8/15 个有
- `PrimitiveInt` —— 8/15 个有
- `ResolutionSelector` —— 7/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/15 个有
- `CR Prompt Text` —— 4/15 个有
- `ModelAttentionBackend` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `FlashVSRNode` —— 2/15 个有
- `LayerUtility: PurgeVRAM V2` —— 2/15 个有
- `LoraLoaderBypassModelOnly` —— 2/15 个有
- `MathExpression|pysssss` —— 2/15 个有
- `MiniMaxH3SigmaShift` —— 2/15 个有
- `ModelPreviewOverrideKJ` —— 2/15 个有
- `SaveImage` —— 2/15 个有
- `ShowAnything|Mie` —— 2/15 个有
- `Sleep` —— 2/15 个有
- `TrimAudioDuration` —— 2/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
