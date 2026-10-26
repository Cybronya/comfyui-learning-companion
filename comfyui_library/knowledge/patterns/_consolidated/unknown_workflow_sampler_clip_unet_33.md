---
name: unknown_workflow_sampler_clip_unet_33
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.93605
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片反推，生成新图，产品也是_2077336907649998849.json, 图片生成/图生图/电商洗图_文字还原-百度Ernie_image_2045898760097636354.json, 图片生成/文生图/ERNIE-Image-Turbo 光影效果 复杂画面处理 光影新世界_2046939542237749250.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图+全节点注释_2046178570917126145.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图-写实风_2045419438635229186.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图V2_2046063492725215234.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2044675520398368770.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2045014051884896258.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2045473705303740418.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2045490522525016066.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2046849642322731009.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2046910510959955970.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2047124098261721089.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2047139433782190082.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2048685419495170049.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2049035575436513282.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2052282886828638210.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图生成器_2047546071609511937.json, 图片生成/文生图/ERNIE-Image-Turbo文生图，测试用，感觉效果一般般_2046403986416214017.json, 图片生成/文生图/ERNIE-Image灵韵东方 • 文心一格造像师：定格知识增强的跨模态艺术巅峰_2044349388868292609.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/图片反推，生成新图，产品也是_2077336907649998849.json、图片生成/图生图/电商洗图_文字还原-百度Ernie_image_2045898760097636354.json、图片生成/文生图/ERNIE-Image-Turbo 光影效果 复杂画面处理 光影新世界_2046939542237749250.json、图片生成/文生图/ERNIE-Image-Turbo 文生图+全节点注释_2046178570917126145.json、图片生成/文生图/ERNIE-Image-Turbo 文生图-写实风_2045419438635229186.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/20 个有
- `PreviewImage` —— 2/20 个有
- `PrimitiveStringMultiline` —— 2/20 个有
- `RH_LLMAPI_Pro_Node` —— 2/20 个有
- `ShowText|pysssss` —— 2/20 个有
- `easy ifElse` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `RH_LLMAPI_NODE` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 20 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，20 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
