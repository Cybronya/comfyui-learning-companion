---
name: unknown_workflow_controlnet_lora_sampler_15
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.64725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-image-controlnet-canny_1958727731859111938.json, 图片生成/图生图/qwen-image-controlnet-depth_1958718480977707010.json, 图片生成/图生图/qwen-image-controlnet-inpaint_1958729644277186562.json, 图片生成/图生图/电商洗图 千问_1959245977016283138.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen-image-controlnet-canny_1958727731859111938.json、图片生成/图生图/qwen-image-controlnet-depth_1958718480977707010.json、图片生成/图生图/qwen-image-controlnet-inpaint_1958729644277186562.json、图片生成/图生图/电商洗图 千问_1959245977016283138.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
