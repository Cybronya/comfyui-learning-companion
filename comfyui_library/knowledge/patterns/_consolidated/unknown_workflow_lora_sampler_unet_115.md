---
name: unknown_workflow_lora_sampler_unet_115
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.882667
common_nodes: [CLIPLoaderGGUF, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UnetLoaderGGUF, VAEDecode, VaeGGUF]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/89-tushengyl_2056374972565770242.json, 图片生成/反推提示词/90tupronghe(本地)_2056617837447434242.json, 图片生成/图生图/02-单图生图_2043581952241967105.json, 图片生成/文生图/01-文生图_2034563277493116930.json, 图片生成/文生图/01-文生图_2042200070795304961.json, 图片生成/文生图/01-文生图新加速_2042830702382682114.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/89-tushengyl_2056374972565770242.json、图片生成/反推提示词/90tupronghe(本地)_2056617837447434242.json、图片生成/图生图/02-单图生图_2043581952241967105.json、图片生成/文生图/01-文生图_2034563277493116930.json、图片生成/文生图/01-文生图_2042200070795304961.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VaeGGUF`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `RTXVideoSuperResolution` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `AnyBooleanSwitch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 83% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1080 | 800 - 1600 | 6 | 78% |
| 高度 | 1920 | 1280 - 2400 | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 800 - 1600，6 个样本
- 高度 中位数 1920，观测区间 1280 - 2400，6 个样本，取值集中（一致性 83%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
