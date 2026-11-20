---
name: text_to_image_lora_sampler_clip_314
type: Text To Image
frequency: 7
level: strong
coverage: 0.899571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MImax H3超强开源视频加速-图生视频工作流_2087344640801464322.json, 视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json, 视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json, 视频生成/图生视频/MiniMax H3参考生视频数字人 图生视频智能体创作_2098639055553646593.json, 视频生成/图生视频/MiniMax H3参考生视频｜数字人动作神态复刻_2098709684097212418.json, 视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json, 视频生成/图生视频/Minimax H3多参生视频sag backend block cache 2倍速加速版_2088271045022277634.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_314

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MImax H3超强开源视频加速-图生视频工作流_2087344640801464322.json、视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json、视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json、视频生成/图生视频/MiniMax H3参考生视频数字人 图生视频智能体创作_2098639055553646593.json、视频生成/图生视频/MiniMax H3参考生视频｜数字人动作神态复刻_2098709684097212418.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `SaveImage` —— 3/7 个有
- `TrimAudioDuration` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `SolAttnPatch` —— 2/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/7 个有
- `ApplyFaceProcessor` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CompressImages` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `FaceProcessorLoader` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `SaveMP4` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
