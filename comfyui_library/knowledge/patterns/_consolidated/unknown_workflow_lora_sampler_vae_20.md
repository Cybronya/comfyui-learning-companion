---
name: unknown_workflow_lora_sampler_vae_20
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, GGUFLoaderKJ, ImageScaleToTotalPixels, KSampler, Label (rgthree), LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, Text Load Line From File, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物15个多视角生成_2008060893489270786.json, 图片生成/图生图/人物15个多视角生成（数据集必备）_1995334886917595138.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物15个多视角生成_2008060893489270786.json、图片生成/图生图/人物15个多视角生成（数据集必备）_1995334886917595138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `GGUFLoaderKJ`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Text Load Line From File`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
