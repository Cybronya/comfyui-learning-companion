---
name: unknown_workflow_sampler_clip_unet_104
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.988917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json, 图片生成/文生图/（官方版）Qwen Image文生图V1_1952787828896952322.json, 图片生成/文生图/（官方版）Qwen Image文生图（媲美即梦）_1953287044091023361.json, 图片生成/文生图/（电商娱乐流）z image turbo 文生图基础工作流_2052286821991755777.json, 平台全量/Qwen Image 2512 商业商品摄影 LoRA｜单品棚拍_2091193349645627394.json, 平台全量/ins手持特写LoRA-穿戴甲商品摄影工作流_2094580320019501057.json, 平台全量/二番剧风_2019018287450951681.json, 平台全量/测试_2117856801151606785.json, 平台全量/纯白底美甲摆拍-穿戴甲产品图工作流_2094436860461412353.json, 数字人/数字人/万圣节萌系插画-文生图_2093977653907902466.json, 数字人/数字人/中秋萌系插画-文生图_2093973513794318337.json, 数字人/数字人/文生图-Qwen2512-6步-模板_2026856696487878658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_104

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json、图片生成/文生图/（官方版）Qwen Image文生图V1_1952787828896952322.json、图片生成/文生图/（官方版）Qwen Image文生图（媲美即梦）_1953287044091023361.json、图片生成/文生图/（电商娱乐流）z image turbo 文生图基础工作流_2052286821991755777.json、平台全量/Qwen Image 2512 商业商品摄影 LoRA｜单品棚拍_2091193349645627394.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 8/12 个有
- `ModelSamplingAuraFlow` —— 7/12 个有
- `ImageScaleBy` —— 2/12 个有
- `VAEEncode` —— 2/12 个有
- `PrimitiveInt` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 8 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |
| 采样步数 | 20 | 6 - 50 | 12 | 42% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4.5 | 12 | 50% |
| 采样算法 | euler | - | 12 | 58% |
| 调度器 | sgm_uniform | - | 12 | 50% |
| 重绘幅度 | 1 | 0.4 - 1 | 12 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，8 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 6 - 50，12 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4.5，12 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 euler，12 个样本，一致性 58%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，12 个样本
