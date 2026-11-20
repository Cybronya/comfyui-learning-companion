---
name: unknown_workflow_sampler_clip_unet_288
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88275
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI试戴美甲-穿戴甲换甲工作流_2094418586373804033.json, 图片生成/图生图/Flux 3_Image_Klein开源版-多图参考生图_2111065019705286658.json, 图片生成/图生图/MOSS Image-to-Image 2K Speed Edition 图生图2K极速版_2113063271686299649.json, 图片生成/图生图/MOSS-Image 一键洗图+高清修复_2114655615028129793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_288

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI试戴美甲-穿戴甲换甲工作流_2094418586373804033.json、图片生成/图生图/Flux 3_Image_Klein开源版-多图参考生图_2111065019705286658.json、图片生成/图生图/MOSS Image-to-Image 2K Speed Edition 图生图2K极速版_2113063271686299649.json、图片生成/图生图/MOSS-Image 一键洗图+高清修复_2114655615028129793.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ReferenceMultiLatent` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 16 | 3 | 76% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 1.5 | 3 | 82% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 16，3 个样本
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 1.5，3 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
