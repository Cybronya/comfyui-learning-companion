---
name: unknown_workflow_inpaint_lora_sampler_41
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.888
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen image 极速8步局部重绘_1954540019660812289.json, 图片生成/图生图/手脚_面部修复_1986304182204452865.json, 图片生成/文生图/qwen image 极速8步局部重绘_1954486666050334721.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen image 极速8步局部重绘_1954540019660812289.json、图片生成/图生图/手脚_面部修复_1986304182204452865.json、图片生成/文生图/qwen image 极速8步局部重绘_1954486666050334721.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `InpaintCrop` —— 1/3 个有
- `InpaintStitch` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `easy float` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 0.45 | 0.18 - 0.45 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 0.45，观测区间 0.18 - 0.45，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
