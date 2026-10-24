---
name: text_to_image_lora_sampler_clip_579
type: Text To Image
frequency: 2
level: weak
coverage: 0.735
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, ImageLoader, JoinStringMulti, KSampler, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, SetNode, ShowText|pysssss, String, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy convertAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-image美女一致性自动洗图和自动去水印工作流，适合抖音、快手等自媒体平台大量出图_2012830979110473729.json, 图片生成/图生图/黛玉妹妹Z-IMAGE-lora-图生图，适合抖音快手头条等平台_2019998492009172994.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_579

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image美女一致性自动洗图和自动去水印工作流，适合抖音、快手等自媒体平台大量出图_2012830979110473729.json、图片生成/图生图/黛玉妹妹Z-IMAGE-lora-图生图，适合抖音快手头条等平台_2019998492009172994.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `ImageLoader`
- `JoinStringMulti`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `String`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1500 | - | 2 | 72% |
| 高度 | 1500 | - | 2 | 72% |
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1500，样本不足，未给区间，2 个样本
- 高度 中位数 1500，样本不足，未给区间，2 个样本
- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
