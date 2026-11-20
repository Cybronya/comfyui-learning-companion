---
name: unknown_workflow_lora_sampler_clip_196
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.842
common_nodes: [CLIPTextEncode, CR Text, ClipLoaderGGUF, ConditioningZeroOut, Dapao_LlamaChat, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, QwenImageEngineer, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-Engineer v6+Dopsd高质量摄影质感文生图_2072864298984108033.json, 图片生成/文生图/Z-image-Engineer v6+Dopsd高质量摄影质感文生图_2073253303030476801.json, 图片生成/文生图/Z-image-Engineer v6+Dopsd高质量摄影质感文生图_2073738996555018241.json, 图片生成/文生图/Z-image-Engineer_v6+Dopsd高质量摄影质感文生图_2116340050672840705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_196

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-Engineer v6+Dopsd高质量摄影质感文生图_2072864298984108033.json、图片生成/文生图/Z-image-Engineer v6+Dopsd高质量摄影质感文生图_2073253303030476801.json、图片生成/文生图/Z-image-Engineer v6+Dopsd高质量摄影质感文生图_2073738996555018241.json、图片生成/文生图/Z-image-Engineer_v6+Dopsd高质量摄影质感文生图_2116340050672840705.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ClipLoaderGGUF`
- `ConditioningZeroOut`
- `Dapao_LlamaChat`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `QwenImageEngineer`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 3/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
