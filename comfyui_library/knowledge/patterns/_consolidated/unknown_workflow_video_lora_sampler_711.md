---
name: unknown_workflow_video_lora_sampler_711
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8025
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DisableNoise, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSamplerSelect, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG, easy cleanGpuUsed]
problems: []
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1957470672698142721.json, 图片生成/文生图/1968667688585318402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_711

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1957470672698142721.json、图片生成/文生图/1968667688585318402.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_WriteText` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `SDXLPromptStyler` —— 1/2 个有
- `SeargePromptText` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
