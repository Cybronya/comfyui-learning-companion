---
name: text_to_image_video_lora_sampler_28
type: Text To Image
frequency: 22
level: strong
coverage: 0.840409
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json, 视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json, 视频生成/图生视频/Minimax H3开源数字人，说话唱歌文生视频两不误_2111201846995017729.json, 视频生成/图生视频/Minimax H3开源版数字人说话唱歌 数字人口播方案_2109421181240700930.json, 视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌口播一条龙免费跑_2111083053400547329.json, 视频生成/图生视频/Minimax H3开源版数字人｜说话唱歌视频都能做_2106615667175804930.json, 视频生成/图生视频/Minimax H3音频驱动数字人对口型人物类特效图生视频_2088195742426030081.json, 视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json, 视频生成/图生视频/口播直出｜MinimaxH3数字人图生视频生成_2089809950645248002.json, 视频生成/图生视频/对口型音频驱动MiniMax H3数字人唱歌工作流，一张图一段音频生成视频_2106864466716614658.json, 视频生成/图生视频/数字人说话唱歌MV｜MiniMaxH3开源版音频驱动对口型加速生成_2090848011483172865.json, 视频生成/图生视频/音频驱动对口型MV｜MiniMaxH3开源数字人加速版_2095079699335700481.json, 视频生成/图生视频/音频驱动对口型｜Minimax H3数字人人物特效图生视频_2089446222766624769.json, 视频生成/图生视频/音频驱动数字人MV｜MiniMaxH3开源版 说话唱歌对口型加速生成_2105524576473141249.json, 视频生成/图生视频/音频驱动数字人对口型｜MiniMaxH3开源版说话唱歌MV生成加速_2090840855216222210.json, 视频生成/图生视频/音频驱动数字人｜MiniMaxH3说话唱歌对口型MV加速版_2090544996637302786.json, 视频生成/文生视频/MiniMax H3开源版数字人说话唱歌音频驱动图生视频处理工具_2102519299419230209.json, 视频生成/文生视频/Minimax H3开源版数字人说话唱歌工作流，文生视频数字人图生视频方案_2108269811766751233.json, 视频生成/文生视频/开源版数字人说话唱歌｜Minimax H3图生视频直出_2092339960107061250.json, 视频生成/文生视频/开源版数字人｜MiniMax H3说话唱歌文生图生视频_2092589071527923714.json, 视频生成/文生视频/说话唱歌数字人｜Minimax H3开源版图生视频生成_2094743484795277314.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3开源版音频驱动数字人-说话唱歌对口型MV生成加速版_2087383420715487233.json、视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV加速版_2094877180009476098.json、视频生成/图生视频/MiniMaxH3开源音频驱动数字人｜说话唱歌对口型MV生成_2094880039287476225.json、视频生成/图生视频/Minimax H3开源数字人，说话唱歌文生视频两不误_2111201846995017729.json、视频生成/图生视频/Minimax H3开源版数字人说话唱歌 数字人口播方案_2109421181240700930.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 21/22 个有
- `孤海注释` —— 21/22 个有
- `AudioCrop` —— 20/22 个有
- `PreviewAudio` —— 20/22 个有
- `SoundFlow_GetLength` —— 20/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/22 个有
- `Int` —— 9/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/22 个有
- `Any To String (mtb)` —— 8/22 个有
- `GetNode` —— 8/22 个有
- `ImageResizeKJv2` —— 8/22 个有
- `PreviewImage` —— 8/22 个有
- `PrimitiveInt` —— 8/22 个有
- `SetNode` —— 8/22 个有
- `ResolutionSelector` —— 5/22 个有
- `SaveImage` —— 5/22 个有
- `AudioConcat` —— 2/22 个有
- `EmptyAudio` —— 2/22 个有
- `SaveAudio` —— 2/22 个有
- `TrimAudioDuration` —— 2/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 高发问题（23/22 个样本）：Steps较低可能导致细节不足
