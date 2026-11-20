---
name: unknown_workflow_sampler_clip_unet_73
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.903357
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/flux1_krea_dev 对比 flux dev_1950943932404400129.json, 图片生成/文生图/flux1_krea_dev 很漂亮_1954159231169642497.json, 图片生成/文生图/flux1_krea_dev满血版出图_1951839776326537218.json, 图片生成/文生图/kontext_dev基础文生图_1952701907708088321.json, 图片生成/文生图/z-image滑块系列文生图_2057114517376688130.json, 图片生成/文生图/【茗翠Ai】F.1 krea文生图_1952021213906415618.json, 图片生成/文生图/千问Qwen_image文生图海报_fp8_官方版26125_2015389169786294274.json, 图片生成/文生图/千问文生图快速中文直出2512_2027699940423639041.json, 图片生成/文生图/古风男工作流_2051554347225497601.json, 图片生成/文生图/基础文生图 Z-Image-Turbo（带LoRA加载节点）_2007330137645260802.json, 图片生成/文生图/墨宝映画人物设定_2015364874955657217.json, 图片生成/文生图/工作流基础系列16-FLUX-Krea文生图工作流_2047554003969511425.json, 图片生成/文生图/工作流基础系列4-z image turbo文生图工作流-基础向讲解此工作流_2044389426284990466.json, 图片生成/文生图/组件系列6-Z-image-turbo文生图_2058749993380569090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/flux1_krea_dev 对比 flux dev_1950943932404400129.json、图片生成/文生图/flux1_krea_dev 很漂亮_1954159231169642497.json、图片生成/文生图/flux1_krea_dev满血版出图_1951839776326537218.json、图片生成/文生图/kontext_dev基础文生图_1952701907708088321.json、图片生成/文生图/z-image滑块系列文生图_2057114517376688130.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `CLIPLoader` —— 8/14 个有
- `ModelSamplingAuraFlow` —— 7/14 个有
- `DualCLIPLoader` —— 6/14 个有
- `PreviewImage` —— 3/14 个有
- `Seed (rgthree)` —— 3/14 个有
- `FluxGuidance` —— 2/14 个有
- `easy promptList` —— 2/14 个有
- `easy seed` —— 2/14 个有
- `CR Multiline Text` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 14 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 14 | 31% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，14 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
