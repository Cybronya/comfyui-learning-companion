---
name: unknown_workflow_lora_sampler_unet_115
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8845
common_nodes: [CLIPLoader, Image Comparer (rgthree), LoadImage, LoraLoaderModelOnly, QwenImageIntegratedKSampler, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问Qwen-Image-Edit-2511-单_双_多图融图_2062783378109329409.json, 图片生成/图生图/千问Qwen-edit-2511-单图编辑_2062808274625449985.json, 图片生成/图生图/千问Qwen-edit-2511-多图编辑_2083881265262063618.json, 图片生成/图生图/千问Qwen-edit-2511-姿势参考_2062818658560331777.json, 图片生成/图生图/千问多图编辑工作流_2088603168807673858.json, 图片生成/图生图/姿势参考优化版工作流（qwen反推姿势动作+姿态图提取）_2087785459777884161.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/千问Qwen-Image-Edit-2511-单_双_多图融图_2062783378109329409.json、图片生成/图生图/千问Qwen-edit-2511-单图编辑_2062808274625449985.json、图片生成/图生图/千问Qwen-edit-2511-多图编辑_2083881265262063618.json、图片生成/图生图/千问Qwen-edit-2511-姿势参考_2062818658560331777.json、图片生成/图生图/千问多图编辑工作流_2088603168807673858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `DWPreprocessor` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | 0 | 0 - 0 | 6 | 100% |
| 调度器 | 0 | 0 - 0 | 6 | 100% |
| 重绘幅度 | 999 | 999 - 6.80093e+14 | 6 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0，观测区间 0 - 0，6 个样本，取值集中（一致性 100%）
- 调度器 中位数 0，观测区间 0 - 0，6 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 999，观测区间 999 - 6.80093e+14，6 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 6.80093e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
