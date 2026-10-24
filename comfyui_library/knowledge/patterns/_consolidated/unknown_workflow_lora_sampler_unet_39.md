---
name: unknown_workflow_lora_sampler_unet_39
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.780417
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2509 anything2real 动漫转真实-八步生图-娱乐向_1989715291422814210.json, 图片生成/图生图/Qwen 2511 anything2real 动漫转真实_2009089869389242369.json, 图片生成/图生图/Qwen 2511 人物一致性动作迁移 _ 加速版_2076166581280919554.json, 图片生成/图生图/Qwen 2511 换背景+局部重绘+单图编辑背景无偏移_2008885767828934658.json, 图片生成/图生图/Qwen Edit 2511 动漫风格转换V1_2005633486033743874.json, 图片生成/图生图/Qwen Edit 2511 双图编辑V1（一致性加强版）_2003801552768933889.json, 图片生成/图生图/Qwen Edit 2511 双图编辑【一致性加强版】电商_摄影等_2004002137615048706.json, 图片生成/图生图/Qwen Edit 2511蒙版+图像编辑V1(无偏移)_2003798966443646977.json, 图片生成/图生图/Qwen+Edit+2511+双图编辑【一致性加强版】电商_2005266637362266113.json, 图片生成/图生图/Qwen-Edit-2509 Utils 2.2 Optional Mask（局部重绘+遮罩）_1989853315464916993.json, 图片生成/图生图/Qwen2509无遮罩换装 一致性_1990289777809387521.json, 图片生成/图生图/千问换装【全自动换装+超强一致性_带遮罩】_2042926037226491906.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_39

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen 2509 anything2real 动漫转真实-八步生图-娱乐向_1989715291422814210.json、图片生成/图生图/Qwen 2511 anything2real 动漫转真实_2009089869389242369.json、图片生成/图生图/Qwen 2511 人物一致性动作迁移 _ 加速版_2076166581280919554.json、图片生成/图生图/Qwen 2511 换背景+局部重绘+单图编辑背景无偏移_2008885767828934658.json、图片生成/图生图/Qwen Edit 2511 动漫风格转换V1_2005633486033743874.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 11/12 个有
- `QwenEditConfigPreparer` —— 11/12 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 11/12 个有
- `CropWithPadInfo` —— 10/12 个有
- `QwenEditAdaptiveLongestEdge` —— 10/12 个有
- `QwenEditOutputExtractor` —— 10/12 个有
- `ImageScaleBy` —— 8/12 个有
- `PreviewImage` —— 7/12 个有
- `ImageConcanate` —— 3/12 个有
- `GetNode` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `AIO_Preprocessor` —— 1/12 个有
- `CR Text` —— 1/12 个有
- `GrowMask` —— 1/12 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/12 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `MaskPreview` —— 1/12 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 12 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | beta57 | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 beta57，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
