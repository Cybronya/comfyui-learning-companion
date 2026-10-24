---
name: unknown_workflow_inpaint_lora_sampler_15
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.852667
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/26.tonnie-Qwen局部重绘（改中文）_1998076860787490818.json, 图片生成/图生图/29.tonnie-wan2.2最强修手_2001777953891577858.json, 图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json, 图片生成/图生图/Wan修手简单版-手动遮罩_1951207158161584130.json, 图片生成/图生图/qwen image 极速8步局部重绘_1954540019660812289.json, 图片生成/文生图/qwen image 极速8步局部重绘_1954486666050334721.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/26.tonnie-Qwen局部重绘（改中文）_1998076860787490818.json、图片生成/图生图/29.tonnie-wan2.2最强修手_2001777953891577858.json、图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json、图片生成/图生图/Wan修手简单版-手动遮罩_1951207158161584130.json、图片生成/图生图/qwen image 极速8步局部重绘_1954540019660812289.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/6 个有
- `DifferentialDiffusion` —— 3/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `LayerMask: MaskGrow` —— 2/6 个有
- `Mask Fill Holes` —— 2/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `MaskFillHoles` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 10 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 41% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 0.405 | 0.2 - 0.7 | 6 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 0.405，观测区间 0.2 - 0.7，6 个样本
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
