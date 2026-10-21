---
name: unknown_workflow_upscale_sampler_clip_4
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.899667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBlend, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSamplerAdvanced, PreviewImage, ResolutionSelector, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2_文生图直出4K高清工作流_2086439888332873729.json, 图片生成/文生图/Krea2_文生图直出4K高清工作流_2087386381529210881.json, 图片生成/文生图/krea2-UE5法相_2095537231166529537.json, 图片生成/文生图/krea2-中秋_2101322859917438977.json, 图片生成/文生图/敦煌Krea2_2098303929271545858.json, 数字人/数字人/krea2-UE5角色定妆照_2090840952448573441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea2_文生图直出4K高清工作流_2086439888332873729.json、图片生成/文生图/Krea2_文生图直出4K高清工作流_2087386381529210881.json、图片生成/文生图/krea2-UE5法相_2095537231166529537.json、图片生成/文生图/krea2-中秋_2101322859917438977.json、图片生成/文生图/敦煌Krea2_2098303929271545858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageBlend`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `easy mathInt` —— 4/6 个有
- `Lora Loader Stack (rgthree)` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `llama_cpp_instruct_adv` —— 3/6 个有
- `llama_cpp_model_loader` —— 3/6 个有
- `ConditioningKrea2Rebalance` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `easy promptList` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1536 | 1536 - 1536 | 6 | 100% |
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，6 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
