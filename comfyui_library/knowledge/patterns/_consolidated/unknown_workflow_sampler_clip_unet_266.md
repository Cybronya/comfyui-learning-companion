---
name: unknown_workflow_sampler_clip_unet_266
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.966
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/给女生画上小丑装_1921490291654852610.json, 平台全量/fill+redux-扩图_1923314936125321217.json, 平台全量/flux去水印工作流_1928437167486357506.json, 平台全量/redux+ace换装_1923306424787791874.json, 平台全量/redux+vae内补-给女生换装_1923283621157720065.json, 平台全量/redux-fill-换装_1923297122022846465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_266

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/给女生画上小丑装_1921490291654852610.json、平台全量/fill+redux-扩图_1923314936125321217.json、平台全量/flux去水印工作流_1928437167486357506.json、平台全量/redux+ace换装_1923306424787791874.json、平台全量/redux+vae内补-给女生换装_1923283621157720065.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 5/6 个有
- `FluxGuidance` —— 5/6 个有
- `InpaintModelConditioning` —— 5/6 个有
- `ReduxAdvanced` —— 5/6 个有
- `StyleModelLoader` —— 5/6 个有
- `CLIPVisionLoader` —— 4/6 个有
- `ImagePadForOutpaint` —— 2/6 个有
- `AdvancedVisionLoader` —— 1/6 个有
- `ClipInterrogator` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `VAEEncodeForInpaint` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 32% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 83% |
| 重绘幅度 | 1 | 0.8 - 1 | 6 | 92% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 92%）
