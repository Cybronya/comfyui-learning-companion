---
name: unknown_workflow_sampler_clip_unet_342
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.897
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/爆分游戏的三个爆分状态_2086696888518135810.json, 平台全量/Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177.json, 平台全量/YJ-FAST-处理衣服-jianan-tmp0-step0_2033547148742103041.json, 平台全量/flux Klein 单图-双图-三图编辑_2065080679817371649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_342

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/爆分游戏的三个爆分状态_2086696888518135810.json、平台全量/Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177.json、平台全量/YJ-FAST-处理衣服-jianan-tmp0-step0_2033547148742103041.json、平台全量/flux Klein 单图-双图-三图编辑_2065080679817371649.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `GetImageSize` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerColor: AutoAdjustV2` —— 2/4 个有
- `AILab_ImageCombiner` —— 1/4 个有
- `BiRefNetRMBG` —— 1/4 个有
- `ColorMatchV2` —— 1/4 个有
- `ImageBlur` —— 1/4 个有
- `Int` —— 1/4 个有
- `InvertMask` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MuyeSizeSelector` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
