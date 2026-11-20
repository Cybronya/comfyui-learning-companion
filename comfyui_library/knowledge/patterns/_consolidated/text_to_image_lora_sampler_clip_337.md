---
name: text_to_image_lora_sampler_clip_337
type: Text To Image
frequency: 6
level: moderate
coverage: 0.692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, KSampler, LoraLoaderModelOnly, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenImage_Edit_满血版-8步生图_1958022139515482113.json, 图片生成/图生图/千问双图QwenImage_Edit_2509-8步双图版_1972574913502572546.json, 图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json, 图片生成/文生图/Z-image-暗黑浮世绘_1997401855502258178.json, 图片生成/文生图/Z-image文生图工作流_2009195465652314113.json, 平台全量/Z-image文生图工作流_2027042272457527298.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_337

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/QwenImage_Edit_满血版-8步生图_1958022139515482113.json、图片生成/图生图/千问双图QwenImage_Edit_2509-8步双图版_1972574913502572546.json、图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json、图片生成/文生图/Z-image-暗黑浮世绘_1997401855502258178.json、图片生成/文生图/Z-image文生图工作流_2009195465652314113.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `String Literal` —— 2/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/6 个有
- `easy seed` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 12 | 6 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 53% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 808 | 512 - 1080 | 6 | 71% |
| 高度 | 1080 | 512 - 1920 | 6 | 51% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 12，6 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 808，观测区间 512 - 1080，6 个样本
- 高度 中位数 1080，观测区间 512 - 1920，6 个样本
