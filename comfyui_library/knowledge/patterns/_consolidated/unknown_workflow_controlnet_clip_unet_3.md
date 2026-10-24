---
name: unknown_workflow_controlnet_clip_unet_3
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Mesh2Motion首帧生成参考图_2052926077273681922.json, 图片生成/图生图/Qwen-inpaint 局部重绘=艾橘溪_1959188827518742529.json, 图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json, 图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Mesh2Motion首帧生成参考图_2052926077273681922.json、图片生成/图生图/Qwen-inpaint 局部重绘=艾橘溪_1959188827518742529.json、图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json、图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `KSampler` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `Int` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10.5 | 1 - 20 | 4 | 10% |
| 采样算法 | 4 | - | 2 | 100% |
| 调度器 | res_multistep | - | 4 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 10.5，观测区间 1 - 20，4 个样本，取值分散，一致性仅 10%
- 采样算法 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，4 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
