---
name: text_to_image_video_lora_sampler_102
type: Text To Image
frequency: 7
level: strong
coverage: 0.918143
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2106756389191372802.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2108613384685047809.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2109704350506508290.json, 数字人/数字人/MiniMax H3音频驱动数字人｜多人对话加速长视频处理_2108375930543624193.json, 视频生成/图生视频/MiniMax H3音频驱动数字人 语音口型同步多人对话一键实现_2110352465429352449.json, 视频生成/图生视频/MiniMax H3音频驱动数字人加速版｜参考图生长视频直出_2103697575655333890.json, 视频生成/图生视频/MiniMax H3音频驱动数字人参考生视频长视频直出加速版，图生视频方案_2103992154782789634.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2106756389191372802.json、数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2108613384685047809.json、数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具_2109704350506508290.json、数字人/数字人/MiniMax H3音频驱动数字人｜多人对话加速长视频处理_2108375930543624193.json、视频生成/图生视频/MiniMax H3音频驱动数字人 语音口型同步多人对话一键实现_2110352465429352449.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `AudioConcat` —— 4/7 个有
- `BatchImagesNode` —— 4/7 个有
- `ComfySwitchNode` —— 4/7 个有
- `GetImageRangeFromBatch` —— 4/7 个有
- `ImageBlur` —— 4/7 个有
- `Int` —— 4/7 个有
- `RIFE VFI` —— 4/7 个有
- `SoundFlow_GetLength` —— 4/7 个有
- `TrimAudioDuration` —— 4/7 个有
- `VAEEncode` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `easy compare` —— 4/7 个有
- `easy forLoopEnd` —— 4/7 个有
- `easy forLoopStart` —— 4/7 个有
- `CR Combine Prompt` —— 3/7 个有
- `ImageBatchRepeatInterleaving` —— 2/7 个有

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
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
