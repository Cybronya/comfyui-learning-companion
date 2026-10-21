---
name: unknown_workflow_lora_sampler_unet_54
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.688667
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, LoraLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/服装_床品_地毯花纹一键提取！QwenImageEdit2511工作流详解，小白友好+全节点注释_2059565759478718465.json, 图片生成/文生图/设计师必备ComfyUI工作流：实物照片→干净印花，全节点手把手注释_2059565790445260801.json, 图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/服装_床品_地毯花纹一键提取！QwenImageEdit2511工作流详解，小白友好+全节点注释_2059565759478718465.json、图片生成/文生图/设计师必备ComfyUI工作流：实物照片→干净印花，全节点手把手注释_2059565790445260801.json、图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.5 | 0.8 - 1.5 | 3 | 74% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.4 - 1 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1.5，观测区间 0.8 - 1.5，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
