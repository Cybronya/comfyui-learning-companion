---
name: text_to_image_video_lora_sampler_47
type: Text To Image
frequency: 16
level: strong
coverage: 0.807625
common_nodes: [AudioCrop, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4步lora加速版Minimax_h3_音乐MV_2085452422591377409.json, 视频生成/图生视频/MiniMax-H3音频数字人来了｜单人出镜最高15秒，口播带货省事_2099401548009918466.json, 视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json, 视频生成/图生视频/Minimax H3音频驱动数字人对口型人物类特效图生视频_2088195742426030081.json, 视频生成/图生视频/单人音频驱动数字人（最高15秒）MiniMax-H3_2087437541388673025.json, 视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json, 视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json, 视频生成/图生视频/数字人说话唱歌MV｜MiniMaxH3开源版音频驱动对口型加速生成_2090848011483172865.json, 视频生成/图生视频/音频驱动对口型MV｜MiniMaxH3开源数字人加速版_2095079699335700481.json, 视频生成/图生视频/音频驱动对口型｜Minimax H3数字人人物特效图生视频_2089446222766624769.json, 视频生成/图生视频/音频驱动数字人MV｜MiniMaxH3开源版 说话唱歌对口型加速生成_2105524576473141249.json, 视频生成/图生视频/音频驱动数字人对口型｜MiniMaxH3开源版说话唱歌MV生成加速_2090840855216222210.json, 视频生成/图生视频/音频驱动数字人｜MiniMaxH3说话唱歌对口型MV加速版_2090544996637302786.json, 视频生成/文生视频/MinimaxH3音频驱动数字人单人版｜文生视频数字人图生视频_2090448002296147970.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/4步lora加速版Minimax_h3_音乐MV_2085452422591377409.json、视频生成/图生视频/MiniMax-H3音频数字人来了｜单人出镜最高15秒，口播带货省事_2099401548009918466.json、视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json、视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json、视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 16 个 workflow 都包含：
- `AudioCrop`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 15/16 个有
- `BasicScheduler` —— 15/16 个有
- `KSamplerSelect` —— 15/16 个有
- `PathchSageAttentionKJ` —— 15/16 个有
- `PrimitiveFloat` —— 15/16 个有
- `RandomNoise` —— 15/16 个有
- `SamplerCustomAdvanced` —— 15/16 个有
- `ComfyMathExpression` —— 14/16 个有
- `PreviewAudio` —— 13/16 个有
- `PrimitiveStringMultiline` —— 13/16 个有
- `Any To String (mtb)` —— 8/16 个有
- `GetNode` —— 8/16 个有
- `ImageResizeKJv2` —— 8/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/16 个有
- `PreviewImage` —— 8/16 个有
- `PrimitiveInt` —— 8/16 个有
- `ResolutionSelector` —— 8/16 个有
- `SetNode` —— 8/16 个有
- `AudioConcat` —— 2/16 个有
- `CR Prompt Text` —— 2/16 个有
- `EmptyAudio` —— 2/16 个有
- `LayerUtility: PurgeVRAM V2` —— 2/16 个有
- `MathExpression|pysssss` —— 2/16 个有
- `MiniMaxH3SigmaShift` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
