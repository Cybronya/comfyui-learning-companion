---
name: text_to_image_video_lora_sampler_89
type: Text To Image
frequency: 9
level: strong
coverage: 0.894667
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/fengjing风景文生视频｜自然场景动态画面生成_2105256241860792321.json, 视频生成/文生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086255484864131074.json, 视频生成/文生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086540912632623105.json, 视频生成/文生视频/h3开源版H3数字人单人版运镜MiniMax图生视频口播数字人参考音频_2086497674601263105.json, 视频生成/文生视频/开源版数字人说话唱歌｜Minimax H3图生视频直出_2092339960107061250.json, 视频生成/文生视频/开源版数字人｜MiniMax H3说话唱歌文生图生视频_2092589071527923714.json, 视频生成/文生视频/精准可控数字人升级版｜H3音频驱动+全能参考附整合包_2093760313689722881.json, 视频生成/文生视频/精准可控数字人升级版｜H3音频驱动+全能参考附整合包_2093991203292401665.json, 视频生成/文生视频/说话唱歌数字人｜Minimax H3开源版图生视频生成_2094743484795277314.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_89

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/fengjing风景文生视频｜自然场景动态画面生成_2105256241860792321.json、视频生成/文生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086255484864131074.json、视频生成/文生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086540912632623105.json、视频生成/文生视频/h3开源版H3数字人单人版运镜MiniMax图生视频口播数字人参考音频_2086497674601263105.json、视频生成/文生视频/开源版数字人说话唱歌｜Minimax H3图生视频直出_2092339960107061250.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
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
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `Int` —— 7/9 个有
- `孤海注释` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `SoundFlow_GetLength` —— 6/9 个有
- `PreviewAudio` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `PathchSageAttentionKJ` —— 4/9 个有
- `JWIntegerToString` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `ResolutionSelector` —— 2/9 个有
- `MiniMaxH3BlockCacheT8` —— 1/9 个有
- `PrimitiveString` —— 1/9 个有
- `Text` —— 1/9 个有
- `ZML_MergeText` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
