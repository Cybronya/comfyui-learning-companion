---
name: unknown_workflow_lora_sampler_clip_70
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8734
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Engineer-V6_2070131809500884994.json, 图片生成/文生图/Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810.json, 图片生成/文生图/Z-image抖音小红书爆款涨粉美女_2010628888250032130.json, 图片生成/文生图/文生图提示词扩写_2063964617184997378.json, 图片生成/文生图/（墨幽版-高允贞）Krea2文生图加速版V1_2086004168828997634.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image-Engineer-V6_2070131809500884994.json、图片生成/文生图/Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810.json、图片生成/文生图/Z-image抖音小红书爆款涨粉美女_2010628888250032130.json、图片生成/文生图/文生图提示词扩写_2063964617184997378.json、图片生成/文生图/（墨幽版-高允贞）Krea2文生图加速版V1_2086004168828997634.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `ClipLoaderGGUF` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `QwenImageEngineer` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_multistep | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
