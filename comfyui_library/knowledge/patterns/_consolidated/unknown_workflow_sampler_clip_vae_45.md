---
name: unknown_workflow_sampler_clip_vae_45
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8652
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, JjkText, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/文生图 ｜ 3D动漫玩偶三视图_1933875714414268417.json, 图片生成/文生图/Flux文生图-基础版_1889856882952089601.json, 图片生成/文生图/Flux模型 电商展台三维渲染效果_1826079381268639745.json, 图片生成/文生图/一键气球文字效果_2036273645370216450.json, 图片生成/文生图/一键气球文字效果_2037774758560931841.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_45

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/文生图 ｜ 3D动漫玩偶三视图_1933875714414268417.json、图片生成/文生图/Flux文生图-基础版_1889856882952089601.json、图片生成/文生图/Flux模型 电商展台三维渲染效果_1826079381268639745.json、图片生成/文生图/一键气球文字效果_2036273645370216450.json、图片生成/文生图/一键气球文字效果_2037774758560931841.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `JjkText`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `ImageUpscaleWithModel` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `Label (rgthree)` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `FluxGuidance` —— 2/5 个有
- `FluxResolutionNode` —— 2/5 个有
- `Int Literal` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ModelSamplingFlux` —— 2/5 个有
- `KSampler` —— 1/5 个有
- `LayerColor: ColorBalance` —— 1/5 个有
- `SDXLEmptyLatentSizePicker+` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.875 | - | 2 | 86% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 832 | 512 - 1024 | 4 | 77% |
| 高度 | 1216 | 1 - 1280 | 5 | 40% |
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
- 宽度 中位数 832，观测区间 512 - 1024，4 个样本
- 高度 中位数 1216，观测区间 1 - 1280，5 个样本，取值分散，一致性仅 40%
