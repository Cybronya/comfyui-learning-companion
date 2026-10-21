---
name: unknown_workflow_sampler_clip_unet_94
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.900429
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR SDXL Aspect Ratio, easy cleanGpuUsed, Seed (rgthree)]
members: [图片生成/文生图/1955199580277280770.json, 图片生成/文生图/1955933159051460609.json, 图片生成/文生图/1957737610612670465.json, 图片生成/文生图/1960223327673593857.json, 图片生成/文生图/1985963732088041473.json, 图片生成/文生图/FLUX + LORA 基础工作流_1830939420676771841.json, 图片生成/文生图/人物一致性6宫格小红书风格_1894278785376890882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1955199580277280770.json、图片生成/文生图/1955933159051460609.json、图片生成/文生图/1957737610612670465.json、图片生成/文生图/1960223327673593857.json、图片生成/文生图/1985963732088041473.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 5/7 个有
- `EmptySD3LatentImage` —— 4/7 个有
- `CR SDXL Aspect Ratio` —— 3/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `ApplyFBCacheOnModel` —— 1/7 个有
- `ImageUpscaleWithModelBatched` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio、easy cleanGpuUsed、Seed (rgthree)
