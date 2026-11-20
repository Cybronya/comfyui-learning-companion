---
name: unknown_workflow_sampler_clip_unet_160
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一张图生成九宫格分镜！FLUX2-Klein，漫剧创作效率翻倍_2042605435265490946.json, 图片生成/图生图/一键批量生成动漫、短剧、角色分镜_2016397532888309761.json, 图片生成/图生图/动漫短剧_AI短剧一致性超强九宫格分镜图工作流_2013924585485373442.json, 图片生成/图生图/动漫短剧_AI短剧一致性超强九宫格分镜图工作流_2018226172726874113.json, 图片生成/图生图/电商详情-普通中文版_1988507050411999234.json, 图片生成/图生图/短剧 FLUX2-Klein一致性分镜生成_2016877010534010881.json, 图片生成/图生图/🦖FLUX-Klein超强9宫格分镜流_2015677364994318338.json, 图片生成/文生图/Flux2-Klein一自动分镜 一键生成_2014679299307085826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_160

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/一张图生成九宫格分镜！FLUX2-Klein，漫剧创作效率翻倍_2042605435265490946.json、图片生成/图生图/一键批量生成动漫、短剧、角色分镜_2016397532888309761.json、图片生成/图生图/动漫短剧_AI短剧一致性超强九宫格分镜图工作流_2013924585485373442.json、图片生成/图生图/动漫短剧_AI短剧一致性超强九宫格分镜图工作流_2018226172726874113.json、图片生成/图生图/电商详情-普通中文版_1988507050411999234.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `INTConstant` —— 7/8 个有
- `JWStringConcat` —— 7/8 个有
- `Qwen3_VQA` —— 7/8 个有
- `Text Multiline` —— 7/8 个有
- `easy promptLine` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `PreviewImage` —— 5/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `ImageFromBatch+` —— 1/8 个有
- `ImageListToBatch+` —— 1/8 个有
- `LayerUtility: TextJoin` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/8 个有
- `easy imageBatchToImageList` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
