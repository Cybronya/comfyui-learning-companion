---
name: unknown_workflow_inpaint_sampler_clip_129
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.972
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/最快nunchaku-flux万物移除工作流_1938238750067462146.json, 平台全量/最快nunchaku-flux扩图工作流_1938585257178550274.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/最快nunchaku-flux万物移除工作流_1938238750067462146.json、平台全量/最快nunchaku-flux扩图工作流_1938585257178550274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INPAINT_InpaintWithModel` —— 1/2 个有
- `INPAINT_LoadInpaintModel` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.94 | - | 2 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.94，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
