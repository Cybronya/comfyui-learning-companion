---
name: unknown_workflow_lora_sampler_clip_54
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.8025
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json, 视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json, 视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json, 视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json, 视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json, 视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json, 视频生成/文生视频/双采样高质量图生视频 LTX2.3-单镜头可扩写提示词 高度遵从 运镜+动作+自动扩写 -高质量1K_2057269109406126081.json, 视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json、视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json、视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json、视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json、视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `KSamplerSelect` —— 7/8 个有
- `LTXVCropGuides` —— 7/8 个有
- `LTXVLatentUpsampler` —— 7/8 个有
- `LTXVScheduler` —— 7/8 个有
- `LatentUpscaleModelLoader` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `VAEDecodeTiled` —— 7/8 个有
- `EmptyImage` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `ImageScaleBy` —— 6/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `KSampler` —— 4/8 个有
- `ManualSigmas` —— 4/8 个有
- `VAEDecode` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Int` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `ComfyMathExpression` —— 1/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `LTXVImgToVideoInplace` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `SamplerEulerAncestral` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `TextGenerateLTX2Prompt` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有
- `easy float` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 8 | 92% |
| 高度 | 25 | 24 - 25 | 8 | 99% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.4 | 0.35 - 0.4 | 4 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，8 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 24 - 25，8 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.35 - 0.4，4 个样本，取值集中（一致性 94%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
