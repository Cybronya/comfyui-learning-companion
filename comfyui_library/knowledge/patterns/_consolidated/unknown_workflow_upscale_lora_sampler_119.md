---
name: unknown_workflow_upscale_lora_sampler_119
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.771
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSizeAndCount, KSamplerSelect, LayerUtility: JoyCaption2, LayerUtility: JoyCaption2ExtraOptions, LoadImage, LoraLoader, Preview Chooser, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed Everywhere, ShowText|pysssss, Text Concatenate, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/flux现代都市女_1995513478788079618.json, 图片生成/文生图/flux现代都市男_1995533970475515906.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_119

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux现代都市女_1995513478788079618.json、图片生成/文生图/flux现代都市男_1995533970475515906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `KSamplerSelect`
- `LayerUtility: JoyCaption2`
- `LayerUtility: JoyCaption2ExtraOptions`
- `LoadImage`
- `LoraLoader`
- `Preview Chooser`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `ShowText|pysssss`
- `Text Concatenate`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
