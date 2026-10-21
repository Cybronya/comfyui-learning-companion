---
name: text_to_image_video_lora_sampler_193
type: Text To Image
frequency: 2
level: weak
coverage: 0.989
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, EmptyHunyuanLatentVideo, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, KSamplerSelect, KSamplerWithNAG, LoadImageOutput, LoraLoader, ModelSamplingSD3, NAGCFGGuider, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, T5TokenizerOptions, TripleCLIPLoader, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/1948704905335844866.json, 视频生成/文生视频/NAG-扩散模型的通用负向引导_2072999668357046272.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_193

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1948704905335844866.json、视频生成/文生视频/NAG-扩散模型的通用负向引导_2072999668357046272.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `KSamplerSelect`
- `KSamplerWithNAG`
- `LoadImageOutput`
- `LoraLoader`
- `ModelSamplingSD3`
- `NAGCFGGuider`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T5TokenizerOptions`
- `TripleCLIPLoader`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | 6 | - | 2 | 100% |
| 调度器 | 2.5 | - | 2 | 100% |
| 重绘幅度 | 0.25 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 2.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 0.25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
