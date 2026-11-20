---
name: unknown_workflow_sampler_clip_unet_142
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9686
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图 FLUX 3 Image Klein-_2112067114927480834.json, 图片生成/文生图/文生图Flux2-Klein_2080293479414059009.json, 图片生成/文生图/最新ERNIE-Image-Turbo 文生图_2046566486847787009.json, 图片生成/文生图/治愈极简印象油画风｜日系氛围感风景插画｜温柔治愈扁平厚涂 CG 光影美学_2046565807789969410.json, 图片生成/文生图/猩红共生体变身与感染_2051256128578830338.json, 图片生成/文生图/瓷影墨韵：新中式IP手办设计_2056251017632768001.json, 图片生成/文生图/通义千问Qwen-文生图-8步出图_1959478057306370049.json, 图片生成/文生图/（贞贞版4图版）Qwen 2512 Kook千问美人+真实幻想+极致真实文生图V1_2008746844083462145.json, 平台全量/基米tv-耄耋一键生成器_2038484491727015937.json, 数字人/数字人/Qwen-Image手写体艺术字生成_2072489495907356674.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/文生图 FLUX 3 Image Klein-_2112067114927480834.json、图片生成/文生图/文生图Flux2-Klein_2080293479414059009.json、图片生成/文生图/最新ERNIE-Image-Turbo 文生图_2046566486847787009.json、图片生成/文生图/治愈极简印象油画风｜日系氛围感风景插画｜温柔治愈扁平厚涂 CG 光影美学_2046565807789969410.json、图片生成/文生图/猩红共生体变身与感染_2051256128578830338.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `EmptyFlux2LatentImage` —— 4/10 个有
- `ModelSamplingAuraFlow` —— 4/10 个有
- `CR Prompt Text` —— 2/10 个有
- `CR Text` —— 2/10 个有
- `TTResolutionSelector` —— 2/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 16 | 10 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 16，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
