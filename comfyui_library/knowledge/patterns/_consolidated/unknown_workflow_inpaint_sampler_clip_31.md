---
name: unknown_workflow_inpaint_sampler_clip_31
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.917
common_nodes: [CLIPTextEncode, DualCLIPLoader, ImageStitch, InpaintModelConditioning, KSampler, LoadImage, MaskPreview, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux.1-Krea-遮罩重绘_1951521792307441666.json, 图片生成/图生图/万物移除-字节OneReward-ComfyUI版_1966175482263891969.json, 图片生成/图生图/人物换背景-字节OneReward-ComfyUI版_1966175004364804098.json, 图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux.1-Krea-遮罩重绘_1951521792307441666.json、图片生成/图生图/万物移除-字节OneReward-ComfyUI版_1966175482263891969.json、图片生成/图生图/人物换背景-字节OneReward-ComfyUI版_1966175004364804098.json、图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageStitch`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `ImageAndMaskPreview` —— 2/4 个有
- `ImpactGaussianBlurMask` —— 2/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `InvertMask` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
