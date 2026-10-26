---
name: text_to_image_lora_sampler_clip_316
type: Text To Image
frequency: 7
level: strong
coverage: 0.889286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json, 视频生成/图生视频/口播直出｜MinimaxH3数字人图生视频生成_2089809950645248002.json, 视频生成/图生视频/多元素参考生视频｜minimax h3图生视频直出_2092387092469993474.json, 视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json, 视频生成/图生视频/多图参考生成视频｜图生视频多图融合一键出片_2093775806538534914.json, 视频生成/图生视频/数字人生成｜minimaxh3图生视频口播直出_2089485343300083713.json, 视频生成/文生视频/新4步LoRa参考图｜MiniMax H3角色一致图生视频_2092736016280023041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_316

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json、视频生成/图生视频/口播直出｜MinimaxH3数字人图生视频生成_2089809950645248002.json、视频生成/图生视频/多元素参考生视频｜minimax h3图生视频直出_2092387092469993474.json、视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json、视频生成/图生视频/多图参考生成视频｜图生视频多图融合一键出片_2093775806538534914.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `VAEDecodeAudio` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/7 个有
- `Int` —— 2/7 个有
- `SaveAudio` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `TrimAudioDuration` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `JWIntegerToString` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `MiniMaxLowVRAMAttention` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `Text` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
