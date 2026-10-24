---
name: unknown_workflow_sampler_clip_vae_48
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8344
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Worker Text2Image_1975809153623003138.json, 图片生成/文生图/Zimage-base_2016353825925373953.json, 图片生成/文生图/中国农村动画风格_1963594349245452289.json, 图片生成/文生图/千问image真实幻想V2文生图_1988091761648115713.json, 图片生成/文生图/自用测试工作流_2017266041059020802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_48

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Worker Text2Image_1975809153623003138.json、图片生成/文生图/Zimage-base_2016353825925373953.json、图片生成/文生图/中国农村动画风格_1963594349245452289.json、图片生成/文生图/千问image真实幻想V2文生图_1988091761648115713.json、图片生成/文生图/自用测试工作流_2017266041059020802.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `QwenEditResolution` —— 2/5 个有
- `ConcatTextOfUtils` —— 1/5 个有
- `InversionDemoLazyIndexSwitch` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 5 | 21% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 5 | 48% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，5 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，5 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
