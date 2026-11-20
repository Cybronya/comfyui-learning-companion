---
name: unknown_workflow_upscale_sampler_clip_82
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.493
common_nodes: [CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner, CheckpointLoaderSimple, EmptyLatentImage, ImageUpscaleWithModel, JWInteger, KSampler, KSamplerAdvanced, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, ttN text]
problems: []
missing: []
members: [平台全量/厚涂双面天使_1810149897524981761.json, 平台全量/喷射少女_1816675225504251906.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/厚涂双面天使_1810149897524981761.json、平台全量/喷射少女_1816675225504251906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

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
- `ControlNetApplyAdvanced` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `DiffControlNetLoader` —— 1/2 个有
- `LayerColor: Brightness & Contrast` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Zoe-DepthMapPreprocessor` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
