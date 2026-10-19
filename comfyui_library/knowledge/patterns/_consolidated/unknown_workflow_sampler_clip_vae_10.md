---
name: unknown_workflow_sampler_clip_vae_10
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.836667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Image Overlay, CR Text Concatenate]
members: [图片生成/文生图/1909949768628666370.json, 图片生成/文生图/1911400407372103681.json, 图片生成/文生图/1912452601420677122.json, 图片生成/文生图/1912840766295867394.json, 图片生成/文生图/1918127402818404354.json, 图片生成/文生图/1954524753786761217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1909949768628666370.json、图片生成/文生图/1911400407372103681.json、图片生成/文生图/1912452601420677122.json、图片生成/文生图/1912840766295867394.json、图片生成/文生图/1918127402818404354.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `NunchakuFluxLoraLoader` —— 5/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `ModelSamplingFlux` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `RH_Prompter` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `Bjornulf_ShowStringText` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `Image Overlay` —— 1/6 个有
- `ImageToMask` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Image Overlay、CR Text Concatenate
