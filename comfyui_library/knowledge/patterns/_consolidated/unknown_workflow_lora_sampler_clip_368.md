---
name: unknown_workflow_lora_sampler_clip_368
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.851
common_nodes: [Bus Node, CLIPSetLastLayer, CLIPTextEncode, CR SDXL Aspect Ratio, CheckpointLoaderSimple, KSampler, LoraLoader, PlaySound|pysssss, SaveImage, Seed (rgthree), ShowText|pysssss, Text Concatenate, VAEDecode]
problems: []
missing: []
members: [平台全量/Inspiration finder for Jewelry-makers & Clients_1887383424712204290.json, 平台全量/珠宝制作灵感生成器_1778262170623074305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_368

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Inspiration finder for Jewelry-makers & Clients_1887383424712204290.json、平台全量/珠宝制作灵感生成器_1778262170623074305.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Bus Node`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoraLoader`
- `PlaySound|pysssss`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `Text Concatenate`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `IterativeLatentUpscale` —— 1/2 个有
- `PixelKSampleUpscalerProvider` —— 1/2 个有
- `Text Random Line` —— 1/2 个有
- `TextBox` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.7 | - | 2 | 100% |
| LoRA 文本强度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
