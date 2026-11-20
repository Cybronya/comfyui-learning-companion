---
name: unknown_workflow_upscale_lora_sampler_25
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88775
common_nodes: [CLIPLoader, EmptyLatentImage, ImageBlend, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2 高清质感修复_2094422883429871618.json, 图片生成/图生图/Krea2_高清质感修复_2096519510642749441.json, 图片生成/图生图/Krea2_高清质感修复_2096878666562236418.json, 图片生成/文生图/Krea2_文生图直出4K高清工作流_2086439888332873729.json, 图片生成/文生图/Krea2_文生图直出4K高清工作流_2087386381529210881.json, 图片生成/文生图/krea2-UE5法相_2095537231166529537.json, 图片生成/文生图/krea2-中秋_2101322859917438977.json, 数字人/数字人/krea2-UE5角色定妆照_2090840952448573441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2 高清质感修复_2094422883429871618.json、图片生成/图生图/Krea2_高清质感修复_2096519510642749441.json、图片生成/图生图/Krea2_高清质感修复_2096878666562236418.json、图片生成/文生图/Krea2_文生图直出4K高清工作流_2086439888332873729.json、图片生成/文生图/Krea2_文生图直出4K高清工作流_2087386381529210881.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageBlend`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
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
- `CLIPTextEncode` —— 5/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `Krea2EditGroundedEncode` —— 3/8 个有
- `Krea2EditModelPatch` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `easy imageColorMatch` —— 3/8 个有
- `easy mathInt` —— 3/8 个有
- `llama_cpp_instruct_adv` —— 3/8 个有
- `llama_cpp_model_loader` —— 3/8 个有
- `Lora Loader Stack (rgthree)` —— 2/8 个有
- `PreviewAny` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `easy promptList` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 8 | 70% |
| 高度 | 1536 | 512 - 1536 | 8 | 57% |
| 采样步数 | fixed | - | 8 | 75% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 75% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，8 个样本
- 高度 中位数 1536，观测区间 512 - 1536，8 个样本
- 采样步数 最常用 fixed，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 75%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
