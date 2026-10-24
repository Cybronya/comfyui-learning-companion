---
name: unknown_workflow_sampler_clip_unet_207
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8675
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Redux 图片融合工作流_1902736324317851650.json, 图片生成/图生图/Flux_Redux官方工作流_1930169236486832129.json, "图片生成/图生图/WH-AI-Studio语义生图,形体转绘（还需研究）_2018161284826537986.json", 图片生成/图生图/图生图一键定制可爱IP形象_1884393250852163586.json, 图片生成/图生图/热血动漫风格｜真人转动漫_1935155915215839234.json, 图片生成/图生图/真人转动漫角色｜Flux 加速_1913224568469946369.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_207

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux Redux 图片融合工作流_1902736324317851650.json、图片生成/图生图/Flux_Redux官方工作流_1930169236486832129.json、图片生成/图生图/WH-AI-Studio语义生图,形体转绘（还需研究）_2018161284826537986.json、图片生成/图生图/图生图一键定制可爱IP形象_1884393250852163586.json、图片生成/图生图/热血动漫风格｜真人转动漫_1935155915215839234.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ModelSamplingFlux` —— 5/6 个有
- `StyleModelApply` —— 5/6 个有
- `ImageScale` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `Get resolution [Crystools]` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `Images to RGB` —— 1/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `StyleModelAdvancedApply` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
