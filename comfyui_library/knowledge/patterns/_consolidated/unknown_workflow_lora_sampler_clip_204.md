---
name: unknown_workflow_lora_sampler_clip_204
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.769333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/-全能图片V1自定义图片尺寸_1963439057818849281.json, 图片生成/文生图/数字CG风格，UES渲染，超广角构图，充满神秘感且细节繁复的云雾缭绕（文生图学员练习版）+全节点注释_2046180250597466114.json, 图片生成/文生图/智趣云课（文生图学员练习版）_2046152098273828865.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/-全能图片V1自定义图片尺寸_1963439057818849281.json、图片生成/文生图/数字CG风格，UES渲染，超广角构图，充满神秘感且细节繁复的云雾缭绕（文生图学员练习版）+全节点注释_2046180250597466114.json、图片生成/文生图/智趣云课（文生图学员练习版）_2046152098273828865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `CR Aspect Ratio` —— 1/3 个有
- `PreviewBridge` —— 1/3 个有
- `RH_Nano_Banana_Image2Image` —— 1/3 个有
- `String Literal` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
