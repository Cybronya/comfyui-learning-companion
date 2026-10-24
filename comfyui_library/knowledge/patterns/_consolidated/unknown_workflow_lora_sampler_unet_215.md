---
name: unknown_workflow_lora_sampler_unet_215
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.640333
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, Easy_QwenEdit2509, GetNode, ImageScaleToTotalPixels, JDCN_StringToList, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, SetNode, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-edit2511人物一致性多姿态多角度出图_2064657602591682562.json, 图片生成/图生图/一键16张Coser写真姿势_2028695545153331201.json, 图片生成/图生图/一键16张Coser写真姿势（首创）2511_2028157821224755201.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_215

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen-edit2511人物一致性多姿态多角度出图_2064657602591682562.json、图片生成/图生图/一键16张Coser写真姿势_2028695545153331201.json、图片生成/图生图/一键16张Coser写真姿势（首创）2511_2028157821224755201.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `Easy_QwenEdit2509`
- `GetNode`
- `ImageScaleToTotalPixels`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `SetNode`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResizeImagesByLongerEdge` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2m | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
