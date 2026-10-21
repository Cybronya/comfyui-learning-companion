---
name: unknown_workflow_controlnet_upscale_latent_upscale_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8695
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Seed, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, KSamplerAdvanced, LatentUpscaleBy, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SetUnionControlNetType, Text, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image2512 ControlNET 使用方法（超高分辨率输出）_2010931911048306690.json, 图片生成/文生图/灵魂画师（QwenControlNet）_2021195345354559489.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen Image2512 ControlNET 使用方法（超高分辨率输出）_2010931911048306690.json、图片生成/文生图/灵魂画师（QwenControlNet）_2021195345354559489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetUnionControlNetType`
- `Text`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `Float` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 2 | 87% |
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | ddim | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 ddim，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
