---
name: unknown_workflow_sampler_clip_unet_100
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.972571
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/墨沫白皙质感Z -Image工作流_2067629087857926145.json, 图片生成/文生图/大洋IP形象的应用_2063092530673184769.json, 图片生成/文生图/文生图片_2061325270497456129.json, 图片生成/文生图/文生图片（Z-image)_2077687725708374017.json, 图片生成/文生图/文生图（解禁模型）：z-image-turbo_2057705249091178498.json, 图片生成/文生图/阿里Z-image，人像真实感拉满_1993853665350008834.json, 图片生成/文生图/🤖Z-image小钢炮来袭！[随机性增强]_1999663045167153154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_100

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/墨沫白皙质感Z -Image工作流_2067629087857926145.json、图片生成/文生图/大洋IP形象的应用_2063092530673184769.json、图片生成/文生图/文生图片_2061325270497456129.json、图片生成/文生图/文生图片（Z-image)_2077687725708374017.json、图片生成/文生图/文生图（解禁模型）：z-image-turbo_2057705249091178498.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/7 个有
- `CR Text` —— 2/7 个有
- `ImpactInt` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `Fast Bypasser (rgthree)` —— 1/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `easy promptList` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1920 | 7 | 65% |
| 高度 | 1536 | 1080 - 1920 | 7 | 79% |
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 10 | 7 | 95% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler_ancestral | - | 7 | 43% |
| 重绘幅度 | sgm_uniform | - | 7 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1920，7 个样本
- 高度 中位数 1536，观测区间 1080 - 1920，7 个样本
- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 10，7 个样本，取值集中（一致性 95%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，7 个样本，一致性 43%
- 重绘幅度 最常用 sgm_uniform，7 个样本，一致性 57%
