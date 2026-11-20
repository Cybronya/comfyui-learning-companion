---
name: unknown_workflow_sampler_clip_unet_151
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.875333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Redux 图片融合工作流_1902736324317851650.json, 图片生成/图生图/Flux_Redux官方工作流_1930169236486832129.json, "图片生成/图生图/WH-AI-Studio语义生图,形体转绘（还需研究）_2018161284826537986.json", 图片生成/图生图/图生图一键定制可爱IP形象_1884393250852163586.json, 图片生成/图生图/热血动漫风格｜真人转动漫_1935155915215839234.json, 图片生成/图生图/真人转动漫角色｜Flux 加速_1913224568469946369.json, 平台全量/Realism ➡ Anime (Flux Redux 8 step)_1897891763078811649.json, 平台全量/【上新】(IPA)-Flux redux model example_1860177378197598210.json, 平台全量/真人转动漫角色｜Flux 加速_1977340566189035522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_151

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux Redux 图片融合工作流_1902736324317851650.json、图片生成/图生图/Flux_Redux官方工作流_1930169236486832129.json、图片生成/图生图/WH-AI-Studio语义生图,形体转绘（还需研究）_2018161284826537986.json、图片生成/图生图/图生图一键定制可爱IP形象_1884393250852163586.json、图片生成/图生图/热血动漫风格｜真人转动漫_1935155915215839234.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
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
- `ModelSamplingFlux` —— 8/9 个有
- `StyleModelApply` —— 8/9 个有
- `ImageScale` —— 5/9 个有
- `ImageConcanate` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `easy imageSize` —— 4/9 个有
- `RH_Captioner` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `Get resolution [Crystools]` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `Images to RGB` —— 1/9 个有
- `InspyrenetRembg` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `StyleModelAdvancedApply` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
