---
name: unknown_workflow_controlnet_sampler_clip_18
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.823333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, ImageConcanate, ImpactSwitch, JWImageResizeByLongerSide, JWInteger, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuPulidApply, NunchakuPulidLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json, 图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json, 图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json、图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json、图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImpactSwitch`
- `JWImageResizeByLongerSide`
- `JWInteger`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `CropFace` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
