---
name: unknown_workflow_controlnet_ipadapter_upscale
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.830667
common_nodes: [Anything Everywhere, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ConstrainImage|pysssss, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, IPAdapterAdvanced, IPAdapterModelLoader, Image Comparer (rgthree), LayerMask: PersonMaskUltra V2, LoadImage, PreviewImage, SDXLPromptStyler, SaveImage, ShowText|pysssss, TransparentImage, UltimateSDUpscale, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/一键变换着装风格_1999360021819518978.json, 图片生成/图生图/一键迁移风格_1900359998558580737.json, 图片生成/图生图/一键迁移风格_1917440176207888385.json, 图片生成/图生图/一键迁移风格_2063276820279156738.json, 图片生成/图生图/一键风格化迁移_2020661507712880641.json, 图片生成/图生图/人物场景一键迁移_2015680381902655489.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键变换着装风格_1999360021819518978.json、图片生成/图生图/一键迁移风格_1900359998558580737.json、图片生成/图生图/一键迁移风格_1917440176207888385.json、图片生成/图生图/一键迁移风格_2063276820279156738.json、图片生成/图生图/一键风格化迁移_2020661507712880641.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `Image Comparer (rgthree)`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `PreviewImage`
- `SDXLPromptStyler`
- `SaveImage`
- `ShowText|pysssss`
- `TransparentImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 5/6 个有
- `CheckpointLoaderSimple` —— 5/6 个有
- `GrowMaskWithBlur` —— 5/6 个有
- `KSampler` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MaskPreview+` —— 5/6 个有
- `easy imageRemBg` —— 5/6 个有
- `CannyEdgePreprocessor` —— 1/6 个有
- `DepthAnythingV2Preprocessor` —— 1/6 个有
- `Efficient Loader` —— 1/6 个有
- `GetImageSize+` —— 1/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `KSampler (Efficient)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 30 | 30 - 30 | 6 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 100% |
| 调度器 | exponential | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 100%
- 调度器 最常用 exponential，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
