---
name: unknown_workflow_sampler_clip_unet_247
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9385
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, INTConstant, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-Klein _ 一致性｜九宫格｜自定义角度 _ 一键出图_2022376852790190082.json, 图片生成/图生图/FLUX2-Klein-9b图像编辑_2033421207898431489.json, 图片生成/图生图/FLUX2-Klein-9b自动批量出图_2052346406085644290.json, 图片生成/图生图/产品换背景批量出图_2098992386100785154.json, 图片生成/图生图/星绘-FLUX2-Klein版一键多机位角度调整_2013878236958171138.json, 平台全量/FLUX2-Klein 一致性分镜生成 一键批量生成动漫 短剧 角色分镜  极速版 超强多功能 Kl_2015245157062414337.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_247

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein _ 一致性｜九宫格｜自定义角度 _ 一键出图_2022376852790190082.json、图片生成/图生图/FLUX2-Klein-9b图像编辑_2033421207898431489.json、图片生成/图生图/FLUX2-Klein-9b自动批量出图_2052346406085644290.json、图片生成/图生图/产品换背景批量出图_2098992386100785154.json、图片生成/图生图/星绘-FLUX2-Klein版一键多机位角度调整_2013878236958171138.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `INTConstant`
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
- `easy promptLine` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `CR Latent Batch Size` —— 2/6 个有
- `QwenMultiangleCameraNode` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Getter` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageGetter` —— 1/6 个有
- `KepStringList` —— 1/6 个有
- `Kep_JoinListAny` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `Setter` —— 1/6 个有
- `easy promptList` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
