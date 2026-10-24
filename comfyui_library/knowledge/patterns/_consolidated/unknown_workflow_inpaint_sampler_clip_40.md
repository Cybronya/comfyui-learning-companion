---
name: unknown_workflow_inpaint_sampler_clip_40
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.831667
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImagePadForOutpaint, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX扩图_1914938088290775041.json, 图片生成/图生图/扩图_1955198486787473409.json, 图片生成/图生图/超简单去水印，秒变竖屏手机版_1903016455229841409.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX扩图_1914938088290775041.json、图片生成/图生图/扩图_1955198486787473409.json、图片生成/图生图/超简单去水印，秒变竖屏手机版_1903016455229841409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `JWImageResizeByLongerSide` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `scale` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 3 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，3 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
