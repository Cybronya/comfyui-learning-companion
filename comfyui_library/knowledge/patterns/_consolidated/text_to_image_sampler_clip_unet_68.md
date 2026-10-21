---
name: text_to_image_sampler_clip_unet_68
type: Text To Image
frequency: 7
level: strong
coverage: 0.873
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/BOOGU测试_2069366790278434817.json, 图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json, 图片生成/文生图/Boogu turbo文生图_2067798697022418945.json, 图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json, 图片生成/文生图/Boogu-Image  Turbo 文生图工作流_2078878116965081089.json, 图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json, 图片生成/文生图/Krea2-风情万种_写实人像（双采版）_2071459488988749825.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/BOOGU测试_2069366790278434817.json、图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json、图片生成/文生图/Boogu turbo文生图_2067798697022418945.json、图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json、图片生成/文生图/Boogu-Image  Turbo 文生图工作流_2078878116965081089.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/7 个有
- `ResolutionSelector` —— 3/7 个有
- `ImageConcanate` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `CR Seed` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `easy promptLine` —— 1/7 个有
- `easy promptList` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | lcm | - | 7 | 71% |
| 调度器 | sgm_uniform | - | 7 | 71% |
| 重绘幅度 | 1 | 0.4 - 1 | 7 | 77% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1536 | 7 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，7 个样本，一致性 71%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，7 个样本
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，7 个样本，取值集中（一致性 80%）
- 高发问题（13/7 个样本）：Steps较低可能导致细节不足
