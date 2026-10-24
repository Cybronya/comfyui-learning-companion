---
name: text_to_image_lora_sampler_clip_284
type: Text To Image
frequency: 7
level: strong
coverage: 0.847714
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3超级长视频1-10顺序生成 自动合并输出_2098819352618426369.json, 视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json, 视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json, 视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频音频参考_2085178835024306178.json, 视频生成/文生视频/新4步LoRa参考图｜MiniMax H3角色一致图生视频_2092736016280023041.json, 视频生成/文生视频/量化加速参考生视频｜MiniMaxH3 文本图像音视频全参考_2089345982659121153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_284

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3超级长视频1-10顺序生成 自动合并输出_2098819352618426369.json、视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json、视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json、视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json、视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频音频参考_2085178835024306178.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `AudioConcatenate` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `ImageBatch` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `VRAM_Debug` —— 1/7 个有
- `VideoInfoLoaded` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
