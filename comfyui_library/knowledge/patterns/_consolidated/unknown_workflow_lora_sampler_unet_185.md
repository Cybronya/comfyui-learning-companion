---
name: unknown_workflow_lora_sampler_unet_185
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85325
common_nodes: [CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品融图 Qwen-Image-2.1_2109928283633700866.json, 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2110044236191191041.json, 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json, 视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_185

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/产品融图 Qwen-Image-2.1_2109928283633700866.json、图片生成/图生图/抠图去背景-Qwen image2.1编辑_2110044236191191041.json、图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json、视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `MUTOU_SmartAspectRatio` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `Text Dictionary Convert` —— 1/4 个有
- `Text Dictionary Get` —— 1/4 个有
- `VNCCS_PoseStudio` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16.5 | 8 - 40 | 4 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16.5，观测区间 8 - 40，4 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
