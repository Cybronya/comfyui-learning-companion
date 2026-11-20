---
name: unknown_workflow_inpaint_clip_unet_3
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85025
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImagePadForOutpaint, InpaintModelConditioning, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/{sy)FLUX fill 无敌扩图流_2066454152284295170.json, 图片生成/图生图/▶Flux_fill扩图流_1956298639385743361.json, 图片生成/图生图/【大厂同款】Flux扩图Pro升级版_1912326739530346497.json, 图片生成/图生图/工作流基础系列17-FLUX-Fill局部编辑工作流_2047640006629527554.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/{sy)FLUX fill 无敌扩图流_2066454152284295170.json、图片生成/图生图/▶Flux_fill扩图流_1956298639385743361.json、图片生成/图生图/【大厂同款】Flux扩图Pro升级版_1912326739530346497.json、图片生成/图生图/工作流基础系列17-FLUX-Fill局部编辑工作流_2047640006629527554.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `ImageCrop+` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 30 | 4 | 0% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 30，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
