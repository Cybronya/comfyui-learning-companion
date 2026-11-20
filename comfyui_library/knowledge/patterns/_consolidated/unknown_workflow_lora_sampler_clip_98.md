---
name: unknown_workflow_lora_sampler_clip_98
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6328
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FlipSigmas, FluxDeGuidance, GetNode, INTConstant, ImageConcatMulti, ImageScale, InFluxModelSamplingPred, LoadImage, LoraLoaderModelOnly, OutFluxModelSamplingPred, PreviewImage, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX逆采样图像_1850813965826748417.json, 图片生成/图生图/RF-Edit风格转绘-上传一张图片，生成漫画风格，哈哈，意想不到的效果~_2018160574168829953.json, 图片生成/图生图/RF-Edit风格转绘_1897148571110776833.json, 图片生成/图生图/宠物一键转绘工作流_1899681982450941953.json, 图片生成/文生图/fluxtopaz RF inverse + controlnet_1958569814094725122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX逆采样图像_1850813965826748417.json、图片生成/图生图/RF-Edit风格转绘-上传一张图片，生成漫画风格，哈哈，意想不到的效果~_2018160574168829953.json、图片生成/图生图/RF-Edit风格转绘_1897148571110776833.json、图片生成/图生图/宠物一键转绘工作流_1899681982450941953.json、图片生成/文生图/fluxtopaz RF inverse + controlnet_1958569814094725122.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxDeGuidance`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageScale`
- `InFluxModelSamplingPred`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConfigureModifiedFlux` —— 3/5 个有
- `FlowEditForwardSampler` —— 3/5 个有
- `FlowEditReverseSampler` —— 3/5 个有
- `Get Image Size` —— 3/5 个有
- `LayerMask: LoadFlorence2Model` —— 3/5 个有
- `LayerUtility: Florence2Image2Prompt` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PrepareAttnBank` —— 3/5 个有
- `StringFunction|pysssss` —— 3/5 个有
- `FluxForwardODESampler` —— 2/5 个有
- `FluxReverseODESampler` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ControlNetLoader` —— 1/5 个有
- `FluxUnionControlNetApply` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | canny | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
