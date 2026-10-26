---
name: unknown_workflow_sampler_clip_unet_154
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.986875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2 klein 任意位置皮肤完美克隆（无限制）_2012907749159473153.json, 图片生成/图生图/flux2-Klein-单图编辑（4B）_2012091014151938050.json, 图片生成/图生图/flux2-Klein-单图编辑（9B）_2012088384096833537.json, 图片生成/图生图/flux2-Klein-图像多角度生成_2012189967140786177.json, 图片生成/图生图/flux2-Klein-换脸(色差偏移修正版)_2012337568234344450.json, 图片生成/图生图/flux2-Klein-最快换脸_2012192553822593025.json, 图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json, 图片生成/图生图/kleinface 换头换脸工作流 Flux2-Klein-9B 人物换头AI智能面部替换高清换头脸_2016848786680713218.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_154

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/flux2 klein 任意位置皮肤完美克隆（无限制）_2012907749159473153.json、图片生成/图生图/flux2-Klein-单图编辑（4B）_2012091014151938050.json、图片生成/图生图/flux2-Klein-单图编辑（9B）_2012088384096833537.json、图片生成/图生图/flux2-Klein-图像多角度生成_2012189967140786177.json、图片生成/图生图/flux2-Klein-换脸(色差偏移修正版)_2012337568234344450.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 6/8 个有
- `FluxKontextImageScale` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `YC Color Match` —— 2/8 个有
- `easy int` —— 2/8 个有
- `DuckHideNode` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `ImageSmartSharpen+` —— 1/8 个有
- `QwenMultiangleCameraNode` —— 1/8 个有
- `SaveImageAndMetadata_` —— 1/8 个有
- `easy positive` —— 1/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
