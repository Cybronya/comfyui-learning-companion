---
name: unknown_workflow_sampler_clip_unet_321
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9182
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX.1_wavespeed加速_1879188150349193218.json, 平台全量/Flux lora realism_1863847934600347650.json, 平台全量/Flux+摄影光影_1838475981622329346.json, 平台全量/Flux模型+LoRA_1866390511366860802.json, 平台全量/扁平风格插画设计_1856646200937369602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_321

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/FLUX.1_wavespeed加速_1879188150349193218.json、平台全量/Flux lora realism_1863847934600347650.json、平台全量/Flux+摄影光影_1838475981622329346.json、平台全量/Flux模型+LoRA_1866390511366860802.json、平台全量/扁平风格插画设计_1856646200937369602.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `Int Literal` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `ApplyFBCacheOnModel` —— 1/5 个有
- `EnhancedCompileModel` —— 1/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `String Literal` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 768 - 1024 | 5 | 88% |
| 高度 | 1216 | 1024 - 1344 | 5 | 91% |
| LoRA 模型强度 | 0.7 | - | 1 | 100% |
| LoRA 文本强度 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 768 - 1024，5 个样本，取值集中（一致性 88%）
- 高度 中位数 1216，观测区间 1024 - 1344，5 个样本，取值集中（一致性 91%）
