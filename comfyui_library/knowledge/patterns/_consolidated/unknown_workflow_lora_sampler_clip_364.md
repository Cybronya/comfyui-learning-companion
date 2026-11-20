---
name: unknown_workflow_lora_sampler_clip_364
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, GetVideoComponents, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, ModelSamplingSD3, SamplerCustom, SaveVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanAnimate2Cache, WanAnimate2ToVideo]
problems: []
missing: []
members: [平台全量/A-11 WanAnimate2 动作迁移 换人换背景_2088247557133791233.json, 平台全量/Wan Animate2 动作迁移 新版模型_2086059595994320897.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_364

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/A-11 WanAnimate2 动作迁移 换人换背景_2088247557133791233.json、平台全量/Wan Animate2 动作迁移 新版模型_2086059595994320897.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SamplerCustom`
- `SaveVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanAnimate2Cache`
- `WanAnimate2ToVideo`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `ColorTransfer` —— 1/2 个有
- `ContextWindowsManual` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Int` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `VHS_GetImageCount` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
