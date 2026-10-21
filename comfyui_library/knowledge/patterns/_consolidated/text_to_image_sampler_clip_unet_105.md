---
name: text_to_image_sampler_clip_unet_105
type: Text To Image
frequency: 4
level: strong
coverage: 0.76825
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PrimitiveStringMultiline, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 MIX融合版 东方审美 高清直出工作流_2070837337231282177.json, 图片生成/文生图/Krea 2 Text to Image 文生图 (超强写实质感)_2075054887305568258.json, 图片生成/文生图/Krea2_文生图_2071154593135939585.json, 图片生成/文生图/RedCraft Krea 2 红潮版_2075054152518029314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea 2 MIX融合版 东方审美 高清直出工作流_2070837337231282177.json、图片生成/文生图/Krea 2 Text to Image 文生图 (超强写实质感)_2075054887305568258.json、图片生成/文生图/Krea2_文生图_2071154593135939585.json、图片生成/文生图/RedCraft Krea 2 红潮版_2075054152518029314.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `DuckDecodeNode` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `ZML_SelectText` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有
- `mxSlider2D` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 9 | 8 - 10 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，观测区间 8 - 10，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
