---
name: unknown_workflow_sampler_clip_unet_253
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.962
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/根据参考图修改图片_2016313387927478274.json, 图片生成/图生图/线稿_2016078729386139649.json, 图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json, 图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json, 视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_253

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/根据参考图修改图片_2016313387927478274.json、图片生成/图生图/线稿_2016078729386139649.json、图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json、图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json、视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
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
- `GetImageSize` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Int` —— 2/5 个有
- `1hew_TextListToString` —— 1/5 个有
- `DF_String_Concatenate` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PurgeVRAM_UTK` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `TextToLowercase` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
