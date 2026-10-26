---
name: unknown_workflow_sampler_clip_unet_196
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.991
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/快速万物消除 擦除 去水印_2102605007383261185.json, 图片生成/图生图/换脸Flux2Klein多图编辑4B加速版_2057827199104929793.json, 图片生成/图生图/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2025838254557237250.json, 图片生成/图生图/换脸Flux2Klein多图编辑9B加速版_2031581292579528705.json, 图片生成/图生图/换脸换人换衣服 写实换装 人物一致 Flux2-Klein9b 保留服饰细节 多图编辑 多图编辑_2100011899302797314.json, 图片生成/图生图/换脸换人换衣服_写实换装_人物一致_Flux2-Klein9b_保留服饰细节_多图编辑_多图编辑_2101216470276595714.json, 图片生成/图生图/换装Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012781629911076866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_196

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/快速万物消除 擦除 去水印_2102605007383261185.json、图片生成/图生图/换脸Flux2Klein多图编辑4B加速版_2057827199104929793.json、图片生成/图生图/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2025838254557237250.json、图片生成/图生图/换脸Flux2Klein多图编辑9B加速版_2031581292579528705.json、图片生成/图生图/换脸换人换衣服 写实换装 人物一致 Flux2-Klein9b 保留服饰细节 多图编辑 多图编辑_2100011899302797314.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `CR Text` —— 6/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `JWFloat` —— 4/7 个有
- `EmptyFlux2LatentImage` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `ImageConcanate` —— 3/7 个有
- `easy imageSize` —— 3/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `InpaintCropImproved` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有
- `InpaintStitchImproved` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
