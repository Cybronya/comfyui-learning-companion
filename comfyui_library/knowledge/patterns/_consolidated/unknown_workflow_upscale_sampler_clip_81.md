---
name: unknown_workflow_upscale_sampler_clip_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.537
common_nodes: [CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner, CheckpointLoaderSimple, EmptyLatentImage, ImageUpscaleWithModel, JWInteger, KSampler, KSamplerAdvanced, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, ttN text]
problems: []
missing: []
members: [平台全量/动物贴纸_1816660473877094401.json, 平台全量/放牧的女孩_1808825698842243073.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/动物贴纸_1816660473877094401.json、平台全量/放牧的女孩_1808825698842243073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeSDXL`
- `CLIPTextEncodeSDXLRefiner`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `ttN text`

**可变部分**（部分 workflow 才有）：
- `BRIA_RMBG_ModelLoader_Zho` —— 1/2 个有
- `BRIA_RMBG_Zho` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 25.5 | - | 2 | 24% |
| 采样算法 | 6.5 | - | 1 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 1 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 25.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 24%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 45，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
