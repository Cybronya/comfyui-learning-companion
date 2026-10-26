---
name: unknown_workflow_sampler_clip_vae_59
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.837
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Worker Text2Image_1975809153623003138.json, 图片生成/文生图/Zimage-base_2016353825925373953.json, 图片生成/文生图/中国农村动画风格_1963594349245452289.json, 图片生成/文生图/千问image真实幻想V2文生图_1988091761648115713.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Worker Text2Image_1975809153623003138.json、图片生成/文生图/Zimage-base_2016353825925373953.json、图片生成/文生图/中国农村动画风格_1963594349245452289.json、图片生成/文生图/千问image真实幻想V2文生图_1988091761648115713.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `QwenEditResolution` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `UnetLoaderGGUF` —— 2/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `InversionDemoLazyIndexSwitch` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 4 | 37% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 4 | 58% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，4 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
