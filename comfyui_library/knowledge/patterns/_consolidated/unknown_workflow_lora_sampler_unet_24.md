---
name: unknown_workflow_lora_sampler_unet_24
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.908
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, SDXL Empty Latent Image]
members: [图片生成/图生图/2044054645772918786.json, 图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json, 图片生成/文生图/人物三视图-高一致性_2062129476934389761.json, 图片生成/文生图/单图编辑_2003615026718121985.json, 图片生成/文生图/多图编辑_2003474271924043777.json, 数字人/数字人/免费 开源 2511 角色设计+数字人 三视图真人动漫人物一致性_2101744942149357570.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_24

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2044054645772918786.json、图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json、图片生成/文生图/人物三视图-高一致性_2062129476934389761.json、图片生成/文生图/单图编辑_2003615026718121985.json、图片生成/文生图/多图编辑_2003474271924043777.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/6 个有
- `EmptySD3LatentImage` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `SDXL Empty Latent Image` —— 3/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `Textbox` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 6 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，6 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、SDXL Empty Latent Image
