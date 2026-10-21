---
name: unknown_workflow_upscale_lora_sampler_39
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8925
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, ImageUpscaleWithModel, JjkText, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux模型 电商展台三维渲染效果_1826079381268639745.json, 图片生成/文生图/图生图加文本（FLUX GGUF+LoRA）_1832761199178993666.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux模型 电商展台三维渲染效果_1826079381268639745.json、图片生成/文生图/图生图加文本（FLUX GGUF+LoRA）_1832761199178993666.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LayerColor: ColorBalance` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.72) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |
| LoRA 模型强度 | 0.875 | - | 2 | 86% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | euler_ancestral | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 0.45 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.875，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
