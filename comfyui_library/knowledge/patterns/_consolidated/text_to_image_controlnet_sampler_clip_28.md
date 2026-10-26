---
name: text_to_image_controlnet_sampler_clip_28
type: Text To Image
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, SetUnionControlNetType, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SDXL文生图基础工作流_2000486653930110978.json, 图片生成/文生图/教学用controlnet控制工作流_1920050306917535746.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/SDXL文生图基础工作流_2000486653930110978.json、图片生成/文生图/教学用controlnet控制工作流_1920050306917535746.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 75% |
| 高度 | 1152 | - | 2 | 89% |
| ControlNet 权重 | 0.775 | - | 2 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- ControlNet 权重 中位数 0.775，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
