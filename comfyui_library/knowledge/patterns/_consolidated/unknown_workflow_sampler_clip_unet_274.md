---
name: unknown_workflow_sampler_clip_unet_274
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.71975
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-Redux融图-海底城市_1912799861392244737.json, 图片生成/图生图/Flux图生图+JC2反推最强组合_1915271331674525697.json, 图片生成/图生图/Flux图生图JOY反推提示词_1906091968668028930.json, 图片生成/图生图/Flux图生图高清修复（超详细讲解使用）_1906105274531237889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_274

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX-Redux融图-海底城市_1912799861392244737.json、图片生成/图生图/Flux图生图+JC2反推最强组合_1915271331674525697.json、图片生成/图生图/Flux图生图JOY反推提示词_1906091968668028930.json、图片生成/图生图/Flux图生图高清修复（超详细讲解使用）_1906105274531237889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 3/4 个有
- `Joy_caption_two_load` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `EG_XZ_QH` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `ReduxAdvanced` —— 1/4 个有
- `StyleModelLoader` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
