---
name: text_to_image_sampler_clip_unet_112
type: Text To Image
frequency: 6
level: strong
coverage: 0.858333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 Turbo风格迁移（双采反推版）_2070847946253496321.json, 图片生成/图生图/Krea2-trubo-洗图_2069945131855343618.json, 图片生成/图生图/Krea2-trubo-洗图工作流_2069770345149718529.json, 图片生成/图生图/boogu-trubo-洗图工作流_2069767095663030273.json, 图片生成/文生图/Krea2 Turbo风格迁移（双采反推版）_2070490329257697282.json, 图片生成/文生图/百度ERNIE-image 人像文生图 【 提示词尺寸优化版 】_2044598172412022786.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2 Turbo风格迁移（双采反推版）_2070847946253496321.json、图片生成/图生图/Krea2-trubo-洗图_2069945131855343618.json、图片生成/图生图/Krea2-trubo-洗图工作流_2069770345149718529.json、图片生成/图生图/boogu-trubo-洗图工作流_2069767095663030273.json、图片生成/文生图/Krea2 Turbo风格迁移（双采反推版）_2070490329257697282.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `llama_cpp_parameters` —— 3/6 个有
- `PreviewAny` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `ImpactSwitch` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 6 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 50% |
| 重绘幅度 | 1 | 0.4 - 1 | 6 | 65% |
| 宽度 | 1024 | 720 - 1024 | 6 | 88% |
| 高度 | 1280 | 1024 - 1280 | 6 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，6 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，6 个样本
- 宽度 中位数 1024，观测区间 720 - 1024，6 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 1024 - 1280，6 个样本，取值集中（一致性 90%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
