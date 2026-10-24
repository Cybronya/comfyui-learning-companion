---
name: unknown_workflow_sampler_clip_unet_332
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.935333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux+Depth+redux风格迁移控制工作流_1923255138985627650.json, 图片生成/图生图/Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810.json, 图片生成/图生图/最新Redux512深度风格迁移工作流_1921476492218531842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_332

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux+Depth+redux风格迁移控制工作流_1923255138985627650.json、图片生成/图生图/Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810.json、图片生成/图生图/最新Redux512深度风格迁移工作流_1921476492218531842.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `CR Latent Batch Size` —— 2/3 个有
- `CR Prompt Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `Text Concatenate (JPS)` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
