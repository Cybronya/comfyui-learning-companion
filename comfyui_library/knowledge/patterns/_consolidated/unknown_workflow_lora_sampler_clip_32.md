---
name: unknown_workflow_lora_sampler_clip_32
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.814625
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Image Overlay, CR Text Concatenate, CR Overlay Text, easy cleanGpuUsed]
members: [图片生成/文生图/1912452601420677122.json, 图片生成/文生图/1912840766295867394.json, 图片生成/文生图/1914304383847231490.json, 图片生成/文生图/1915672810759589889.json, 图片生成/文生图/1915753087057723394.json, 图片生成/文生图/1918127402818404354.json, 图片生成/文生图/1942467291403464705.json, 图片生成/文生图/1954518475970625537.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1912452601420677122.json、图片生成/文生图/1912840766295867394.json、图片生成/文生图/1914304383847231490.json、图片生成/文生图/1915672810759589889.json、图片生成/文生图/1915753087057723394.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 7/8 个有
- `CR Text` —— 3/8 个有
- `RH_Translator` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `LoadImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `RH_Prompter` —— 2/8 个有
- `Bjornulf_ShowStringText` —— 1/8 个有
- `CR Overlay Text` —— 1/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `Image Overlay` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImageToMask` —— 1/8 个有
- `InvertMask` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Image Overlay、CR Text Concatenate、CR Overlay Text、easy cleanGpuUsed
