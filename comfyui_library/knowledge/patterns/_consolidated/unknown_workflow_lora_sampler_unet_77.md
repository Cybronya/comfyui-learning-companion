---
name: unknown_workflow_lora_sampler_unet_77
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.957333
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/宠物包装-右前方俯视角_2085243313585741825.json, 图片生成/图生图/智能多角度图生图工作流_2011806565329801218.json, 图片生成/图生图/智能多角度生成【plus】_2009814484990300162.json, 图片生成/图生图/智能多角度生成【plus】_2010736091204161537.json, 图片生成/图生图/智能多角度生成【plus】_2043579135452254210.json, 图片生成/图生图/智能多角度生成【plus】多角度生产物品图片_2013612910664224769.json, 图片生成/图生图/智能多角度生成安静自用_2022270442819555330.json, 图片生成/图生图/镜头多角度控制_2031384378806378498.json, 图片生成/图生图/镜头多角度控制多控制版本_2038813267946119170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_77

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/宠物包装-右前方俯视角_2085243313585741825.json、图片生成/图生图/智能多角度图生图工作流_2011806565329801218.json、图片生成/图生图/智能多角度生成【plus】_2009814484990300162.json、图片生成/图生图/智能多角度生成【plus】_2010736091204161537.json、图片生成/图生图/智能多角度生成【plus】_2043579135452254210.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 8/9 个有
- `CR Text` —— 1/9 个有
- `Image Overlay` —— 1/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/9 个有
- `图像缩放V2_孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 9 | 100% |
| 高度 | 720 | 720 - 720 | 9 | 100% |
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，9 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
