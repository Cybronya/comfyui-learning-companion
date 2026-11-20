---
name: unknown_workflow_clip_unet_vae_6
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9585
common_nodes: [CLIPLoader, CLIPTextEncode, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json, 图片生成/文生图/Zimage生图-随机增强-两步法_2004931976354299905.json, 图片生成/文生图/danotebook-ernie-image-turbo_2062464622694854657.json, 图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json, 图片生成/文生图/flux.2-klein文生图_2077238073297031169.json, 图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json, 图片生成/文生图/文生图  z-image-turbo_2054380645274660866.json, 图片生成/文生图/文生图片_2061325270497456129.json, 图片生成/文生图/文生图片（Z-image)_2077687725708374017.json, 图片生成/文生图/文生图（解禁模型）：z-image-turbo_2054196239780065281.json, 图片生成/文生图/文生图（解禁模型）：z-image-turbo_2057705249091178498.json, 图片生成/文生图/阿里Z-image，人像真实感拉满_1993853665350008834.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json、图片生成/文生图/Zimage生图-随机增强-两步法_2004931976354299905.json、图片生成/文生图/danotebook-ernie-image-turbo_2062464622694854657.json、图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json、图片生成/文生图/flux.2-klein文生图_2077238073297031169.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `KSamplerAdvanced` —— 8/12 个有
- `EmptyLatentImage` —— 7/12 个有
- `EmptyFlux2LatentImage` —— 5/12 个有
- `KSampler` —— 4/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `MuyeSizeSelector` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 67% |
| Prompt 约束强度(CFG) | 9 | 1 - 25 | 12 | 18% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 12 | 42% |
| 重绘幅度 | sgm_uniform | - | 12 | 58% |
| 宽度 | 1080 | 864 - 1920 | 7 | 69% |
| 高度 | 1536 | 1080 - 1920 | 7 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 9，观测区间 1 - 25，12 个样本，取值分散，一致性仅 18%
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，12 个样本，一致性 42%
- 重绘幅度 最常用 sgm_uniform，12 个样本，一致性 58%
- 宽度 中位数 1080，观测区间 864 - 1920，7 个样本
- 高度 中位数 1536，观测区间 1080 - 1920，7 个样本，取值集中（一致性 82%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
