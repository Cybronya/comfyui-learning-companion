---
name: unknown_workflow_lora_sampler_unet_75
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPLoader, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, GetImageSize, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2 图像编辑与细节增强_2074460439945244673.json, 图片生成/文生图/krea2风格模仿编辑_2076998609358385153.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_75

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2 图像编辑与细节增强_2074460439945244673.json、图片生成/文生图/krea2风格模仿编辑_2076998609358385153.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `KOOK_SaveJPGImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
