---
name: unknown_workflow_sampler_clip_unet_178
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.97925
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图 FLUX 3 Image Klein-_2112067114927480834.json, 图片生成/文生图/文生图Flux2-Klein_2080293479414059009.json, 图片生成/文生图/最新ERNIE-Image-Turbo 文生图_2046566486847787009.json, 图片生成/文生图/治愈极简印象油画风｜日系氛围感风景插画｜温柔治愈扁平厚涂 CG 光影美学_2046565807789969410.json, 图片生成/文生图/空白工作流_2033896316320882689.json, 图片生成/文生图/鞋履_1914548552176205826.json, 图片生成/文生图/鞋履_2040302614029537281.json, 图片生成/文生图/黑森林Flux2文生图_1993588775534133249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_178

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/文生图 FLUX 3 Image Klein-_2112067114927480834.json、图片生成/文生图/文生图Flux2-Klein_2080293479414059009.json、图片生成/文生图/最新ERNIE-Image-Turbo 文生图_2046566486847787009.json、图片生成/文生图/治愈极简印象油画风｜日系氛围感风景插画｜温柔治愈扁平厚涂 CG 光影美学_2046565807789969410.json、图片生成/文生图/空白工作流_2033896316320882689.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `CR Text` —— 2/8 个有
- `FlexLoraLoaderModelOnly` —— 2/8 个有
- `FluxGuidance` —— 2/8 个有
- `TTResolutionSelector` —— 2/8 个有
- `EmptySD3LatentImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | 6 - 20 | 8 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 18，观测区间 6 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
