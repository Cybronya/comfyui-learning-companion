---
name: text_to_image_lora_sampler_clip_553
type: Text To Image
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EasyCache, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】 字节跳动 Flux USO 主体一致性编辑生图工作流_1964627667322552322.json, 平台全量/【阡陌】 字节跳动 Flux USO 主体+单图_多图风格参考生图工作流_1964634724960452609.json, 平台全量/【阡陌】 字节跳动 Flux USO 单图_多图风格参考生图工作流_1964662986759618562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_553

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【阡陌】 字节跳动 Flux USO 主体一致性编辑生图工作流_1964627667322552322.json、平台全量/【阡陌】 字节跳动 Flux USO 主体+单图_多图风格参考生图工作流_1964634724960452609.json、平台全量/【阡陌】 字节跳动 Flux USO 单图_多图风格参考生图工作流_1964662986759618562.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EasyCache`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToMaxDimension` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `workflow>USO STYLE` —— 2/3 个有
- `FluxGuidance` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `workflow>uso引导` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
