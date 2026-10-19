---
name: unknown_workflow_lora_sampler_clip_16
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7919
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json, 视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json, 视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json, 视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json, 视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json, 视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json, 视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json, 视频生成/文生视频/用LTX-2大模型轻松制作搞笑祝福视频，ComfyUI工作流教程来啦！_2010631084064641025.json, 视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json, 视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json、视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json、视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json、视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json、视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
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
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 9/10 个有
- `LTXVCropGuides` —— 9/10 个有
- `LTXVLatentUpsampler` —— 9/10 个有
- `LTXVScheduler` —— 9/10 个有
- `LatentUpscaleModelLoader` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `EmptyImage` —— 8/10 个有
- `GetImageSize` —— 8/10 个有
- `ImageScaleBy` —— 8/10 个有
- `PrimitiveFloat` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `ManualSigmas` —— 7/10 个有
- `VAEDecode` —— 6/10 个有
- `KSampler` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `CR Text` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `Int` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `ComfyMathExpression` —— 1/10 个有
- `DualCLIPLoader` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `SamplerEulerAncestral` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 10 | 93% |
| 高度 | 25 | 24 - 25 | 10 | 99% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，10 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 24 - 25，10 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
