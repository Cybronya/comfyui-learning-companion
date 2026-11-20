---
name: unknown_workflow_lora_sampler_unet_177
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问2511GGUF-单双三图参考_2026470669629792258.json, 图片生成/图生图/千问漫剧改图专用_2004540596394098689.json, 图片生成/图生图/表情包九宫格_2115260445140537345.json, 图片生成/图生图/角色四视图_2115256195563999233.json, 图片生成/图生图/👾怪獸Qwen-Edit-2511单图多图编辑👾_2003830705392107521.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_177

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/千问2511GGUF-单双三图参考_2026470669629792258.json、图片生成/图生图/千问漫剧改图专用_2004540596394098689.json、图片生成/图生图/表情包九宫格_2115260445140537345.json、图片生成/图生图/角色四视图_2115256195563999233.json、图片生成/图生图/👾怪獸Qwen-Edit-2511单图多图编辑👾_2003830705392107521.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 4/5 个有
- `AnyBooleanSwitch` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 5 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
