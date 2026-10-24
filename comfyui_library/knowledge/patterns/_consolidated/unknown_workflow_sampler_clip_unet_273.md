---
name: unknown_workflow_sampler_clip_unet_273
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8405
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657.json, 图片生成/图生图/Flux_Krea_Redux_Advanced工作流_1966815491174096897.json, 图片生成/文生图/06.Flux_Redux_Advanced_1993297476142694401.json, 图片生成/文生图/Flux_Redux+openpose 参考图并出多视图_1900538927567249410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_273

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657.json、图片生成/图生图/Flux_Krea_Redux_Advanced工作流_1966815491174096897.json、图片生成/文生图/06.Flux_Redux_Advanced_1993297476142694401.json、图片生成/文生图/Flux_Redux+openpose 参考图并出多视图_1900538927567249410.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 3/4 个有
- `ReduxAdvanced` —— 3/4 个有
- `ControlNetLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SetUnionControlNetType` —— 2/4 个有
- `CLIPVisionEncode` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `DepthAnythingPreprocessor` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PerturbedAttentionGuidance` —— 1/4 个有
- `StyleAdvancedApply` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.55 | - | 2 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.55，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
