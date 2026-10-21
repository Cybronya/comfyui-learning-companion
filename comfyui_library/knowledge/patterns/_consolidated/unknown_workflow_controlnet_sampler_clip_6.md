---
name: unknown_workflow_controlnet_sampler_clip_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.841
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, ImageConcanate, KSamplerSelect, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, CR Prompt Text]
members: [图片生成/文生图/1925220714343768066.json, 视频生成/图生视频/1915458738965385218.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1925220714343768066.json、视频生成/图生视频/1915458738965385218.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageConcanate`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `DepthAnything_V2` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `NunchakuPulidApply` —— 1/2 个有
- `NunchakuPulidLoader` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、CR Prompt Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
