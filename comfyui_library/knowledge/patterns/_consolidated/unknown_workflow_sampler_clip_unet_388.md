---
name: unknown_workflow_sampler_clip_unet_388
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.751667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json, 图片生成/文生图/In-Context-Lora_1943610986538692609.json, 图片生成/文生图/InContextLoRa通用流(合集）_1938790150803480577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_388

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json、图片生成/文生图/In-Context-Lora_1943610986538692609.json、图片生成/文生图/InContextLoRa通用流(合集）_1938790150803480577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `LoadImageFromUrl` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `CR Image Size` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `TextCombinerSix` —— 1/3 个有
- `TextToNumber` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
