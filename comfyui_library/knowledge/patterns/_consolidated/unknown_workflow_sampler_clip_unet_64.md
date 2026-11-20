---
name: unknown_workflow_sampler_clip_unet_64
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.904143
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/flux_redux_model_example.json, 图片生成/反推提示词/FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874.json, 图片生成/图生图/FLUX_Redux_纯净(图生图)_1920006003302006785.json, 图片生成/图生图/Flux Redux洗图工作流_1955898391345680385.json, 图片生成/图生图/Flux Redux洗图工作流_2020675664122224641.json, 图片生成/图生图/Flux+Redux洗图工作流_1990713474449891329.json, 图片生成/图生图/Flux-Redux洗图工作流_1999806514867171330.json, 图片生成/图生图/Flux_Redux洗图工作流（极致写实小红书风格模仿美少女）_1984262638253260802.json, 图片生成/图生图/Flux_Redux洗图工作流（男人金钱豹）_1984268576913833986.json, 图片生成/图生图/flux redux洗图、风格参考工作流_1965654086169317378.json, 图片生成/图生图/redux洗图工作流_1980567344630120450.json, 图片生成/文生图/Flux基础文生图工作流_1997984984822611970.json, 图片生成/文生图/flux洗图工作流_1981983365639356418.json, 平台全量/Flux基础文生图工作流_2070667707422437378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_redux_model_example.json、图片生成/反推提示词/FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874.json、图片生成/图生图/FLUX_Redux_纯净(图生图)_1920006003302006785.json、图片生成/图生图/Flux Redux洗图工作流_1955898391345680385.json、图片生成/图生图/Flux Redux洗图工作流_2020675664122224641.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 12/14 个有
- `Image Comparer (rgthree)` —— 12/14 个有
- `StyleModelApplySimple` —— 12/14 个有
- `DetailDaemonSamplerNode` —— 11/14 个有
- `JWImageResizeByLongerSide` —— 11/14 个有
- `LoraLoader` —— 11/14 个有
- `VAEEncode` —— 11/14 个有
- `Joy_caption_two` —— 10/14 个有
- `Joy_caption_two_load` —— 10/14 个有
- `ShowText|pysssss` —— 10/14 个有
- `EmptySD3LatentImage` —— 3/14 个有
- `FluxGuidance` —— 3/14 个有
- `ModelSamplingFlux` —— 2/14 个有
- `StyleModelApply` —— 2/14 个有
- `CR Text Concatenate` —— 1/14 个有
- `DeepTranslatorTextNode` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `PreviewImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 11 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，11 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
