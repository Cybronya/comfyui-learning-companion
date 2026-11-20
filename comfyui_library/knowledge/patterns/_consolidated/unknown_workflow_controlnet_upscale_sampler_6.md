---
name: unknown_workflow_controlnet_upscale_sampler_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.644
common_nodes: [ApplyInstantID, ApplyPulid, CLIPTextEncode, CR Image Input Switch (4 way), CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnything_V2, Display Int (rgthree), DownloadAndLoadDepthAnythingV2Model, EmptyLatentImage, FaceKeypointsPreprocessor, GetNode, ImageResize+, ImageUpscaleWithModel, ImpactInt, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LineArtPreprocessor, LoadImage, PortraitMaster_中文版, PreviewImage, PulidEvaClipLoader, PulidModelLoader, RH_Captioner, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, TextCombinerSix, UpscaleModelLoader, VAEEncode, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [图片生成/图生图/【AI琼瑶女主角】【AI为墨，古风为纸】_1908495449932898306.json, 平台全量/古风写真_1838168857839124481.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【AI琼瑶女主角】【AI为墨，古风为纸】_1908495449932898306.json、平台全量/古风写真_1838168857839124481.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `ApplyPulid`
- `CLIPTextEncode`
- `CR Image Input Switch (4 way)`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnything_V2`
- `Display Int (rgthree)`
- `DownloadAndLoadDepthAnythingV2Model`
- `EmptyLatentImage`
- `FaceKeypointsPreprocessor`
- `GetNode`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler (Efficient)`
- `LineArtPreprocessor`
- `LoadImage`
- `PortraitMaster_中文版`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidModelLoader`
- `RH_Captioner`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `TextCombinerSix`
- `UpscaleModelLoader`
- `VAEEncode`
- `easy cleanGpuUsed`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.55 | - | 2 | 91% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 15 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.55，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
