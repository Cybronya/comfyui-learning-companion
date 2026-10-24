---
name: unknown_workflow_sampler_clip_unet_180
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.831429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux3_klein_image_edit图像编辑_2110972221408763906.json, 图片生成/图生图/flux3_klein_image_edit图像编辑_2112068355019599874.json, 图片生成/图生图/【遇见AI】flux3 image 图生图和图片参考_2111309354984108033.json, 图片生成/图生图/图片反推，生成新图，产品也是_2077336907649998849.json, 图片生成/图生图/电商洗图_文字还原-百度Ernie_image_2045898760097636354.json, 图片生成/图生图/（9图）flux3_klein_image_edit图像编辑_2111089818842255361.json, 图片生成/文生图/flux3_image_klein多图编辑_2011011965199589378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_180

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/flux3_klein_image_edit图像编辑_2110972221408763906.json、图片生成/图生图/flux3_klein_image_edit图像编辑_2112068355019599874.json、图片生成/图生图/【遇见AI】flux3 image 图生图和图片参考_2111309354984108033.json、图片生成/图生图/图片反推，生成新图，产品也是_2077336907649998849.json、图片生成/图生图/电商洗图_文字还原-百度Ernie_image_2045898760097636354.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceMultiLatent` —— 5/7 个有
- `TextGenerate` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `EmptyFlux2LatentImage` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `easy ifElse` —— 2/7 个有
- `BatchImagesNode` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 4 - 25 | 7 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 40% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 4 - 25，7 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
