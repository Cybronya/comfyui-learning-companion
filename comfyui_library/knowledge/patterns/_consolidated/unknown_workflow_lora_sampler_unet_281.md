---
name: unknown_workflow_lora_sampler_unet_281
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.768667
common_nodes: [CLIPLoader, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/qwen image2.1-扩图_2110323479294857217.json, 平台全量/人物抠图去背景PNG输出image2.1_2118265013197697025.json, 视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_281

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/qwen image2.1-扩图_2110323479294857217.json、平台全量/人物抠图去背景PNG输出image2.1_2118265013197697025.json、视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetImageSize`
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
- `ImagePadForOutpaint` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `VNCCS_PoseStudio` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 3 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 2384 | 3 | 57% |
| 高度 | 1024 | 1024 - 2560 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2384，3 个样本
- 高度 中位数 1024，观测区间 1024 - 2560，3 个样本
