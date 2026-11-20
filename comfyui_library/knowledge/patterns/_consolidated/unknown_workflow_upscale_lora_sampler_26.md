---
name: unknown_workflow_upscale_lora_sampler_26
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.87625
common_nodes: [CLIPLoader, Easy_QwenEdit2509, Fast Groups Muter (rgthree), Image Comparer (rgthree), ImageScaleRestore_UTK, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PurgeVRAM_UTK, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511_一键二次元动漫风格工作流_2027810038596767745.json, 图片生成/图生图/Qwen 2511_一键转3D国漫风格工作流_2026223216770945026.json, 图片生成/图生图/Qwen 2511_一键转半次元卡通风格工作流_2027794107984252929.json, 图片生成/图生图/转3D国漫风格工作流_2031015915982163970.json, 图片生成/图生图/转3D国漫风格工作流_2061094256328142849.json, 图片生成/图生图/转绘2d国漫风格_2062897698625380354.json, 图片生成/图生图/转绘3d国漫风格_2029549172390633474.json, 图片生成/图生图/转绘3d国漫风格_2064341278980141058.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen 2511_一键二次元动漫风格工作流_2027810038596767745.json、图片生成/图生图/Qwen 2511_一键转3D国漫风格工作流_2026223216770945026.json、图片生成/图生图/Qwen 2511_一键转半次元卡通风格工作流_2027794107984252929.json、图片生成/图生图/转3D国漫风格工作流_2031015915982163970.json、图片生成/图生图/转3D国漫风格工作流_2061094256328142849.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `Easy_QwenEdit2509`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleRestore_UTK`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PurgeVRAM_UTK`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/8 个有
- `LayerUtility: ImageReel` —— 1/8 个有
- `LayerUtility: ImageReelComposit` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
