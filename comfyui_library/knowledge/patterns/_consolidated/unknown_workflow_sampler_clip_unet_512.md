---
name: unknown_workflow_sampler_clip_unet_512
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.871
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, ColorMatchV2, ComfyUI-Krea2T-Enhancer, ConditioningZeroOut, EmptyChromaRadianceLatentImage, EmptyLatentImage, Image Comparer (rgthree), KSamplerSelect, PiDConditioning, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SamplerCustom, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/PID+×+Krea2+细节增强引擎_2073373288369319937.json, 平台全量/PID × Krea2 Detail Enhancement Engine_2073788008070991873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_512

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/PID+×+Krea2+细节增强引擎_2073373288369319937.json、平台全量/PID × Krea2 Detail Enhancement Engine_2073788008070991873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `ColorMatchV2`
- `ComfyUI-Krea2T-Enhancer`
- `ConditioningZeroOut`
- `EmptyChromaRadianceLatentImage`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `PiDConditioning`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SamplerCustom`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | beta57 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | -1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 beta57，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 1，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
