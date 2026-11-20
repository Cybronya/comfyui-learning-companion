---
name: unknown_workflow_upscale_lora_sampler_148
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, ImageResize+, ImageUpscaleWithModel, JjkText, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SaveImage, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/图生图加文本（FLUX GGUF+LoRA）_1832761199178993666.json, 平台全量/中秋月饼_1832779175991357442.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_148

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/图生图加文本（FLUX GGUF+LoRA）_1832761199178993666.json、平台全量/中秋月饼_1832779175991357442.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 75% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
