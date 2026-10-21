---
name: unknown_workflow_sampler_clip_unet_103
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.933286
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1954125145533247489.json, 视频生成/图生视频/2034620365376331777.json, 视频生成/图生视频/1950374828178104322.json, 视频生成/图生视频/1956204129557336066.json, 视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json, 视频生成/文生视频/1949992424375500801.json, 视频生成/文生视频/1969656393957601281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_103

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1954125145533247489.json、视频生成/图生视频/2034620365376331777.json、视频生成/图生视频/1950374828178104322.json、视频生成/图生视频/1956204129557336066.json、视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `WanImageToVideo` —— 4/7 个有
- `Label (rgthree)` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `Wan22FunControlToVideo` —— 2/7 个有
- `WanFirstLastFrameToVideo` —— 2/7 个有
- `DWPreprocessor` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `WanFunInpaintToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 57% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 7 | 32% |
| 采样算法 | 3.5 | 1 - 4 | 7 | 48% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，7 个样本，取值分散，一致性仅 32%
- 采样算法 中位数 3.5，观测区间 1 - 4，7 个样本，取值分散，一致性仅 48%
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
