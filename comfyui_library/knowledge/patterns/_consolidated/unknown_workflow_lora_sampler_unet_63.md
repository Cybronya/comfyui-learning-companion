---
name: unknown_workflow_lora_sampler_unet_63
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.822556
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/93motehuanz(yifuyzhi)_2056985995144417282.json, 图片生成/反推提示词/hyimage_2048278779121901569.json, 图片生成/图生图/qwen image edit 2509_1987811007693262850.json, 图片生成/图生图/人物换装_多图编辑_2032426321309077505.json, 图片生成/图生图/保留衣服细节+自然融入环境=完美换装_2035311130079404034.json, 图片生成/图生图/完美换装工作流：衣服细节保留+和谐融入环境_1989633039712088066.json, 图片生成/图生图/最新qwen image2511双图编辑工作流_2013222102685454337.json, 数字人/数字人/图片先处理2_2056712612838203394.json, 数字人/数字人/图片先处理_2041470058462973953.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/93motehuanz(yifuyzhi)_2056985995144417282.json、图片生成/反推提示词/hyimage_2048278779121901569.json、图片生成/图生图/qwen image edit 2509_1987811007693262850.json、图片生成/图生图/人物换装_多图编辑_2032426321309077505.json、图片生成/图生图/保留衣服细节+自然融入环境=完美换装_2035311130079404034.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 8/9 个有
- `EmptyLatentImage` —— 6/9 个有
- `GetNode` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `CR Text` —— 4/9 个有
- `FluxKontextImageScale` —— 4/9 个有
- `ImageConcanate` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `TextEncodeQwenImageEdit` —— 3/9 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 3/9 个有
- `CFGNorm` —— 2/9 个有
- `CR Prompt Text` —— 2/9 个有
- `ModelSamplingAuraFlow` —— 2/9 个有
- `NunchakuQwenImageDiTLoader` —— 2/9 个有
- `RTXVideoSuperResolution` —— 2/9 个有
- `FluxResolutionNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 512 - 1024 | 6 | 75% |
| 高度 | 1024 | 512 - 1368 | 6 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，6 个样本
- 高度 中位数 1024，观测区间 512 - 1368，6 个样本
- 高发问题（14/9 个样本）：Steps较低可能导致细节不足
