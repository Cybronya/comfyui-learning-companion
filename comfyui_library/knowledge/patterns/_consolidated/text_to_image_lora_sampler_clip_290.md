---
name: text_to_image_lora_sampler_clip_290
type: Text To Image
frequency: 7
level: strong
coverage: 0.853429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3双人对话 文生音频图生图处理生成工具_2100316663001477121.json, 平台全量/稳定加速版全能参考刘神1_2094037719600164866.json, 数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json, 数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json, 视频生成/图生视频/4步多图自用提速｜H3图生视频快速参考生成_2089040496692916225.json, 视频生成/图生视频/高质量加速版图生视频｜MiniMax H3图片转视频工作流_2088135941901864962.json, 音频生成/音频生成/MiniMax H3 TTS文生音频音频克隆SeedAudio开源版_2088194262323253249.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_290

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/H3双人对话 文生音频图生图处理生成工具_2100316663001477121.json、平台全量/稳定加速版全能参考刘神1_2094037719600164866.json、数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json、数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json、视频生成/图生视频/4步多图自用提速｜H3图生视频快速参考生成_2089040496692916225.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `MiniMaxH3AudioConditioningT8` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `LoraLoaderBypassModelOnly` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `EasyCache` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `MiniMaxH3ReferenceToVideo` —— 2/7 个有
- `SaveAudioAdvanced` —— 2/7 个有
- `easy ifElse` —— 2/7 个有
- `easy isNone` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `JWString` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `LayerUtility: TextBox` —— 1/7 个有
- `LoadVideo` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `SpectrumSDXL` —— 1/7 个有

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
