---
name: unknown_workflow_lora_sampler_clip_150
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95225
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UnetLoaderGGUF, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LOGO生成 - Qwen_1993252010327736321.json, 图片生成/文生图/LOGO生成器 Qwen-image Q8+4步Lora极速生成_1954712420105252865.json, 图片生成/文生图/Qwen image 汉字专用海报极速文生图+润色_1954718876200267778.json, 图片生成/文生图/一键LOGO极速生成_2034820251891798017.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/LOGO生成 - Qwen_1993252010327736321.json、图片生成/文生图/LOGO生成器 Qwen-image Q8+4步Lora极速生成_1954712420105252865.json、图片生成/文生图/Qwen image 汉字专用海报极速文生图+润色_1954718876200267778.json、图片生成/文生图/一键LOGO极速生成_2034820251891798017.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `SeedVR2` —— 2/4 个有
- `SeedVR2BlockSwap` —— 2/4 个有
- `CFGZeroStar` —— 1/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 5 | 4 - 5 | 4 | 91% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 5，4 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
