---
name: text_to_image_video_lora_sampler_142
type: Text To Image
frequency: 4
level: strong
coverage: 0.92475
common_nodes: [AudioConcat, BasicGuider, BatchImagesNode, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, GetImageRangeFromBatch, ImageBlur, Int, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RIFE VFI, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SolAttnMiniMax, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2106756389191372802.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2108613384685047809.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2109704350506508290.json, 数字人/数字人/MiniMax H3音频驱动数字人｜多人对话加速长视频处理_2108375930543624193.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2106756389191372802.json、数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2108613384685047809.json、数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2109704350506508290.json、数字人/数字人/MiniMax H3音频驱动数字人｜多人对话加速长视频处理_2108375930543624193.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `ImageBlur`
- `Int`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RIFE VFI`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SolAttnMiniMax`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Combine Prompt` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `ImageBatchRepeatInterleaving` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
