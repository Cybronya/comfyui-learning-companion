---
name: unknown_workflow_sampler_clip_unet_29
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.944043
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json, 图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json, 图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json, 图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json, 图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json, 图片生成/文生图/Flux2 Klein 文生图_2025932476836749314.json, 图片生成/文生图/Flux2 Klein 文生图_2028304337616769026.json, 图片生成/文生图/Flux2 Klein 文生图_2070321896603873281.json, 图片生成/文生图/Flux2 Klein 文生图_2070323795138801666.json, 图片生成/文生图/Flux2 Klein 文生图_2070331931929178114.json, 图片生成/文生图/Flux2_Klein 文生图9B版-官方版-4步_2012020314640748545.json, 图片生成/文生图/Flux2文生图工作流_1993530593369587713.json, 图片生成/文生图/Flux2文生图工作流_1993542491129446401.json, 图片生成/文生图/Flux3_Klein图像编辑工作流_2111476889922662402.json, 图片生成/文生图/danotebook-ernie-image-turbo_2062464622694854657.json, 图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json, 图片生成/文生图/flux2.0_1995304483615858689.json, 图片生成/文生图/【遇见AI】ernie-image-turbo文生图_2046172974834786305.json, 图片生成/文生图/【遇见AI】ernie-image文生图_2046172899383447554.json, 图片生成/文生图/最新ERNIE-Image-Turbo 文生图_2046566486847787009.json, 图片生成/文生图/治愈极简印象油画风｜日系氛围感风景插画｜温柔治愈扁平厚涂 CG 光影美学_2046565807789969410.json, 图片生成/文生图/鞋履_1914548552176205826.json, 图片生成/文生图/鞋履_2040302614029537281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json、图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json、图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json、图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json、图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 22/23 个有
- `CR Text` —— 8/23 个有
- `FluxGuidance` —— 5/23 个有
- `LoadImage` —— 5/23 个有
- `FlexLoraLoaderModelOnly` —— 2/23 个有
- `Int` —— 2/23 个有
- `ReferenceMultiLatent` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 22 | 23 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 23 | 46% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 22，23 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，23 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（13/23 个样本）：Steps较低可能导致细节不足
