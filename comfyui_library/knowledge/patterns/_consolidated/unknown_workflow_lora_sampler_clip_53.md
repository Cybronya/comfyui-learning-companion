---
name: unknown_workflow_lora_sampler_clip_53
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.71175
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageCrop+, CR Text, Note Plus (mtb), SDXLEmptyLatentSizePicker+]
members: [图片生成/文生图/1908149869620375554.json, 图片生成/文生图/1909968900275273729.json, 图片生成/文生图/1910633207707172866.json, 图片生成/文生图/1917844166154321921.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1908149869620375554.json、图片生成/文生图/1909968900275273729.json、图片生成/文生图/1910633207707172866.json、图片生成/文生图/1917844166154321921.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `NunchakuFluxDiTLoader` —— 2/4 个有
- `NunchakuFluxLoraLoader` —— 2/4 个有
- `NunchakuTextEncoderLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SDXLEmptyLatentSizePicker+` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ImageCrop+` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `QuadrupleCLIPLoader` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 28 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | lcm | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：ImageCrop+、CR Text、Note Plus (mtb)、SDXLEmptyLatentSizePicker+
