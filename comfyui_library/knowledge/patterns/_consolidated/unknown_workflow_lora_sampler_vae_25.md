---
name: unknown_workflow_lora_sampler_vae_25
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.755
common_nodes: [CLIPLoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImageIntegratedKSampler, QwenMultiangleCameraNode, SaveImage, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen2511多角度相机-Lora-高级工作流-免费课程同步流程_2010603981927616513.json, 平台全量/Qwen多角度控制_2117439553916198914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen2511多角度相机-Lora-高级工作流-免费课程同步流程_2010603981927616513.json、平台全量/Qwen多角度控制_2117439553916198914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImageIntegratedKSampler`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | 736 | - | 2 | 0% |
| 调度器 | 552 | - | 2 | 0% |
| 重绘幅度 | 6.66241e+13 | - | 2 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 736，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 调度器 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 重绘幅度 中位数 6.66241e+13，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 1.33248e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
