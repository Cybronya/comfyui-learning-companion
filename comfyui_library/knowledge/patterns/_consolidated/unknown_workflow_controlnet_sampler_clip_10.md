---
name: unknown_workflow_controlnet_sampler_clip_10
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.85
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, ImageConcanate, ImpactSwitch, JWImageResizeByLongerSide, JWInteger, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuPulidApply, NunchakuPulidLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json, 图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json, 图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json, 平台全量/最新双截棍模型＋最新姿态深度控制模型2.0_1925515888458387458.json, 平台全量/洗稿加pulid换脸_1926938593586221057.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json、图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json、图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json、平台全量/最新双截棍模型＋最新姿态深度控制模型2.0_1925515888458387458.json、平台全量/洗稿加pulid换脸_1926938593586221057.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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
- `EmptySD3LatentImage` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `DepthAnything_V2` —— 3/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/5 个有
- `OpenposePreprocessor` —— 3/5 个有
- `RH_Captioner` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 2/5 个有
- `CropFace` —— 2/5 个有
- `ImageBlend` —— 2/5 个有
- `Text Concatenate` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy anythingIndexSwitch` —— 2/5 个有
- `BiRefNetRMBG` —— 1/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `DWPreprocessor` —— 1/5 个有
- `LayerUtility: ImageBlendAdvance` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: LaMa` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `NunchakuFluxLoraLoader` —— 1/5 个有
- `NunchakuTextEncoderLoader` —— 1/5 个有
- `ReduxAdvanced` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `StyleModelLoader` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，5 个样本，取值集中（一致性 100%）
