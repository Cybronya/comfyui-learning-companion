---
name: unknown_workflow_lora_sampler_clip_323
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7975
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SDXLEmptyLatentSizePicker+, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy promptConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/沙雕动漫超火古风人物加速_1966870624557731842.json, 图片生成/文生图/简笔画动漫人物三视图多视图超清_开高清放大_1970684621732147201.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_323

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/沙雕动漫超火古风人物加速_1966870624557731842.json、图片生成/文生图/简笔画动漫人物三视图多视图超清_开高清放大_1970684621732147201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Upscale Image` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `NunchakuQwenImageDiTLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
