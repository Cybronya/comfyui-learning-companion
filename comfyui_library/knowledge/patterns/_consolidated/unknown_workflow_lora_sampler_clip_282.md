---
name: unknown_workflow_lora_sampler_clip_282
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/提示词推导生图_1928412918549725186.json, 图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_282

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/提示词推导生图_1928412918549725186.json、图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `String Replace (mtb)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | - | 2 | 62% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 928，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
