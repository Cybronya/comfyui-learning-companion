---
name: unknown_workflow_upscale_sampler_clip_85
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.731
common_nodes: [BNK_TiledKSampler, Bjornulf_ShowInt, CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ImageUpscaleWithModel, LayerColor: Brightness & Contrast, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, Upscale Model Loader, VAEDecode, VAEEncode, easy forLoopEnd, easy forLoopStart, easy imageCount, easy imageRemBg, easy showAnything]
problems: []
missing: []
members: [平台全量/循环处理多张图片抠图增强RMBG1.4_1980822880206372866.json, 平台全量/循环处理多张图片抠图增强_1925115543773507586.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/循环处理多张图片抠图增强RMBG1.4_1980822880206372866.json、平台全量/循环处理多张图片抠图增强_1925115543773507586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `BNK_TiledKSampler`
- `Bjornulf_ShowInt`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `LayerColor: Brightness & Contrast`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy imageRemBg`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1024 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1024 | - | 2 | 100% |
| 采样算法 | random | - | 2 | 100% |
| 调度器 | 28 | - | 2 | 100% |
| 重绘幅度 | 8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 random，2 个样本，一致性 100%
- 调度器 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1024，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：Prompt 约束强度(CFG) 观测到 1024，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 8，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
